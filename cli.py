from tagger import GmailSubjectTagger


class CLI:
    '''Command-line interface for Gmail Subject Tagger'''
    
    def __init__(self):
        self.tagger = GmailSubjectTagger()
    
    def run(self):
        '''Run interactive mode'''
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