from textual.app import App, ComposeResult
from textual.widgets import Button, Label, Static
from textual.containers import Container, VerticalScroll
from textual.widgets import Footer, Label, ListItem, ListView, Select



class CLIWidget(Container):
    CSS_PATH = "cli.tcss"
    options = [("First", 1), ("Second", 2)]
    my_select: Select[int] =  Select(options)

    def compose(self) -> ComposeResult:
        yield Label("="*60)
        yield Label("GMAIL SUBJECT TAGGER")
        yield Label("="*60)
        yield Label("Note: Gmail API doesn't allow direct subject modification.")
        yield Label("This tool adds colorful labels that appear next to subjects!")
        yield Label("Commands:")
        yield Select(options=self.options, classes="select")