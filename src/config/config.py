"""
Configuration and training data utilities for the Gmail Subject Auto-Tagger.

This module contains the application's configuration constants, Gmail API
settings, machine learning model settings, email categories, and Gmail
label colors.

It also provides utilities for loading the email classification dataset
from Hugging Face, caching it locally, and converting the dataset into
the training data format expected by the application's machine learning
pipeline.

The main configuration areas provided by this module are:

- Gmail API credentials and authorization scopes.
- Machine learning model path and minimum classification confidence.
- Supported email categories and their corresponding Gmail label colors.
- Hugging Face dataset configuration and local cache path.
- Mapping between dataset labels and application categories.
"""
from pathlib import Path
from datasets import load_dataset, load_from_disk

# Gmail API Configuration
GMAIL_CREDENTIALS_FILE = 'credentials.json'
GMAIL_TOKEN_FILE = 'token.json'
GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

# Model Configuration
MODEL_PATH = 'src/models/email_model.pkl'
MIN_CONFIDENCE = 0.6

# Categories (must match the labels from the dataset)
DATASET_LABELS = [
    'Business',
    'Reminders',
    'Events & Invitations',
    'Finanquitce & Bills',
    'Travel & Bookings',
    'Customer Support',
    'Personal',
    'Newsletters',
    'Job Application',
    'Promotions',
]

CATEGORIES = DATASET_LABELS

LABEL_COLORS = {
    'Business': {'backgroundColor': '#4986e7', 'textColor': '#ffffff'},
    'Reminders': {'backgroundColor': '#16a765', 'textColor': '#ffffff'},
    'Events & Invitations': {'backgroundColor': '#9fc6e7', 'textColor': '#000000'},
    'Finance & Bills': {'backgroundColor': '#f691b2', 'textColor': '#ffffff'},
    'Travel & Bookings': {'backgroundColor': '#fad165', 'textColor': '#000000'},
    'Customer Support': {'backgroundColor': '#ff7537', 'textColor': '#ffffff'},
    'Personal': {'backgroundColor': '#8d6e63', 'textColor': '#ffffff'},
    'Newsletters': {'backgroundColor': '#cabdbf', 'textColor': '#000000'},
    'Job Application': {'backgroundColor': '#7e57c2', 'textColor': '#ffffff'},
    'Promotions': {'backgroundColor': '#ac2b16', 'textColor': '#ffffff'},
}

DATASET_NAME = 'imnim/multiclass-email-classification'
DATASET_LOCAL_PATH = Path(__file__).resolve().parents[1] / 'datasets' / 'hf_email_dataset'

LABEL_MAPPING = {label: label for label in DATASET_LABELS}


def load_hf_email_dataset():
    """
    Load the email classification dataset from Hugging Face.

    If a locally cached version of the dataset exists, it is loaded
    instead of downloading the dataset again. Otherwise, the dataset
    is downloaded from Hugging Face, saved to the local cache directory,
    and returned.

    Returns:
        Dataset:
            The Hugging Face training dataset containing email
            classification data.
    """
    if DATASET_LOCAL_PATH.exists():
        print(f'Loading cached dataset from {DATASET_LOCAL_PATH}')
        return load_from_disk(str(DATASET_LOCAL_PATH))

    dataset = load_dataset(DATASET_NAME, split='train')
    DATASET_LOCAL_PATH.mkdir(parents=True, exist_ok=True)
    dataset.save_to_disk(str(DATASET_LOCAL_PATH))
    print(f'Saved dataset to {DATASET_LOCAL_PATH}')
    return dataset


def get_training_data():
    """
    Prepare email data for machine learning model training.

    Loads the configured Hugging Face dataset and converts each valid
    record into the application's training data format.

    Each record must contain a non-empty subject and body and at least
    one label that matches a category defined in :data:`LABEL_MAPPING`.
    Records that do not satisfy these requirements are skipped.

    Returns:
        list[dict]:
            A list of dictionaries containing the following keys:

            - **``subject``**: Email subject.
            - **``body``**: Email body.
            - **``category``**: Mapped application category.
    """
    dataset = load_hf_email_dataset()
    training_data = []

    for row in dataset:
        subject = (row.get('subject') or '').strip()
        body = (row.get('body') or '').strip()
        labels = row.get('labels') or []

        if not subject or not body:
            continue

        mapped_category = None
        for label in labels:
            mapped_category = LABEL_MAPPING.get(label)
            if mapped_category:
                break

        if mapped_category is None:
            continue

        training_data.append({
            'subject': subject,
            'body': body,
            'category': mapped_category,
        })

    return training_data

TRAINING_DATA = get_training_data()
