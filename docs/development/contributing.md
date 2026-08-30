# Contributing

Contributions to NLP-Mailer are welcome.

Before submitting a change, make sure that the implementation, documentation and configuration remain consistent.

---

## Development Workflow

A typical workflow is:

```text
Create branch
     │
     ▼
Implement change
     │
     ▼
Test locally
     │
     ▼
Update documentation
     │
     ▼
Build documentation
     │
     ▼
Commit changes
     │
     ▼
Open Pull Request
```

---

## Branches

Use descriptive branch names.

Examples:

```text
feature/add-category
feature/improve-classifier
fix/gmail-authentication
docs/update-installation
refactor/gmail-connector
```

---

## Commits

Keep commits focused and descriptive.

Examples:

```text
feat: add new email category
fix: handle expired gmail token
docs: update installation guide
refactor: simplify email categorizer
```

---

## Pull Requests

A pull request should include:

- a clear description;
- a focused set of changes;
- tests where appropriate;
- updated documentation;
- no credentials or authentication tokens.

---

## Security

Never commit:

```text
credentials.json
token.json
email_model.pkl
```

unless a generated artifact is explicitly required by the project configuration.

OAuth credentials and tokens must never be included in pull requests.

---

## Documentation Changes

If a change affects user-visible behavior, update the appropriate documentation section.

For example:

| Change                   | Documentation                   |
| ------------------------ | ------------------------------- |
| New CLI command          | Guide → Commands                |
| New configuration option | Getting Started → Configuration |
| ML change                | Guide → Machine Learning        |
| New class                | API Reference                   |
| Architecture change      | Architecture                    |
| Authentication change    | Gmail Setup                     |
