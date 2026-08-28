# Usage

## Running the application

```bash
python main.py
```

This starts the interactive command-line interface.

## Available commands

- `tag [N]` — tag the last N emails
- `preview [N]` — preview what would be tagged without applying changes
- `unread` — process only unread emails
- `today` — process emails from today
- `week` — process emails from the past 7 days
- `test` — test the model on a custom subject and body
- `confidence` — change the confidence threshold
- `clear` — remove the labels created by the app
- `quit` — exit the tool

## Example

```text
Command: preview 10
Command: tag 20
Command: test
```

## Confidence threshold

The default confidence threshold is defined in the configuration file. Higher values mean stricter classification and fewer false positives.

## Dataset refresh

If you want to refresh the local dataset cache, you can run the dataset download script from the project root.

```bash
python src/services/download_email_dataset.py
```
