import os.path
import base64
from typing import Optional, List, Dict, Any
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config import GMAIL_CREDENTIALS_FILE, GMAIL_TOKEN_FILE, GMAIL_SCOPES, LABEL_COLORS


class GmailConnector:
    '''Handle Gmail API connection and operations'''
    
    def __init__(self):
        self.credentials_file = GMAIL_CREDENTIALS_FILE
        self.token_file = GMAIL_TOKEN_FILE
        self.service: Optional[Any] = None  # Type hint fix for dynamic API
        
    def authenticate(self):
        '''Authenticate with Gmail API'''
        creds = None
        
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, GMAIL_SCOPES)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(self.credentials_file):
                    print("Gmail credentials not found!")
                    print("Setup instructions:")
                    print("1. Go to: https://console.cloud.google.com")
                    print("2. Create a project and enable Gmail API")
                    print("3. Create OAuth 2.0 credentials")
                    print("4. Download as 'credentials.json'")
                    print("5. Place in same directory as this script")
                    return False
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, GMAIL_SCOPES)
                creds = flow.run_local_server(port=0)
            
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())
        
        self.service = build('gmail', 'v1', credentials=creds)
        print("Gmail authentication successful")
        return True
    
    def get_emails(self, max_results: int = 50, query: str = '') -> List[Dict[str, Any]]:
        '''Fetch emails from Gmail'''
        try:
            # Type annotation suppression comments for IDE
            results = self.service.users().messages().list(  # type: ignore
                userId='me', maxResults=max_results, q=query).execute()
            messages = results.get('messages', [])
            
            emails = []
            for msg in messages:
                email_data = self.service.users().messages().get(  # type: ignore
                    userId='me', id=msg['id'], format='full').execute()
                
                email = self._parse_email(email_data)
                emails.append(email)
            
            return emails
        except HttpError as error:
            print(f"Error fetching emails: {error}")
            return []
    
    def _parse_email(self, email_data: Dict[str, Any]) -> Dict[str, Any]:
        '''Parse Gmail API email data'''
        headers = email_data['payload']['headers']
        
        subject = ''
        sender = ''
        date = ''
        
        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
            elif header['name'] == 'From':
                sender = header['value']
            elif header['name'] == 'Date':
                date = header['value']
        
        body = self._get_email_body(email_data['payload'])
        
        return {
            'id': email_data['id'],
            'threadId': email_data['threadId'],
            'subject': subject,
            'sender': sender,
            'date': date,
            'body': body,
            'labels': email_data.get('labelIds', [])
        }
    
    def _get_email_body(self, payload: Dict[str, Any]) -> str:
        '''Extract email body from payload'''
        body = ''
        
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    if 'data' in part['body']:
                        body = base64.urlsafe_b64decode(
                            part['body']['data']).decode('utf-8')
                        break
        elif 'body' in payload and 'data' in payload['body']:
            body = base64.urlsafe_b64decode(
                payload['body']['data']).decode('utf-8')
        
        return body[:500]
    
    def create_label(self, label_name: str) -> Optional[str]:
        '''Create a Gmail label'''
        try:
            # Check if label exists
            labels = self.service.users().labels().list(userId='me').execute()  # type: ignore
            for lbl in labels.get('labels', []):
                if lbl['name'] == label_name:
                    return lbl['id']
            
            # Create new label
            label = {
                'name': label_name,
                'labelListVisibility': 'labelShow',
                'messageListVisibility': 'show',
                'color': self._get_label_color(label_name)
            }
            created_label = self.service.users().labels().create(  # type: ignore
                userId='me', body=label).execute()
            return created_label['id']
        except HttpError as error:
            print(f"Label error: {error}")
            return None
    
    def _get_label_color(self, label_name: str) -> Dict[str, str]:
        '''Get color for label based on category'''
        for category, color in LABEL_COLORS.items():
            if category in label_name:
                return color
        return {'backgroundColor': '#cccccc', 'textColor': '#000000'}
    
    def apply_label(self, email_id: str, label_id: str) -> bool:
        '''Apply label to email'''
        try:
            self.service.users().messages().modify(  # type: ignore
                userId='me',
                id=email_id,
                body={'addLabelIds': [label_id]}
            ).execute()
            return True
        except HttpError as error:
            print(f"Error applying label: {error}")
            return False
    
    def remove_category_labels(self) -> int:
        '''Remove all category labels'''
        try:
            labels = self.service.users().labels().list(userId='me').execute()  # type: ignore
            removed = 0
            for label in labels.get('labels', []):
                if label['name'].startswith('📧 '):
                    self.service.users().labels().delete(  # type: ignore
                        userId='me', id=label['id']).execute()
                    removed += 1
            return removed
        except Exception as e:
            print(f"Error removing labels: {e}")
            return 0