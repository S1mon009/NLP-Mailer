# Gmail Auto-Categorizer with NLP

Automatic addition of categories to Gmail message subjects using machine learning and natural language processing (NLP).

## Description

This project uses NLP algorithms to analyze email subjects and automatically assign appropriate categories. It enables Gmail inbox organization by adding category labels to messages, making management and searching easier.

## Features

- **Automatic categorization**: Analysis of email subjects and assignment of categories such as "Work", "Personal", "Finance", etc.
- **Gmail API integration**: Direct connection to Gmail for fetching and tagging messages.
- **ML model**: Uses TF-IDF and Naive Bayes for text classification.
- **Dry-run mode**: Ability to preview changes without applying them.
- **Configurable confidence thresholds**: Setting minimum confidence level for categorization.
- **Command-line interface**: Easy execution from the command line.

## Prerequisites

- Python 3.8 or newer
- Gmail account with API access enabled
- `credentials.json` file with Gmail API credentials

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
   - Linux/Mac:
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
   - Enable Gmail API
   - Create credentials (OAuth 2.0 Client ID)
   - Download the `credentials.json` file and place it in the project's root directory

2. **First Run**:
   - On the first run, the application will perform the authentication process
   - A `token.json` file will be created for future sessions

## Usage

### Basic Execution

```bash
python main.py
```

The application automatically:

- Checks and trains the model if it doesn't exist
- Authenticates with Gmail
- Processes the last 50 messages
- Adds category labels to subjects

## Categories

The application recognizes the following categories:

- **Work**: Meetings, projects, deadlines
- **Personal**: Personal messages, birthdays
- **Finance**: Bills, bank statements
- **Shopping**: Orders, deliveries
- **Social**: Social media notifications
- **Promotions**: Offers, discounts
- **Spam**: Spam and suspicious messages
- **Newsletters**: Newsletters, bulletins

## ML Model

- **Vectorizer**: TF-IDF with maximum 1000 features
- **Classifier**: Naive Bayes (MultinomialNB)
- **Training data**: Built-in examples for each category
- **Model saving**: Model is saved as `src/models/email_model.pkl`

## Security

- The application requires only Gmail modification access (labels)
- Authentication tokens are stored locally
- Does not send email content outside local processing

## Troubleshooting

### Authentication Error

- Check if `credentials.json` is valid
- Delete `token.json` and run again for re-authentication

### Missing Model

- Model will be automatically trained on first run
- Force retraining by deleting `src/models/email_model.pkl`

### Low Categorization Accuracy

- Adjust confidence threshold
- Consider adding your own training data
