# Gmail Labels

NLP-Mailer organizes categorized messages using Gmail labels.

The application creates a dedicated label for each supported category.

---

## Label Naming

Labels use the following format:

```text
📧 <Category>
```

Examples:

```text
📧 Business
📧 Finance & Bills
📧 Personal
📧 Promotions
```

The prefix makes application-generated labels easy to distinguish from other Gmail labels.

---

## Label Creation

When a category is encountered, NLP-Mailer checks whether the corresponding Gmail label already exists.

If it does not exist, the application creates it.

Existing labels are reused.

This prevents duplicate labels from being created during subsequent executions.

---

## Label Colors

Category labels can be assigned colors through the `LABEL_COLORS` configuration.

The color mapping is defined centrally in the configuration module.

---

## Applying Labels

After a successful classification:

```text
Email
  │
  ▼
Prediction
  │
  ▼
Confidence check
  │
  ▼
Category label
  │
  ▼
Gmail message
```

The category label is added to the corresponding Gmail message.

---

## Removing Labels

All application category labels can be removed using:

```text
clear
```

The application requests confirmation before performing the operation.

---

## Important Note

NLP-Mailer primarily organizes messages using Gmail labels.

It does not need to modify the original email content in order to categorize a message.
