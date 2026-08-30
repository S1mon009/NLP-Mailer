# Machine Learning

NLP-Mailer uses a lightweight supervised machine learning pipeline for email classification.

The implementation is based on scikit-learn and is designed to run efficiently on a regular CPU.

---

## Machine Learning Pipeline

```text
Email Subject + Body
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
 Category Probability
          │
          ▼
 Confidence Evaluation
```

---

## Training Dataset

The classifier is trained using the configured Hugging Face email classification dataset.

The dataset contains examples assigned to different email categories.

During preparation, invalid or unsupported records are filtered out.

---

## TF-IDF

TF-IDF stands for **Term Frequency–Inverse Document Frequency**.

It transforms text into numerical features based on how important a word is within a document and across the complete training dataset.

NLP-Mailer currently limits the feature vocabulary to a fixed number of features.

It also uses English stop-word filtering.

---

## Multinomial Naive Bayes

The classifier used by the application is:

```python
MultinomialNB()
```

Multinomial Naive Bayes is a common choice for text classification because it is:

- lightweight;
- fast to train;
- fast during prediction;
- suitable for high-dimensional text data;
- suitable for CPU-based execution.

---

## Training

The model is trained when no serialized model is available.

The training process is conceptually:

```text
Dataset
   │
   ▼
Validate records
   │
   ▼
Prepare text
   │
   ▼
Fit TF-IDF
   │
   ▼
Train MultinomialNB
   │
   ▼
Save Pipeline
```

---

## Model Persistence

The complete scikit-learn pipeline is saved to:

```text
src/models/email_model.pkl
```

This includes both:

- the TF-IDF vectorizer;
- the trained classifier.

Because both components are stored together, the same feature transformation used during training is reused during prediction.

---

## Model Loading

On startup, NLP-Mailer checks whether the model file exists.

If it does, the existing pipeline is loaded.

This avoids unnecessary retraining.

---

## Retraining

To force a new training run, remove:

```text
src/models/email_model.pkl
```

and start the application again.

The application will detect that the model is missing and train a new pipeline.

---

## Limitations

The current model has several inherent limitations:

- classification quality depends on the training dataset;
- probabilities are not necessarily perfectly calibrated;
- categories that overlap semantically can be difficult to distinguish;
- unusual or previously unseen email formats may produce low-confidence predictions;
- the model is primarily designed for English text.

The confidence threshold should therefore be treated as a safety mechanism rather than a guarantee of correctness.
