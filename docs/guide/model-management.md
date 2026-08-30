# Model Management

NLP-Mailer stores the trained machine learning pipeline locally.

---

## Model Location

The default location is:

```text
src/models/email_model.pkl
```

---

## Loading an Existing Model

If the model file exists, NLP-Mailer loads it during initialization.

This significantly reduces startup time compared with training the model every time.

---

## Creating a New Model

If the model file does not exist, the application:

1. loads the dataset;
2. prepares the training data;
3. creates the ML pipeline;
4. trains the classifier;
5. saves the resulting pipeline.

---

## Retraining

To retrain the model:

```text
Delete:
src/models/email_model.pkl
```

Then restart the application.

---

## Why Retrain?

Retraining can be useful when:

- the training dataset changes;
- categories are modified;
- the preprocessing pipeline changes;
- the classifier configuration changes;
- the existing model becomes outdated.

---

## Model Compatibility

The model is serialized using Python's model persistence mechanism.

For reliable loading, use compatible versions of Python and scikit-learn when moving a model between environments.

A model should be regenerated if major dependency changes make the existing serialized pipeline incompatible.
