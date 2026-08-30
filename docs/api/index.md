# API Reference

The API Reference documents the public Python components used by NLP-Mailer.

The documentation is generated from Python docstrings using **mkdocstrings**.

---

## Components

### CLI

Provides the interactive command-line interface.

[CLI API](cli.md)

### Gmail Connector

Provides Gmail API communication and authentication.

[Gmail Connector API](gmail-connector.md)

### Email Categorizer

Provides machine learning training, prediction and model persistence.

[Email Categorizer API](email-categorizer.md)

### Gmail Subject Tagger

Coordinates Gmail retrieval, classification and label management.

[Gmail Subject Tagger API](gmail-subject-tagger.md)

### Configuration

Contains application-wide configuration constants and utilities.

[Configuration API](configuration.md)

---

## Documentation Generation

API pages use the `mkdocstrings` plugin.

Example:

```markdown
::: src.services.email_categorizer.EmailCategorizer
```

This means API documentation is generated directly from the Python source code.

When a class or method changes, its docstring can be updated without manually duplicating the API description in Markdown.
