# Configuration

The project configuration is defined in `src/config/config.py`.

## Main settings

### Gmail settings

- `GMAIL_CREDENTIALS_FILE`
- `GMAIL_TOKEN_FILE`
- `GMAIL_SCOPES`

These settings control the Gmail API authentication and required access scope.

### Model settings

- `MODEL_PATH`
- `MIN_CONFIDENCE`

The model file is saved locally and the minimum confidence threshold is used during categorization.

### Dataset settings

- `DATASET_NAME`
- `DATASET_LOCAL_PATH`

The project downloads the public dataset from Hugging Face and stores the local cache under the `src/datasets` folder.

## Category configuration

The available labels come from the dataset and are stored as `CATEGORIES`.

Example categories:

- Business
- Reminders
- Events & Invitations
- Finance & Bills
- Travel & Bookings
- Customer Support
- Personal
- Newsletters
- Job Application
- Promotions

## Label colors

The project also defines Gmail label colors in `LABEL_COLORS`, so each category receives a dedicated visual style in the inbox.

## Confidence threshold

The minimum confidence is used to decide whether a classification is reliable enough to be applied to an email.

If the confidence is too low, the email is skipped instead of labeled.
