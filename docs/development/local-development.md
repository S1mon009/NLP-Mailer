# Local Development

This guide explains how to prepare an NLP-Mailer development environment.

---

## Clone the Repository

```bash
git clone https://github.com/S1mon009/NLP-Mailer.git
cd NLP-Mailer
```

---

## Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start NLP-Mailer with:

```bash
python main.py
```

---

## Running Documentation Locally

Start the MkDocs development server:

```bash
mkdocs serve
```

The documentation can then be viewed through the local MkDocs server.

---

## Building Documentation

Create a production documentation build:

```bash
mkdocs build
```

For CI-style validation, use:

```bash
mkdocs build --strict
```

The `--strict` option treats documentation warnings as errors and is recommended for continuous integration.

---

## Development Principles

When extending NLP-Mailer:

- keep responsibilities separated;
- avoid putting Gmail API calls directly in the CLI;
- keep ML logic inside `EmailCategorizer`;
- keep Gmail-specific logic inside `GmailConnector`;
- update docstrings when public APIs change;
- update documentation when behavior changes.
