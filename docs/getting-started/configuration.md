# Configuration

NLP-Mailer stores its application configuration in:

```text
src/config/config.py
```

The configuration module defines paths, Gmail permissions, categories, dataset settings and the default classification confidence threshold.

---

## Model Configuration

### `MODEL_PATH`

Defines where the trained machine learning model is stored.

```python
MODEL_PATH = "src/models/email_model.pkl"
```

The file contains the serialized scikit-learn pipeline.

If the file exists, NLP-Mailer loads the existing model instead of training a new one.

---

## Confidence Configuration

### `MIN_CONFIDENCE`

Defines the minimum confidence required for an email to be automatically categorized.

```python
MIN_CONFIDENCE = 0.6
```

The value must be between `0.0` and `1.0`.

For example:

```text
0.90  → very conservative
0.75  → conservative
0.60  → default
0.50  → more aggressive
```

A higher value reduces the number of potentially incorrect labels but also increases the number of messages that remain unclassified.

---

## Gmail Configuration

### `GMAIL_CREDENTIALS_FILE`

Defines the OAuth client credentials file:

```python
GMAIL_CREDENTIALS_FILE = "credentials.json"
```

### `GMAIL_TOKEN_FILE`

Defines the location of the locally stored OAuth token:

```python
GMAIL_TOKEN_FILE = "token.json"
```

### `GMAIL_SCOPES`

NLP-Mailer uses the Gmail modification scope:

```text
https://www.googleapis.com/auth/gmail.modify
```

This permission allows the application to read messages and modify their labels.

---

## Categories

The application uses predefined categories to classify messages.

The categories currently supported by the project are:

- Business
- Reminders
- Events & Invitations
- Finance & Bills
- Travel & Bookings
- Customer Support
- Personal
- Newsletters
- Job Application
- Promotions

The category definitions are stored in the configuration module.

---

## Dataset Configuration

Training data is obtained from the configured Hugging Face dataset and cached locally.

The local cache prevents the application from downloading the same dataset every time the model is trained.

---

## Security

Never commit the following files to Git:

```text
credentials.json
token.json
```

These files contain authentication information and should be treated as secrets.

A recommended `.gitignore` configuration is:

```text
credentials.json
token.json
*.pkl
.venv/
```

---

## Configuration Reference

For the complete list of configuration constants and functions, see the [Configuration API](../api/configuration.md).
