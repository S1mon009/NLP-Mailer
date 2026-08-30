# Documentation

NLP-Mailer documentation is generated using MkDocs and Material for MkDocs.

API documentation is generated from Python docstrings using mkdocstrings.

---

## Documentation Structure

```text
docs/
├── index.md
├── getting-started/
├── guide/
├── architecture/
├── api/
├── development/
└── reference/
```

Each section has a specific purpose:

| Section         | Purpose                        |
| --------------- | ------------------------------ |
| Getting Started | Installation and initial setup |
| Guide           | Application usage              |
| Architecture    | Internal design                |
| API             | Python API                     |
| Development     | Contributor information        |
| Reference       | FAQ and troubleshooting        |

---

## Running MkDocs

Start the local development server:

```bash
mkdocs serve
```

Build the documentation:

```bash
mkdocs build
```

Validate strictly:

```bash
mkdocs build --strict
```

---

## Writing API Documentation

Public Python classes and methods should have clear docstrings.

The project uses Google-style docstrings.

Example:

```python
def predict(self, subject: str, body: str):
    """Predict an email category.

    Args:
        subject: Email subject.
        body: Email body.

    Returns:
        Predicted category and confidence.
    """
```

---

## Updating Documentation

Documentation should be updated whenever:

- a command changes;
- a configuration option changes;
- the ML pipeline changes;
- Gmail behavior changes;
- a public API changes;
- installation requirements change.

---

## Documentation Quality

Documentation should be:

- concise;
- technically accurate;
- written in clear English;
- consistent with the implementation;
- easy to navigate;
- free from unnecessary duplication.

Avoid documenting behavior that does not exist in the current implementation.
