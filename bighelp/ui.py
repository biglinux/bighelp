"""
User Interface module for BigHelp.

This module contains the main Textual app and UI components.
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Container, VerticalScroll
from textual.binding import Binding

from bighelp.app.menu import MainMenu


class BigHelpApp(App):
    """
    Main application for BigHelp using Textual.
    """

    CSS = """
    Screen {
        background: #0f1419;
    }

    Header {
        background: #2d3748;
        color: #ffffff;
        text-align: center;
        height: 3;
    }

    Footer {
        background: #2d3748;
        color: #ffffff;
    }

    #welcome {
        width: 100%;
        height: auto;
        padding: 2 4;
        background: #4a5568;
        color: #ffffff;
        text-align: center;
        margin-bottom: 1;
    }

    .menu-container {
        width: 100%;
        height: auto;
        padding: 1 2;
    }

    Button {
        width: 100%;
        margin-bottom: 1;
        background: #3182ce;
        color: #ffffff;
        padding: 1 2;
        border: tall #2c5282;
    }

    Button:hover {
        background: #2b6cb0;
    }
    """

    TITLE = "BigHelp - Learn Linux Terminal!"
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("h", "home", "Home"),
    ]

    def compose(self) -> ComposeResult:
        """Create the UI layout."""
        yield Header()
        yield Container(
            Static("Welcome to BigHelp! The friendly terminal assistant for kids!", id="welcome"),
            VerticalScroll(
                MainMenu(),
                classes="menu-container"
            )
        )
        yield Footer()

    def action_home(self) -> None:
        """Return to the main menu."""
        self.mount(MainMenu())

    def action_quit(self) -> None:
        """Quit the application."""
        self.exit()