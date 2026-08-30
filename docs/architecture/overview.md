# Architecture Overview

NLP-Mailer follows a modular architecture that separates the user interface, application logic, Gmail integration, configuration and machine learning components.

---

## Architectural Layers

```text
┌─────────────────────────────────────┐
│              CLI Layer              │
│             src/cli/                │
└──────────────────┬──────────────────┘
                   │
                   ▼
┌─────────────────────────────────────┐
│          Service Layer              │
│            src/services/             │
└───────────────┬───────────┬─────────┘
                │           │
                ▼           ▼
┌────────────────────┐ ┌────────────────────┐
│ Integration Layer  │ │ Machine Learning   │
│ src/integrations/  │ │ EmailCategorizer   │
└──────────┬─────────┘ └──────────┬─────────┘
           │                      │
           ▼                      ▼
        Gmail API             ML Model
```

---

## CLI Layer

The CLI is responsible for interaction with the user.

It handles:

- command parsing;
- command execution;
- user prompts;
- displaying results.

The CLI does not directly implement Gmail API or machine learning functionality.

---

## Service Layer

The service layer contains the application's primary business logic.

The main component is:

```text
GmailSubjectTagger
```

It coordinates:

- email retrieval;
- classification;
- confidence evaluation;
- label creation;
- label assignment;
- preview operations.

---

## Integration Layer

`GmailConnector` isolates Gmail-specific functionality.

This means that the rest of the application does not need to know how OAuth, MIME parsing or Gmail API requests work.

---

## Machine Learning Layer

`EmailCategorizer` encapsulates the classification system.

It is responsible for:

- preprocessing;
- training;
- prediction;
- confidence calculation;
- model persistence.

---

## Configuration Layer

The configuration module provides centralized application settings.

This prevents constants such as paths, categories and thresholds from being scattered throughout the codebase.

---

## Design Goals

The architecture aims to provide:

- separation of concerns;
- low coupling between components;
- reusable services;
- simple testing;
- easier future extension.

For more information, see [Project Structure](project-structure.md).
