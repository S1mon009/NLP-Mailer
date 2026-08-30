# Confidence

Classification confidence determines whether NLP-Mailer should trust a model prediction enough to apply a Gmail label.

---

## How Confidence Is Calculated

The classifier produces a probability for each supported category.

For example:

```text
Business           0.10
Finance & Bills    0.04
Personal           0.02
Promotions         0.84
```

The highest probability is selected:

```text
Prediction: Promotions
Confidence: 0.84
```

---

## Minimum Confidence

The default minimum confidence is:

```text
0.60
```

Therefore:

```text
0.84 >= 0.60
```

The prediction is accepted.

A prediction such as:

```text
0.43 < 0.60
```

is rejected.

---

## Choosing a Threshold

There is no universally optimal threshold.

A lower threshold:

- classifies more messages;
- increases coverage;
- may produce more incorrect classifications.

A higher threshold:

- classifies fewer messages;
- reduces the number of uncertain predictions;
- may leave more messages unclassified.

---

## Recommended Values

| Threshold | Behavior               |
| --------: | ---------------------- |
|    `0.40` | Aggressive             |
|    `0.50` | Moderately aggressive  |
|    `0.60` | Default                |
|    `0.70` | Conservative           |
|    `0.80` | Very conservative      |
|    `0.90` | Extremely conservative |

These values are guidelines rather than guarantees of model accuracy.

---

## Changing the Threshold

Run:

```text
confidence
```

Then enter a value between `0.0` and `1.0`.

Example:

```text
0.75
```

---

## Evaluating a Threshold

A good workflow is:

```text
confidence
      │
      ▼
preview 50
      │
      ▼
Review predictions
      │
      ▼
Adjust threshold
      │
      ▼
preview again
```

This makes it possible to find a balance between coverage and classification quality.
