# Testing

Testing is an important part of maintaining NLP-Mailer as the project grows.

---

## Manual Testing

The application provides several commands that can be used for manual validation.

### Test the classifier

```text
test
```

### Preview real Gmail messages

```text
preview 10
```

### Test unread messages

```text
unread
```

These commands make it possible to validate functionality without immediately processing the entire inbox.

---

## Safe Testing Workflow

A recommended workflow is:

```text
test
  │
  ▼
preview 10
  │
  ▼
Review predictions
  │
  ▼
Adjust threshold
  │
  ▼
preview 50
  │
  ▼
tag
```

---

## Testing Gmail Integration

Gmail integration should be tested carefully because successful operations can modify the user's mailbox.

Use preview operations whenever possible.

Avoid running large tagging operations against a production inbox while developing new functionality.

---

## Testing Documentation

Validate the documentation build using:

```bash
mkdocs build --strict
```

This catches broken references, invalid configuration and documentation warnings.

---

## Future Automated Testing

As the project grows, automated tests should cover:

- text preprocessing;
- category prediction;
- confidence handling;
- configuration;
- Gmail response parsing;
- label management;
- CLI command parsing.

External Gmail API calls should ideally be mocked during automated tests.
