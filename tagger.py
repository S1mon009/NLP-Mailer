from collections import Counter
from gmail_connector import GmailConnector
from email_categorizer import EmailCategorizer
from config import MIN_CONFIDENCE


class GmailSubjectTagger:
    '''Main application that tags email subjects'''
    
    def __init__(self):
        self.gmail = GmailConnector()
        self.categorizer = EmailCategorizer()
        self.label_cache = {}
    
    def setup(self):
        '''Setup and train model if needed'''
        if not self.categorizer.model_path.exists():
            print("\\n⚠️  No trained model found. Training...")
            self.categorizer.train()
        
        return self.gmail.authenticate()
    
    def tag_emails(self, max_emails=50, query='', dry_run=False, min_confidence=None):
        '''
        Fetch and tag email subjects with categories
        
        Args:
            max_emails: Number of emails to process
            query: Gmail search query
            dry_run: If True, only preview changes
            min_confidence: Minimum confidence threshold
        '''
        if min_confidence is None:
            min_confidence = MIN_CONFIDENCE
        
        print(f"\\n📬 Fetching up to {max_emails} emails from Gmail...")
        if query:
            print(f"   Query: {query}")
        
        emails = self.gmail.get_emails(max_results=max_emails, query=query)
        
        if not emails:
            print("No emails found")
            return
        
        print(f"✓ Fetched {len(emails)} emails")
        print(f"\\n🤖 Categorizing and tagging subjects...")
        print(f"   Min confidence: {min_confidence:.0%}")
        
        results = []
        tagged = 0
        skipped = 0
        low_confidence = 0
        
        for i, email in enumerate(emails, 1):
            # Skip if already tagged
            if self.categorizer.has_category_tag(email['subject']):
                skipped += 1
                continue
            
            category, confidence = self.categorizer.categorize(email)
            
            # Debug: show what we got
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
                print(f"   Processed {i}/{len(emails)}...")
        
        print(f"\\n✓ Processing complete!")
        self._show_summary(results, tagged, skipped, low_confidence, dry_run)
        
        return results
    
    def _show_summary(self, results, tagged, skipped, low_confidence, dry_run):
        '''Display tagging summary'''
        print("\\n" + "="*60)
        print("📊 TAGGING SUMMARY")
        print("="*60)
        
        if dry_run:
            print("\\n🔍 DRY RUN MODE - No changes applied")
        
        print(f"\\n📌 Tagged: {tagged}")
        print(f"⏭️  Already tagged: {skipped}")
        print(f"⚠️  Low confidence (skipped): {low_confidence}")
        
        if results:
            print(f"\\n📋 Sample tagged emails:")
            category_counts = Counter(r['category'] for r in results)
            
            for category, count in category_counts.most_common():
                print(f"\\n  {category} ({count}):")
                samples = [r for r in results if r['category'] == category][:3]
                for sample in samples:
                    old = sample['email']['subject'][:40]
                    new = sample['new_subject'][:50]
                    conf = sample['confidence']
                    print(f"    • {old}...")
                    print(f"      → {new}... ({conf:.1%})")
    
    def test_email(self, subject, body=''):
        '''Test categorization on a single email'''
        email = {'subject': subject, 'body': body}
        category, confidence = self.categorizer.categorize(email)
        
        print(f"\\n  Original: {subject}")
        print(f"  Tagged: [{category}] {subject}")
        print(f"  Confidence: {confidence:.2%}")
        
        return category, confidence
    
    def clear_labels(self):
        '''Remove all category labels'''
        print("\\n🗑️  Clearing category labels...")
        removed = self.gmail.remove_category_labels()
        print(f"✓ Removed {removed} category labels")