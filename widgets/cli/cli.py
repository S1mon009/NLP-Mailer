from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Static
from textual.containers import Container, VerticalScroll
from textual.widgets import Footer, Label, ListItem, ListView, Select
from pathlib import Path



class CLIWidget(Container):
    options = [
        ("Tag [N] - Tag N recent emails (default: 20)", 1),
        ("Preview [N] - Preview what would be tagged", 2),
        ("Preview [N] - Preview what would be tagged", 3),
        ("Unread - Tag only unread emails", 4),
        ("Today - Tag emails from today", 5),
        ("Week - Tag emails from this week", 6),
        ("Test - Test categorization", 7),
        ("Confidence - Set custom confidence threshold", 8),
        ("Clear - Remove all category labels", 9),
        ("Quit - Exit", 10),
    ]

    def compose(self) -> ComposeResult:
        yield Label("Note: Gmail API doesn't allow direct subject modification.", variant="warning")
        yield Label("This tool adds colorful labels that appear next to subjects!", variant="warning")
        yield Label("-"*60)
        yield Label("Commands:")
        yield Select(options=self.options, prompt="Choose an option")

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        print(str(event.value))