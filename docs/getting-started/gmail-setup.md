# Gmail Setup

NLP-Mailer uses the Gmail API to retrieve messages and manage Gmail labels.

Before running the application for the first time, a Google Cloud project and OAuth credentials must be configured.

---

## 1. Create a Google Cloud Project

Open the Google Cloud Console and create a new project.

You can also use an existing project if it is not already configured for another application.

---

## 2. Enable the Gmail API

Open the API Library and enable:

```text
Gmail API
```

The application cannot communicate with Gmail until the API is enabled.

---

## 3. Configure OAuth Consent

Create an OAuth consent screen.

For personal development and testing, the application can use an external OAuth configuration with your Gmail account added as a test user when required by Google.

---

## 4. Create OAuth Credentials

Create an OAuth 2.0 Client ID for a desktop application.

Download the generated credentials file.

Rename it to:

```text
credentials.json
```

Place it in the root directory of NLP-Mailer:

```text
NLP-Mailer/
├── credentials.json
├── main.py
└── src/
```

---

## 5. Required Permission

NLP-Mailer uses:

```text
https://www.googleapis.com/auth/gmail.modify
```

This permission is required because the application needs to create and apply Gmail labels.

---

## 6. Authentication Flow

When NLP-Mailer starts, it checks whether a previously generated token exists.

```text
                  Start application
                         │
                         ▼
                  token.json exists?
                    /          \
                  yes           no
                  │              │
                  ▼              ▼
             Load token      OAuth flow
                  │              │
                  ▼              ▼
             Valid token?    Authenticate
               /    \             │
             yes     no           ▼
              │       │       Save token
              │       └──────► token.json
              │
              ▼
        Gmail API client
```

If the token is expired but contains a refresh token, the application attempts to refresh it automatically.

---

## Security Recommendations

Do not upload or commit:

```text
credentials.json
token.json
```

Do not share these files with other users.

If credentials are accidentally exposed, revoke them through Google Cloud and generate new credentials.

---

## Troubleshooting Authentication

If authentication fails:

1. verify that the Gmail API is enabled;
2. verify that the Gmail account is authorized;
3. verify that `credentials.json` exists;
4. remove `token.json`;
5. restart NLP-Mailer.

For more information, see [Troubleshooting](../reference/troubleshooting.md).
