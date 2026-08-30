# Application Flow

This page describes how NLP-Mailer processes an email from startup to label assignment.

---

## Startup

The application starts from:

```text
main.py
```

The CLI and application services are initialized.

---

## Initialization

The application initializes:

```text
CLI
 │
 ├── GmailSubjectTagger
 │      ├── GmailConnector
 │      └── EmailCategorizer
 │
 └── Configuration
```

The categorizer checks whether a persisted model is available.

---

## Model Initialization

```text
email_model.pkl exists?
        │
   ┌────┴────┐
  yes       no
   │          │
   ▼          ▼
Load model  Train model
   │          │
   └────┬─────┘
        ▼
   Ready to classify
```

---

## Gmail Authentication

The Gmail connector loads the OAuth token if available.

If authentication is required, the OAuth flow is started.

Once authenticated, the Gmail API client becomes available.

---

## Email Processing

When a tagging command is executed:

```text
CLI command
    │
    ▼
GmailSubjectTagger
    │
    ▼
GmailConnector
    │
    ▼
Retrieve messages
```

---

## Classification

Each email is passed to the categorizer:

```text
Subject + Body
      │
      ▼
Preprocessing
      │
      ▼
TF-IDF
      │
      ▼
Naive Bayes
      │
      ▼
Prediction + Probability
```

---

## Confidence Evaluation

The predicted probability is compared with the configured threshold.

```text
confidence >= MIN_CONFIDENCE
```

If the condition is true, the prediction is accepted.

Otherwise, the email is skipped.

---

## Label Assignment

Accepted messages are associated with a category label.

If the label does not exist, it is created.

The label is then applied to the Gmail message.

---

## Preview Mode

`preview` follows the same classification process but stops before modifying Gmail.

```text
Retrieve
   │
   ▼
Classify
   │
   ▼
Calculate confidence
   │
   ▼
Display result
   │
   X
No Gmail modification
```

This makes preview mode safe for testing.
