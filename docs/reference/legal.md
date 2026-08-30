# Legal and Privacy

NLP-Mailer interacts with Gmail and processes email content. Users are responsible for ensuring that their use of the application complies with applicable laws, regulations and service terms.

---

## Gmail API

NLP-Mailer uses the Gmail API to access and modify messages.

Users should review Google's current Gmail API terms, OAuth requirements and applicable Google policies before deploying the application.

---

## Email Data

Email messages can contain sensitive or confidential information.

Although NLP-Mailer is designed to perform classification locally, users are responsible for securing:

```text
credentials.json
token.json
email_model.pkl
dataset cache
```

and any logs or files that may contain email-related information.

---

## Authentication Credentials

OAuth credentials and tokens must not be shared publicly.

Do not commit:

```text
credentials.json
token.json
```

to source control.

If credentials are exposed, revoke them and create new credentials.

---

## Automated Classification

Machine learning predictions are probabilistic.

A high confidence score does not guarantee that a classification is correct.

Users should therefore review the behavior of NLP-Mailer before relying on automatic categorization for important communications.

---

## No Guarantee of Accuracy

NLP-Mailer does not guarantee:

- correct email categorization;
- complete email processing;
- uninterrupted Gmail API access;
- compatibility with all future Gmail API changes;
- compatibility with all versions of Python or scikit-learn.

---

## User Responsibility

The user is responsible for:

- configuring OAuth permissions appropriately;
- protecting authentication credentials;
- reviewing automatically generated labels;
- ensuring compliance with applicable privacy requirements;
- maintaining backups of important information.

---

## Third-Party Services

NLP-Mailer depends on third-party services and libraries, including Gmail API and Hugging Face datasets.

Their terms, availability and behavior may change independently of this project.
