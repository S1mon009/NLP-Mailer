"""
Email subject tagging using machine learning and Gmail.

This module provides the :class:`GmailSubjectTagger` class, which combines
the Gmail API integration with the machine learning-based
:class:`~src.services.email_categorizer.EmailCategorizer` to automatically
categorize emails and tag their subjects.

The module supports processing multiple emails, confidence thresholds,
dry-run mode, Gmail label management, and testing individual emails.
"""
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple
from src.integrations.gmail_connector import GmailConnector
from src.services.email_categorizer import EmailCategorizer
from src.config.config import MIN_CONFIDENCE


class GmailSubjectTagger:
    """
    Coordinate Gmail access and machine learning-based email tagging.

    This class is responsible for fetching emails from Gmail, categorizing
    them using :class:`EmailCategorizer`, and applying corresponding Gmail
    labels. It can also preview changes without modifying Gmail using
    dry-run mode.

    Attributes:
        gmail: Gmail API connector used to authenticate, retrieve emails,
            create labels, and apply labels.
        categorizer: Machine learning-based email categorizer.
        label_cache: Cache containing Gmail label IDs indexed by category.
    """
    def __init__(self) -> None:
        """
        Initialize the Gmail subject tagger.

        Creates a Gmail connector, initializes the email categorizer,
        and prepares an empty cache for Gmail label IDs.
        """
        self.gmail = GmailConnector()
        self.categorizer = EmailCategorizer()
        self.label_cache = {}

    def setup(self) -> Any:
        """Set up the tagger and authenticate with Gmail.

        If no trained categorization model exists, the method trains
        a new model using the configured training dataset. After ensuring
        that a model is available, it authenticates the Gmail connector.

        Returns:
            The result of the Gmail authentication process.
        """
        if not self.categorizer.model_path.exists():
            print("No trained model found. Training...")
            self.categorizer.train()

        return self.gmail.authenticate()

    def tag_emails(self,
                   max_emails:int = 50, query:str = '',
                   dry_run:bool = False,
                   min_confidence: Optional[float] = None)-> Optional[List[Dict[str, Any]]]:
        """
        Fetch, categorize, and tag email subjects.

        Retrieves emails from Gmail using the provided search query,
        categorizes each email, and prepares a category tag for messages
        whose prediction confidence meets the configured threshold.

        Emails that already contain a recognized category tag are skipped.
        When ``dry_run`` is enabled, the method only previews the changes
        and does not modify Gmail labels.

        Args:
            max_emails: Maximum number of emails to process.
            query: Gmail search query used to filter messages.
                An empty string retrieves emails without an additional filter.
            dry_run: If ``True``, preview the tagging operation without
                applying labels to Gmail.
            min_confidence: Minimum prediction confidence required for an
                email to be tagged. If ``None``, the configured
                ``MIN_CONFIDENCE`` value is used.

        Returns:
            A list of dictionaries containing information about emails
            selected for tagging. Returns ``None`` if no emails are found.

        Note:
            The current implementation prepares the new subject value
            but does not directly update the Gmail message subject.
            It applies the corresponding Gmail label.
        """
        if min_confidence is None:
            min_confidence = MIN_CONFIDENCE

        print(f"Fetching up to {max_emails} emails from Gmail...")
        if query:
            print(f"Query: {query}")

        emails = self.gmail.get_emails(max_results=max_emails, query=query)

        if not emails:
            print("No emails found")
            return

        print(f"Fetched {len(emails)} emails")
        print("Categorizing and tagging subjects...")
        print(f"Min confidence: {min_confidence:.0%}")

        results = []
        tagged = 0
        skipped = 0
        low_confidence = 0

        for i, email in enumerate(emails, 1):
            if self.categorizer.has_category_tag(email['subject']):
                skipped += 1
                continue

            category, confidence = self.categorizer.categorize(email)

            if i <= 5:  # Show first 5 for debugging
                subject_preview = email['subject'][:50]
                print(f"   [{i}] \"{subject_preview}...\" → {category} ({confidence:.1%})")

            # Skip if confidence too low
            if confidence < min_confidence:
                low_confidence += 1
                continue

            # Create label name
            label_name = f"📧 {category}"

            results.append({
                'email': email,
                'category': category,
                'confidence': confidence,
                'label_name': label_name,
                'new_subject': f"[{category}] {email['subject']}"
            })

            # Apply label
            if not dry_run:
                if category not in self.label_cache:
                    label_id = self.gmail.create_label(label_name)
                    if label_id:
                        self.label_cache[category] = label_id

                if category in self.label_cache:
                    self.gmail.apply_label(email['id'], self.label_cache[category])
                    tagged += 1
            else:
                tagged += 1

            if i % 10 == 0:
                print(f"Processed {i}/{len(emails)}...")

        print("Processing complete!")
        self._show_summary(results, tagged, skipped, low_confidence, dry_run)

        return results

    def _show_summary(self,
        results: List[Dict[str, Any]],
        tagged: int,
        skipped: int,
        low_confidence: int,
        dry_run: bool
    ) -> None:
        """
        Display a summary of the email tagging operation.

        Prints the number of tagged, skipped, and low-confidence emails.
        When tagging results are available, also displays a breakdown
        of categories and sample emails for each category.

        Args:
            results: List of email tagging results generated by
                :meth:`tag_emails`.
            tagged: Number of emails successfully tagged or previewed.
            skipped: Number of emails that already contained a category tag.
            low_confidence: Number of emails skipped because their prediction
                confidence was below the configured threshold.
            dry_run: Indicates whether the operation was performed in
                dry-run mode.

        Returns:
            None.
        """
        print("="*60)
        print("TAGGING SUMMARY")
        print("="*60)

        if dry_run:
            print("DRY RUN MODE - No changes applied")

        print(f"Tagged: {tagged}")
        print(f"Already tagged: {skipped}")
        print(f"Low confidence (skipped): {low_confidence}")

        if results:
            print("Sample tagged emails:")
            category_counts = Counter(r['category'] for r in results)

            for category, count in category_counts.most_common():
                print(f"{category} ({count}):")
                samples = [r for r in results if r['category'] == category][:3]
                for sample in samples:
                    old = sample['email']['subject'][:40]
                    new = sample['new_subject'][:50]
                    conf = sample['confidence']
                    print(f"• {old}...")
                    print(f"→ {new}... ({conf:.1%})")

    def test_email(self, subject: str, body:str = '') -> Tuple[str, float]:
        """
        Test email categorization without modifying Gmail.

        Creates a temporary email from the provided subject and body,
        passes it through the categorization model, and displays the
        predicted category and confidence score.

        Args:
            subject: Subject of the email to categorize.
            body: Optional body content of the email.

        Returns:
            A tuple containing the predicted category and confidence score.
        """
        email = {'subject': subject, 'body': body}
        category, confidence = self.categorizer.categorize(email)

        print(f"Original: {subject}")
        print(f"Tagged: [{category}] {subject}")
        print(f"Confidence: {confidence:.2%}")

        return category, confidence

    def clear_labels(self) -> None:
        """Remove all email categorization labels from Gmail.

        Calls the Gmail connector to remove all labels created for
        email categorization and displays the number of removed labels.

        Returns:
            None.
        """
        print("Clearing category labels...")
        removed = self.gmail.remove_category_labels()
        print(f"Removed {removed} category labels")
