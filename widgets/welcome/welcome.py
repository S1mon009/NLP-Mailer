from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Static
from textual.containers import Container, VerticalScroll
from textual.widgets import Footer, Label, ListItem, ListView
from pathlib import Path



class WelcomeWidget(Container):
    """Welcome widget displaying application description"""
    CSS_PATH = str(Path(__file__).parent / "welcome.tcss")

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            yield Label("GMAIL SUBJECT AUTO-TAGGER")
            yield Label("This app automatically categorizes your emails!")
            yield Label("📧 What the app does:", classes="description")
            yield ListView(
                ListItem(Label("Connects to your Gmail account")),
                ListItem(Label("Analyzes email content using NLP")),
                ListItem(Label("Automatically assigns appropriate labels")),
                ListItem(Label("Example: 'Meeting tomorrow' → '📧 Work'")),
            )
            yield Label("Features:")
            yield ListView(
                ListItem(Label("Background email processing")),
                ListItem(Label("Intelligent categorization")),
                ListItem(Label("Easy Gmail integration")),
            )