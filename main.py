"""Application entry point for the Gmail Subject Auto-Tagger.

This module provides the main entry point for the command-line
application. It initializes the CLI, performs the required setup,
and starts the tagger when the setup is completed successfully.

The application automatically assigns category labels to Gmail
messages based on their subjects.
"""
from src.cli.cli import CLI

def main() -> None:
    """Start the Gmail Subject Auto-Tagger application.

    Initializes the command-line interface and performs the required
    setup before starting the application. If the setup is successful,
    the CLI is launched. Otherwise, an error message is displayed and
    the application exits.

    Returns:
        None: This function does not return a value.
    """
    print("="*60)
    print("GMAIL SUBJECT AUTO-TAGGER")
    print("="*60)
    print("Automatically adds category labels to your Gmail!")
    print("Example: 'Meeting tomorrow' → Shows '📧 Work' label")

    cli = CLI()

    if cli.tagger.setup():
        cli.run()
    else:
        print("Setup failed. Check credentials and try again.")

if __name__ == "__main__":
    main()
