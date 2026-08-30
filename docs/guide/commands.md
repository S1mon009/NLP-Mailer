# Commands

NLP-Mailer provides an interactive command-line interface.

Start the application with:

```bash
python main.py
```

After initialization, the CLI accepts commands for processing and managing email messages.

---

## `tag`

Processes recent emails and applies the predicted category label.

```text
tag
```

The command accepts an optional number:

```text
tag 50
```

This requests processing of up to 50 messages.

---

## `preview`

Displays predictions without modifying Gmail.

```text
preview
```

You can specify the number of messages:

```text
preview 25
```

`preview` is the recommended command for testing classification results.

!!! tip

```
Always use `preview` before processing a large number of messages.
```

---

## `unread`

Processes unread messages.

```text
unread
```

The underlying Gmail search is:

```text
is:unread
```

---

## `today`

Processes messages received recently.

```text
today
```

The command uses:

```text
newer_than:1d
```

---

## `week`

Processes messages from the last seven days.

```text
week
```

The corresponding Gmail query is:

```text
newer_than:7d
```

---

## `test`

Tests the classifier with manually entered content.

```text
test
```

The application requests:

```text
Subject:
Body (optional):
```

The result contains the predicted category and confidence.

---

## `confidence`

Changes the confidence threshold interactively.

```text
confidence
```

For example:

```text
Enter confidence threshold (0.0-1.0): 0.8
```

A higher threshold makes automatic classification more conservative.

---

## `clear`

Removes the category labels created by NLP-Mailer.

```text
clear
```

The application asks for confirmation before removing labels.

!!! warning

```
Use this command carefully because it removes the application's category labels from Gmail.
```

---

## `quit`

Terminates the application.

```text
quit
```

---

## Command Summary

| Command       | Description                       |
| ------------- | --------------------------------- |
| `tag [N]`     | Tag recent emails                 |
| `preview [N]` | Preview predictions               |
| `unread`      | Process unread emails             |
| `today`       | Process recent emails             |
| `week`        | Process emails from the last week |
| `test`        | Test classification manually      |
| `confidence`  | Change confidence threshold       |
| `clear`       | Remove category labels            |
| `quit`        | Exit the application              |
