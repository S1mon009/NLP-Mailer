# Email Categorization

NLP-Mailer uses machine learning to determine which category best matches an email.

The classification process is based on the email subject and body.

---

## Input Data

For each message, NLP-Mailer extracts:

- subject,
- body,
- sender,
- date,
- Gmail labels,
- message identifier.

The machine learning model primarily uses the subject and body.

---

## Subject Weighting

The email subject is intentionally given additional importance.

The classifier combines the text approximately as:

```text
Subject + Subject + Body
```

Repeating the subject increases the influence of subject terms during TF-IDF feature extraction.

This is useful because subjects often contain highly informative keywords.

For example:

```text
Your electricity bill is available
```

provides a stronger classification signal than a generic body containing many unrelated words.

---

## Preprocessing

Before classification, the text is normalized.

The preprocessing step includes:

- lowercasing;
- removing URLs;
- removing email addresses;
- removing non-alphabetic characters;
- normalizing whitespace.

The goal is to reduce irrelevant variations in the input text.

---

## Prediction

The processed text is passed to the machine learning pipeline.

The classifier produces probabilities for each supported category.

Example:

```text
Business           0.03
Finance & Bills    0.91
Personal           0.02
Promotions         0.04
```

The category with the highest probability becomes the prediction.

---

## Confidence

The highest predicted probability is treated as the classification confidence.

For the example above:

```text
Category: Finance & Bills
Confidence: 91%
```

The confidence is then compared with the configured threshold.

---

## Confidence Decision

```text
             Prediction
                  │
                  ▼
          Calculate confidence
                  │
                  ▼
       confidence >= threshold?
            /             \
          yes              no
           │                │
           ▼                ▼
      Apply label          Skip
```

This mechanism helps prevent uncertain predictions from automatically modifying Gmail.

---

## Existing Categories

The application currently supports categories such as:

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

---

## Skipping Already Processed Messages

NLP-Mailer checks whether a message already contains a category indicator.

This prevents repeatedly processing messages that have already been categorized.

---

## Preview Mode

Use:

```text
preview 20
```

to inspect classification results before applying labels.

This is particularly useful when changing the model or confidence threshold.
