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

# Label Colors (for Gmail)
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
    '''Download the public email classification dataset and cache it locally.'''
    if DATASET_LOCAL_PATH.exists():
        print(f'Loading cached dataset from {DATASET_LOCAL_PATH}')
        return load_from_disk(str(DATASET_LOCAL_PATH))

    dataset = load_dataset(DATASET_NAME, split='train')
    DATASET_LOCAL_PATH.mkdir(parents=True, exist_ok=True)
    dataset.save_to_disk(str(DATASET_LOCAL_PATH))
    print(f'Saved dataset to {DATASET_LOCAL_PATH}')
    return dataset


def get_training_data():
    '''Map HF dataset labels to the project's category set.'''
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


# Training Data
TRAINING_DATA = get_training_data()