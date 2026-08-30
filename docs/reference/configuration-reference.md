# Configuration Reference

This page provides a quick reference for the main NLP-Mailer configuration values.

---

## Gmail

| Setting                  | Purpose                           |
| ------------------------ | --------------------------------- |
| `GMAIL_CREDENTIALS_FILE` | OAuth client credentials location |
| `GMAIL_TOKEN_FILE`       | OAuth token location              |
| `GMAIL_SCOPES`           | Gmail API permissions             |

---

## Machine Learning

| Setting          | Purpose                                |
| ---------------- | -------------------------------------- |
| `MODEL_PATH`     | Location of the serialized ML pipeline |
| `MIN_CONFIDENCE` | Minimum accepted prediction confidence |

---

## Dataset

The dataset configuration defines:

- dataset source;
- local cache;
- supported labels.

The local cache prevents unnecessary dataset downloads.

---

## Categories

The application currently works with:

```text
Business
Reminders
Events & Invitations
Finance & Bills
Travel & Bookings
Customer Support
Personal
Newsletters
Job Application
Promotions
```

---

## Label Colors

Gmail label colors are configured through:

```text
LABEL_COLORS
```

Each supported category can have its own Gmail color configuration.

---

## Recommended Defaults

For a typical installation, the following values are recommended:

```text
Model path:
src/models/email_model.pkl

Minimum confidence:
0.60

Credentials:
credentials.json

Token:
token.json
```

For a complete programmatic reference, see the [Configuration API](../api/configuration.md).
