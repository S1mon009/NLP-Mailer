# NLP-Mailer

**NLP-Mailer** is a Python-based command-line application that automatically categorizes Gmail messages using natural language processing and machine learning.

The application connects to Gmail through the Gmail API, analyzes email content, predicts the most appropriate category, and applies a corresponding Gmail label.

NLP-Mailer is designed to provide a lightweight, local and configurable solution for automatic email organization without requiring an external AI service.

---

## Why NLP-Mailer?

Managing a large inbox manually can become repetitive and time-consuming. Traditional Gmail filters are useful for rule-based organization, but they require users to define explicit rules for every type of message.

NLP-Mailer takes a different approach.

Instead of relying exclusively on predefined rules, it uses a machine learning model trained on categorized email data. The model analyzes the content of an email and estimates which category best describes the message.

The application can therefore recognize patterns in email text without requiring a separate Gmail filter for every situation.

---

## Key Features

- **Automatic email categorization** using machine learning.
- **Gmail API integration** for reading and labeling messages.
- **OAuth 2.0 authentication** for secure Gmail access.
- **TF-IDF text vectorization** for converting email text into numerical features.
- **Multinomial Naive Bayes classification** for category prediction.
- **Confidence-based filtering** to prevent low-confidence predictions from being applied.
- **Local model persistence** using a serialized scikit-learn pipeline.
- **Interactive CLI** for controlling the application.
- **Preview mode** for testing predictions without modifying Gmail.
- **Custom confidence threshold** configuration.
- **Automatic Gmail label creation**.
- **Local dataset caching** to avoid unnecessary downloads.

---

## How It Works

The application processes an email through several stages:

```text
                    Gmail
                      │
                      ▼
              Gmail Connector
                      │
                      ▼
              Email Extraction
                      │
                      ▼
             Text Preprocessing
                      │
                      ▼
                  TF-IDF
                      │
                      ▼
             Multinomial Naive Bayes
                      │
                      ▼
             Category Prediction
                      │
                      ▼
             Confidence Evaluation
                      │
              ┌───────┴───────┐
              │               │
           Accepted          Rejected
              │               │
              ▼               ▼
        Gmail Label          Skip
```

The model combines the email subject and body before classification. The subject is intentionally given additional weight because it often contains strong signals about the purpose of an email.

---

## Technology Stack

| Component            | Technology              |
| -------------------- | ----------------------- |
| Programming language | Python                  |
| Machine learning     | scikit-learn            |
| NLP                  | NLTK                    |
| Feature extraction   | TF-IDF                  |
| Classifier           | Multinomial Naive Bayes |
| Email provider       | Gmail                   |
| API                  | Gmail API               |
| Authentication       | OAuth 2.0               |
| Dataset              | Hugging Face Datasets   |
| Documentation        | MkDocs                  |
| Documentation theme  | Material for MkDocs     |
| API documentation    | mkdocstrings            |

---

## Project Goals

NLP-Mailer focuses on three main goals:

### Automation

Reduce the amount of manual work required to organize an inbox.

### Simplicity

Provide a lightweight application that can be executed locally without requiring a dedicated AI infrastructure.

### Extensibility

Keep Gmail integration, machine learning and application logic separated so that individual components can be extended independently.

---

## Documentation

Use the following sections to learn more about NLP-Mailer:

- [Getting Started](getting-started/installation.md) — install and configure the application.
- [Guide](guide/commands.md) — learn how to use the CLI.
- [Architecture](architecture/overview.md) — understand how the application is structured.
- [API Reference](api/index.md) — explore the Python API.
- [Development](development/local-development.md) — contribute to the project.
- [Reference](reference/faq.md) — find answers to common questions and problems.

---

## License

See the [Legal](reference/legal.md) section for information about project licensing, Gmail API usage and responsibilities related to automated email processing.
