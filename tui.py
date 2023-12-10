from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static


class WeightCollection(Static):
    """A visual representation of available weights (plates)."""


class WeightLiftingApp(App):
    """A Textual app to aid barbell training."""

    CSS_PATH = "tui.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield WeightCollection(
            "Available plates: 5, 10, 25, 45", classes="box", id="plates"
        )
        yield Static("Barbell", classes="box", id="bar")
        yield Static("Third Main for Table?", classes="box", id="main")
        # yield Static("Fourth", classes="box")
        # yield Static("Fifth", classes="box")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = WeightLiftingApp()
    app.run()
