# FAQ

## Does NLP-Mailer require a GPU?

No.

The application uses a lightweight scikit-learn model and can run on a regular CPU.

---

## Does NLP-Mailer use ChatGPT or another LLM?

No.

The current implementation uses traditional machine learning with TF-IDF and Multinomial Naive Bayes.

---

## Are emails sent to an external AI service?

The classification pipeline itself does not require an external LLM API.

Email data is retrieved from Gmail and processed by the local application.

---

## Where is the trained model stored?

By default:

```text
src/models/email_model.pkl
```

---

## Where is Gmail authentication stored?

The OAuth token is stored locally in:

```text
token.json
```

The OAuth client credentials are stored in:

```text
credentials.json
```

---

## Can I change the confidence threshold?

Yes.

Run:

```text
confidence
```

and enter a value between `0.0` and `1.0`.

---

## Can I preview classifications before applying labels?

Yes.

Use:

```text
preview 20
```

Preview mode does not apply the predicted labels.

---

## How do I retrain the model?

Delete:

```text
src/models/email_model.pkl
```

and restart the application.

---

## Can I add another email category?

Yes.

A new category needs to be added to the category configuration and supported by the training data.

See the development documentation for more information.

---

## Does NLP-Mailer modify the original email?

The primary categorization mechanism is Gmail labels.

The application does not need to rewrite the actual message body to classify an email.

---

## Why was an email skipped?

The most common reasons are:

- confidence was below the configured threshold;
- the message was already categorized;
- the message did not contain enough useful text.

Use `preview` to inspect the prediction and confidence.

---

## Can I use multiple Gmail accounts?

The application is designed around a locally authenticated Gmail account.

To use another account, the corresponding OAuth authentication needs to be performed for that account.
