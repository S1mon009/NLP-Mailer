"""
Gmail API connector for email retrieval and label management.

This module provides the GmailConnector class, which handles
authentication with the Gmail API and provides operations for retrieving
emails, parsing message data, creating and applying labels, and removing
application-specific category labels.

The connector uses OAuth 2.0 authentication and stores the authorization
token locally for subsequent sessions. Gmail labels are automatically
assigned colors based on the application's category configuration.
"""
import os.path
import base64
from typing import Optional, List, Dict, Any
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.config.config import GMAIL_CREDENTIALS_FILE, GMAIL_TOKEN_FILE, GMAIL_SCOPES, LABEL_COLORS


class GmailConnector:
    """
    Handle authentication and operations with the Gmail API.

    The connector manages the Gmail API service, authenticates the user
    using OAuth 2.0, retrieves and parses email messages, and manages
    Gmail labels used by the application.

    Attributes:
        credentials_file (str): Path to the Gmail OAuth client credentials
            file.
        token_file (str): Path to the locally stored OAuth authorization
            token.
        service (Optional[Any]): Authenticated Gmail API service instance.
            Set to ``None`` until authentication is completed successfully.
    """
    def __init__(self) -> None:
        """
        Initialize the Gmail API connector. 
        Loads the configured credentials and token file paths and initializes the Gmail API service as ``None``. Authentication must be performed using `authenticate` before API operations can be executed. 
        """
        self.credentials_file = GMAIL_CREDENTIALS_FILE
        self.token_file = GMAIL_TOKEN_FILE
        self.service: Optional[Any] = None

    def authenticate(self) -> bool:
        """
        Authenticate the application with the Gmail API. 
        
        Attempts to authenticate using a previously stored OAuth token. If the token has expired and contains a refresh token, it is refreshed automatically. If no valid token is available, the method starts the OAuth 2.0 authorization flow using the configured credentials file. 
        
        After successful authentication, the credentials are saved to the configured token file and an authenticated Gmail API service is created. 
        
        Returns: 
            bool: ``True`` if authentication succeeds, otherwise ``False``. 
        
        Notes: 
            The Gmail OAuth credentials file must exist at `credentials_file` when authentication is performed for the first time. """
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
        """
        Retrieve emails from the authenticated Gmail account.
        
        Fetches messages matching the specified Gmail search query and parses each message into a dictionary containing its metadata and email body. 
        
        Args: 
            max_results (int): Maximum number of emails to retrieve. Defaults to ``50``. 
            query (str): Gmail search query used to filter messages. An empty string retrieves messages without an additional search filter. 
        
        Returns: 
            List[Dict[str, Any]]: A list of parsed email dictionaries. Each dictionary contains the message ID, thread ID, subject, sender, date, body, and Gmail label IDs. 
            
            Returns an empty list if a Gmail API error occurs. """
        try:
            # pylint: disable=no-member 
            results = self.service.users().messages().list(  # type: ignore
                userId='me', maxResults=max_results, q=query).execute()
            # pylint: enable=no-member
            messages = results.get('messages', [])

            emails = []
            for msg in messages:
                # pylint: disable=no-member 
                email_data = self.service.users().messages().get(
                    userId='me', id=msg['id'], format='full').execute()
                # pylint: enable=no-member

                email = self._parse_email(email_data)
                emails.append(email)

            return emails
        except HttpError as error:
            print(f"Error fetching emails: {error}")
            return []

    def _parse_email(self, email_data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse a Gmail API message into a simplified email dictionary. 
        
        Extracts common email metadata such as the subject, sender, and date from the Gmail message headers. The email body is extracted using :meth:`_get_email_body`. 
        
        Args: 
            email_data (Dict[str, Any]): Raw email message data returned by the Gmail API. 
        
        Returns: 
            Dict[str, Any]: Parsed email data containing: 
            - **``id``**: Unique Gmail message ID. 
            - **``threadId``**: Gmail conversation thread ID. 
            - **``subject``**: Email subject. 
            - **``sender``**: Email sender. 
            - **``date``**: Email date. 
            - **``body``**: Extracted email body. 
            - **``labels``**: List of Gmail label IDs. 
        """
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
        """
        Extract the plain-text body from a Gmail message payload. 
        
        Searches the message payload for a ``text/plain`` part and decodes its Base64URL-encoded content. For messages without separate parts, the method attempts to decode the body directly. 
        
        The returned body is limited to the first 500 characters to prevent excessively large message contents from being processed. 
        
        Args: 
            payload (Dict[str, Any]): Gmail API message payload containing the email body and its MIME parts. 
        Returns: 
            str: Decoded plain-text email body, truncated to 500 characters. Returns an empty string if no decodable body is found. 
        """
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
        """
        Create a Gmail label if it does not already exist.

        The method first checks whether a label with the specified name
        already exists. If found, its ID is returned. Otherwise, a new
        label is created with visibility settings and a color determined
        by the label category.

        Args:
            label_name: Name of the Gmail label to create.

        Returns:
            The Gmail label ID if the label exists or was successfully
            created, otherwise ``None``.

        Raises:
            HttpError: Handled internally when the Gmail API request fails.
                The error is logged and ``None`` is returned.
        """
        try:
            # pylint: disable=no-member 
            labels = self.service.users().labels().list(userId='me').execute()
            # pylint: enable=no-member
            for lbl in labels.get('labels', []):
                if lbl['name'] == label_name:
                    return lbl['id']

            label = {
                'name': label_name,
                'labelListVisibility': 'labelShow',
                'messageListVisibility': 'show',
                'color': self._get_label_color(label_name)
            }
            # pylint: disable=no-member 
            created_label = self.service.users().labels().create(
                userId='me', body=label).execute()
            # pylint: enable=no-member
            return created_label['id']
        except HttpError as error:
            print(f"Label error: {error}")
            return None

    def _get_label_color(self, label_name: str) -> Dict[str, str]:
        """
        Get the color configuration for a Gmail label.

        The color is selected based on whether a configured category name
        occurs in the label name. If no matching category is found, a
        default gray color configuration is returned.

        Args:
            label_name: Name of the Gmail label for which the color
                should be determined.

        Returns:
            A dictionary containing the Gmail label color configuration
            with ``backgroundColor`` and ``textColor`` keys.
        """
        for category, color in LABEL_COLORS.items():
            if category in label_name:
                return color
        return {'backgroundColor': '#cccccc', 'textColor': '#000000'}

    def apply_label(self, email_id: str, label_id: str) -> bool:
        """
        Apply a Gmail label to an email.

        Uses the Gmail API to add the specified label to the given
        message.

        Args:
            email_id: ID of the Gmail message to which the label should
                be applied.
            label_id: ID of the Gmail label to apply.

        Returns:
            ``True`` if the label was successfully applied, otherwise
            ``False``.

        Raises:
            HttpError: Handled internally when the Gmail API request fails.
                The error is logged and ``False`` is returned.
        """
        try:
            # pylint: disable=no-member
            self.service.users().messages().modify(
                userId='me',
                id=email_id,
                body={'addLabelIds': [label_id]}
            ).execute()
            # pylint: enable=no-member
            return True
        except HttpError as error:
            print(f"Error applying label: {error}")
            return False

    def remove_category_labels(self) -> int:
        """
        Remove all category labels from the Gmail account.

        Searches for all Gmail labels and deletes those whose names start
        with the ``📧 `` prefix. This is intended to remove labels created
        for email categorization while leaving unrelated Gmail labels
        untouched.
s
        Returns:
            The number of category labels successfully removed.
            Returns ``0`` if an error occurs while retrieving or deleting
            labels.
        """
        try:
            # pylint: disable=no-member
            labels = self.service.users().labels().list(userId='me').execute()
            # pylint: enable=no-member
            removed = 0
            for label in labels.get('labels', []):
                if label['name'].startswith('📧 '):
                    # pylint: disable=no-member 
                    self.service.users().labels().delete(
                        userId='me', id=label['id']).execute()
                    # pylint: enable=no-member
                    removed += 1
            return removed
        except Exception as e:
            print(f"Error removing labels: {e}")
            return 0
