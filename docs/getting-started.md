# Getting Started

## Requirements

Before you start, make sure you have:

- Python 3.10+
- Git
- access to a Google Cloud project
- a valid Gmail OAuth `credentials.json` file

## Clone the repository

```bash
git clone https://github.com/your-username/NLP-Mailer.git
cd NLP-Mailer
```

## Create a virtual environment

```bash
python -m venv .venv
```

On Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Prepare Gmail credentials

1. Open the Google Cloud Console.
2. Create or select a project.
3. Enable the Gmail API.
4. Create OAuth 2.0 credentials.
5. Download the JSON file and save it as `credentials.json` in the project root.

## Run the app

```bash
python main.py
```

On first launch, the app will:

- create or load the trained model,
- authenticate with Gmail,
- download the Hugging Face dataset if needed,
- start the interactive CLI.
