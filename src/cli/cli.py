"""
Command-line interface for the Gmail Subject Auto-Tagger.

This module provides the interactive command-line interface used to
control the Gmail Subject Auto-Tagger. It allows users to tag emails,
preview categorization results, filter emails by status or date,
configure the confidence threshold, test email categorization, and
remove existing category labels.

The `CLI` class acts as the main interface between the user
and the `src.services.tagger.GmailSubjectTagger` service.
"""
import os
from src.services.tagger import GmailSubjectTagger

class CLI:
    """
    Provide an interactive command-line interface for Gmail tagging.

    The CLI handles user input and delegates email processing operations
    to an instance of :class:`~src.services.tagger.GmailSubjectTagger`.

    Attributes:
        tagger (GmailSubjectTagger): Service responsible for Gmail email
            processing, categorization, and label management.
    """

    def __init__(self) -> None:
        """
        Initialize the command-line interface. 
        Creates a new class `src.services.tagger.GmailSubjectTagger` 
        instance that is used to perform all Gmail-related operations.
        """
        self.tagger = GmailSubjectTagger()

    def run(self) -> None:
        """
        Start the interactive command-line interface.

        Displays the available commands and continuously waits for user
        input until the ``quit`` command is entered.

        Supported commands include:

        - **``tag [N]``** - Tag the N most recent emails. Defaults to 20 emails.
        - **``preview [N]``** - Preview the categorization of the N most recent emails without modifying Gmail labels.
        - **``unread``** - Tag up to 50 unread emails.
        - **``today``** - Tag up to 50 emails received within the last day.
        - **``week``** - Tag up to 100 emails received within the last seven days.
        - **``test``** - Test email categorization by providing a subject and optional body.
        - **``confidence``** - Set a custom confidence threshold and specify the number of emails to process.
        - **``clear``** - Remove all category labels after user confirmation.
        - **``quit``** - Exit the interactive CLI.

        Returns:
            None: The method runs until the user exits the application.
        """
        print("n" + "="*60)
        print("GMAIL SUBJECT TAGGER")
        print("="*60)
        print("Note: Gmail API doesn't allow direct subject modification.")
        print("This tool adds colorful labels that appear next to subjects!")
        print("Commands:")
        print("  tag [N] - Tag N recent emails (default: 20)")
        print("  preview [N] - Preview what would be tagged")
        print("  unread - Tag only unread emails")
        print("  today - Tag emails from today")
        print("  week - Tag emails from this week")
        print("  test - Test categorization")
        print("  confidence - Set custom confidence threshold")
        print("  clear - Remove all category labels")
        print("  quit - Exit")

        while True:
            print("-"*60)
            cmd = input("Command: ").strip().lower()

            if cmd == 'quit':
                print("Goodbye!")
                os.remove('token.json')  # Remove token file to force re-authentication next time
                break

            elif cmd.startswith('tag'):
                parts = cmd.split()
                n = int(parts[1]) if len(parts) > 1 else 20
                self.tagger.tag_emails(max_emails=n, dry_run=False)

            elif cmd.startswith('preview'):
                parts = cmd.split()
                n = int(parts[1]) if len(parts) > 1 else 20
                self.tagger.tag_emails(max_emails=n, dry_run=True)

            elif cmd == 'unread':
                self.tagger.tag_emails(max_emails=50, query='is:unread', dry_run=False)

            elif cmd == 'today':
                self.tagger.tag_emails(max_emails=50, query='newer_than:1d', dry_run=False)

            elif cmd == 'week':
                self.tagger.tag_emails(max_emails=100, query='newer_than:7d', dry_run=False)

            elif cmd == 'confidence':
                try:
                    conf = float(input("Enter confidence threshold (0.0-1.0): "))
                    if 0 <= conf <= 1:
                        n = int(input("How many emails to tag? ") or "20")
                        self.tagger.tag_emails(max_emails=n, dry_run=False, min_confidence=conf)
                    else:
                        print("Must be between 0.0 and 1.0")
                except ValueError:
                    print("Invalid number")

            elif cmd == 'test':
                subject = input("Subject: ")
                body = input("Body (optional): ")
                self.tagger.test_email(subject, body)

            elif cmd == 'clear':
                confirm = input("Remove all category labels? (yes/no): ")
                if confirm.lower() == 'yes':
                    self.tagger.clear_labels()

            else:
                print("Unknown command")
