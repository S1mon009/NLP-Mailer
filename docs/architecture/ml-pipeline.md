# ML Pipeline

The NLP-Mailer machine learning pipeline converts raw email text into a predicted category.

---

## Pipeline Overview

```text
Raw Email
   │
   ▼
Subject + Body
   │
   ▼
Text Cleaning
   │
   ▼
TF-IDF Vectorization
   │
   ▼
Multinomial Naive Bayes
   │
   ▼
Class Probabilities
```

---

## Step 1 — Input Preparation

The application extracts the email subject and body.

The subject is included twice to increase its influence:

```text
subject + subject + body
```

---

## Step 2 — Text Cleaning

The input is normalized by removing irrelevant textual elements.

The process includes:

- URL removal;
- email address removal;
- non-alphabetic character removal;
- lowercase conversion;
- whitespace normalization.

---

## Step 3 — TF-IDF

The cleaned text is transformed into numerical vectors.

The vectorizer uses a limited vocabulary and English stop-word filtering.

---

## Step 4 — Classification

The generated vector is passed to:

```python
MultinomialNB()
```

The classifier produces a probability distribution over the supported categories.

---

## Step 5 — Confidence

The largest probability becomes the prediction confidence.

Example:

```text
Business          0.05
Finance & Bills   0.87
Personal          0.03
Promotions        0.05
```

Result:

```text
Category: Finance & Bills
Confidence: 87%
```

---

## Step 6 — Decision

The confidence is compared with the configured minimum.

```text
87% >= 60%
```

The message can therefore be tagged.

If the result were:

```text
42% < 60%
```

the message would be skipped.
