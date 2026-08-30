# Project Structure

The source code is organized into separate packages according to responsibility.

```text
src/
├── cli/
│   └── cli.py
│
├── config/
│   └── config.py
│
├── datasets/
│   └── ...
│
├── integrations/
│   └── gmail_connector.py
│
├── models/
│   └── email_model.pkl
│
└── services/
    ├── email_categorizer.py
    └── tagger.py
```

---

## `src/cli`

Contains the command-line interface.

The main class is responsible for presenting available commands and delegating operations to the application service.

---

## `src/config`

Contains centralized configuration.

This includes:

- Gmail credentials paths;
- OAuth scopes;
- model path;
- confidence threshold;
- category definitions;
- label colors;
- dataset configuration.

---

## `src/datasets`

Contains locally cached training data.

The dataset cache allows the application to reuse previously downloaded data.

---

## `src/integrations`

Contains integrations with external services.

Currently the primary integration is:

```text
GmailConnector
```

The connector isolates Gmail API functionality from the rest of the application.

---

## `src/models`

Contains persisted machine learning artifacts.

The primary artifact is:

```text
email_model.pkl
```

---

## `src/services`

Contains application and machine learning services.

### `EmailCategorizer`

Handles the machine learning pipeline.

### `GmailSubjectTagger`

Coordinates email retrieval, classification and Gmail labeling.

---

## `main.py`

The project entry point.

It initializes and starts the CLI application.

---

## Separation of Responsibilities

A simplified responsibility map is:

| Component            | Responsibility            |
| -------------------- | ------------------------- |
| `main.py`            | Application entry point   |
| `CLI`                | User interaction          |
| `GmailSubjectTagger` | Application orchestration |
| `GmailConnector`     | Gmail API                 |
| `EmailCategorizer`   | NLP and ML                |
| `config.py`          | Configuration             |
| `email_model.pkl`    | Persisted model           |
