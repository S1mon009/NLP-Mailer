# Gmail Auto-Categorizer with NLP

This project automatically adds category labels to Gmail messages using NLP and machine learning.

It loads a real dataset from Hugging Face, trains a lightweight classifier, and applies category labels to email subjects through the Gmail API.

## Why this project

The goal is to make large inboxes easier to organize without manual tagging. By analyzing the subject and message content, the app assigns a category such as Business, Personal, Travel, or Promotions.

## Main features

- automatic email classification,
- Gmail API integration,
- NLP-based text categorization,
- real dataset support from Hugging Face,
- confidence threshold control,
- command-line interface for manual usage,
- local caching of the training dataset.

## Project overview

The application follows a simple flow:

1. download the dataset,
2. save it locally,
3. train the model,
4. authenticate with Gmail,
5. classify incoming messages,
6. add category labels.

## Repository

- GitHub: https://github.com/your-username/NLP-Mailer

## Documentation sections

- [Getting Started](getting-started.md)
- [Configuration](configuration.md)
- [Usage](usage.md)
- [Releases](releases.md)
