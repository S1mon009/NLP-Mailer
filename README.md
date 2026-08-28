# Gmail Auto-Categorizer with NLP

![Static Badge](https://img.shields.io/badge/python-python?style=for-the-badge&logo=python&logoColor=%23fff&color=%233776AB) ![Static Badge](https://img.shields.io/badge/scikitlearn-scikitlearn?style=for-the-badge&logo=scikitlearn&logoColor=%23fff&color=%23F7931E) ![Static Badge](https://img.shields.io/badge/gmail-gmail?style=for-the-badge&logo=gmail&logoColor=%23fff&color=%23EA4335)

Automatic addition of categories to Gmail message subjects using machine learning and natural language processing (NLP).

## Description

This project uses NLP algorithms to analyze email subjects and automatically assign appropriate categories. It helps organize the Gmail inbox by adding category labels to messages, making them easier to manage and search.

## Features

- **Automatic categorization**: analysis of email subjects and assignment of categories such as Business, Personal, Finance, Travel, Promotions, and more.
- **Gmail API integration**: direct connection to Gmail for fetching and tagging messages.
- **ML model**: uses TF-IDF and Naive Bayes for text classification.
- **Dry-run mode**: preview changes before applying them.
- **Configurable confidence thresholds**: set a minimum confidence level for categorization.
- **Command-line interface**: easy execution from the terminal.
- **Real dataset support**: loads and stores a public dataset from Hugging Face for training.

## Prerequisites

- Python 3.10 or newer
- Gmail account with API access enabled
- `credentials.json` file with Gmail API credentials
- Internet access for the first dataset download

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gmail-auto-categorizer-with-nlp.git
   cd gmail-auto-categorizer-with-nlp
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source .venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Gmail API Authentication**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Gmail API
   - Create credentials (OAuth 2.0 Client ID)
   - Add the Gmail address you want to use in the application to the test users list
   - Download the `credentials.json` file and place it in the project's root directory

2. **First Run**:
   - On the first run, the application performs the authentication flow
   - Select the Gmail address you added to the test users list
   - A `token.json` file will be created for future sessions

## Usage

### Basic Execution

```bash
python main.py
```

The application automatically:

- checks whether a model exists,
- trains the model if it does not exist,
- authenticates with Gmail,
- processes recent email messages,
- adds category labels to subjects.

## Categories

The model recognizes the following categories from the dataset:

- **Business**
- **Reminders**
- **Events & Invitations**
- **Finance & Bills**
- **Travel & Bookings**
- **Customer Support**
- **Personal**
- **Newsletters**
- **Job Application**
- **Promotions**

## ML Model

- **Vectorizer**: TF-IDF with a maximum of 1000 features
- **Classifier**: Naive Bayes (MultinomialNB)
- **Training data**: public email dataset from Hugging Face
- **Model saving**: saved as `src/models/email_model.pkl`

## Security

- the application requires Gmail modification access only for labels,
- authentication tokens are stored locally,
- no email content is sent outside local processing.

## Troubleshooting

### Authentication Error

- verify that `credentials.json` is valid,
- remove `token.json` and run the app again for fresh authentication.

### Missing Model

- the model is created automatically on the first run,
- you can force retraining by deleting `src/models/email_model.pkl`.

### Low Categorization Accuracy

- adjust the confidence threshold,
- consider adding your own custom training data.

### Dataset Download Issues

- ensure internet access is available,
- verify the local dataset cache exists and is not corrupted.
