from textual.app import App
from textual.app import App, ComposeResult
from textual.widgets import Welcome
from widgets.welcome.welcome import WelcomeWidget
from textual.widgets import Header
from widgets.cli.cli import CLIWidget

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield CLIWidget()
        # yield WelcomeWidget()
        
    def on_mount(self) -> None:
        self.title = "Gmail Auto-Categorizer"
        self.sub_title = "categorize your emails with NLP"

if __name__ == "__main__":
    app = MyApp()
    app.run()