# First Run

After installing NLP-Mailer and configuring Gmail API credentials, the application can be started with:

```bash
python main.py
```

---

## Initialization

During startup, NLP-Mailer initializes the main application components.

The initialization process includes:

1. loading configuration;
2. initializing the machine learning categorizer;
3. checking for an existing trained model;
4. training the model if necessary;
5. initializing the Gmail connector;
6. authenticating with Gmail;
7. starting the interactive CLI.

---

## Model Initialization

The application first checks whether:

```text
src/models/email_model.pkl
```

exists.

If the model exists, it is loaded.

If it does not exist, NLP-Mailer loads the training dataset and trains a new model.

The trained pipeline is then saved locally.

---

## First Gmail Authentication

On the first run, Google authentication is required.

A browser window is opened and the user is asked to grant the required Gmail permissions.

After successful authentication, the application stores the authorization token locally.

---

## Preview Before Tagging

Before modifying Gmail, it is recommended to test the classifier using:

```text
preview 10
```

This allows you to inspect predictions without applying labels.

---

## Test Classification

You can also test a single message using:

```text
test
```

The application asks for an email subject and optionally its body.

This is useful for evaluating the classifier before processing real messages.

---

## First Tagging Run

Once the results look correct, run:

```text
tag 20
```

This processes up to 20 recent messages.

For larger inboxes, increase the number gradually rather than processing a very large number of messages immediately.

---

## Recommended First-Run Workflow

```text
Install
   │
   ▼
Configure Gmail API
   │
   ▼
Start NLP-Mailer
   │
   ▼
Authenticate
   │
   ▼
Train / Load Model
   │
   ▼
test
   │
   ▼
preview 10
   │
   ▼
Adjust confidence
   │
   ▼
tag 20
```
