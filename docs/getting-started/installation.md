# Installation

This guide explains how to install NLP-Mailer and prepare the local Python environment.

---

## Requirements

Before installing NLP-Mailer, make sure the following software is available:

- Python 3.10 or newer
- Git
- pip
- a Gmail account
- a Google Cloud project with access to the Gmail API

NLP-Mailer is designed to run locally and does not require a GPU.

---

## Clone the Repository

Clone the repository using Git:

```bash
git clone https://github.com/S1mon009/NLP-Mailer.git
cd NLP-Mailer
```

---

## Create a Virtual Environment

A virtual environment is recommended to isolate NLP-Mailer's dependencies from other Python projects.

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### macOS and Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activation, the terminal should indicate that the virtual environment is active.

---

## Install Dependencies

Install the project's Python dependencies:

```bash
pip install -r requirements.txt
```

The dependencies include the libraries required for:

- Gmail API communication,
- OAuth authentication,
- natural language processing,
- machine learning,
- dataset loading,
- documentation generation.

---

## Verify the Installation

Verify that Python is available:

```bash
python --version
```

Then verify that the main dependencies can be imported:

```bash
python -c "import sklearn, nltk, googleapiclient; print('Installation successful')"
```

---

## Project Structure

After installation, the project should have a structure similar to:

```text
NLP-Mailer/
├── src/
│   ├── cli/
│   ├── config/
│   ├── datasets/
│   ├── integrations/
│   ├── models/
│   └── services/
│
├── docs/
├── main.py
├── mkdocs.yml
├── requirements.txt
└── README.md
```

---

## Next Steps

After installing the dependencies, continue with:

1. [Configuration](configuration.md)
2. [Gmail Setup](gmail-setup.md)
3. [First Run](first-run.md)
