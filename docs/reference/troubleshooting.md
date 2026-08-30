# Troubleshooting

This page describes common problems and possible solutions.

---

## Gmail Authentication Failed

### Symptoms

The application cannot authenticate with Gmail.

### Solutions

Verify that:

1. `credentials.json` exists;
2. Gmail API is enabled;
3. the Gmail account is authorized;
4. the OAuth consent configuration is correct.

If the token is invalid, remove:

```text
token.json
```

and authenticate again.

---

## Gmail API Permission Error

Verify that the application has:

```text
https://www.googleapis.com/auth/gmail.modify
```

If permissions have changed, remove `token.json` and repeat authentication.

---

## Model Training Takes a Long Time

The first run can take longer because the application may need to:

1. download the dataset;
2. prepare the data;
3. train the classifier;
4. serialize the model.

Once:

```text
src/models/email_model.pkl
```

exists, subsequent launches can load the saved model instead.

---

## Model File Is Missing

If the model is missing, restart the application.

NLP-Mailer should detect the missing model and train a new one.

---

## Dataset Download Failed

Check:

- internet connectivity;
- access to the Hugging Face dataset;
- permissions for the local dataset directory;
- available disk space.

---

## Predictions Are Poor

Possible causes include:

- insufficient training data;
- ambiguous categories;
- emails that differ significantly from training examples;
- inappropriate confidence threshold;
- language mismatch.

Use:

```text
test
```

to inspect individual predictions.

Then use:

```text
preview 20
```

to evaluate predictions on real messages.

---

## Too Many Emails Are Skipped

The confidence threshold may be too high.

Try:

```text
confidence
```

and temporarily use a lower value such as:

```text
0.5
```

Then run:

```text
preview 20
```

---

## Too Many Incorrect Labels

The confidence threshold may be too low.

Increase it:

```text
confidence
```

For example:

```text
0.8
```

Then evaluate the results using:

```text
preview 20
```

---

## Labels Are Not Created

Check that the Gmail OAuth scope includes:

```text
gmail.modify
```

Then authenticate again if necessary.

---

## Documentation Build Fails

Run:

```bash
mkdocs build --strict
```

The command will provide the exact warning or error that prevents a clean build.

Common causes include:

- invalid Markdown;
- missing pages;
- incorrect navigation paths;
- broken API references;
- missing MkDocs plugins.
