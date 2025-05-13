"""
User Interface module for BigHelp.

This module contains the main Textual app and UI components.
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Container, VerticalScroll
from textual.binding import Binding

from app.menu import MainMenu


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

    Button:focus {
        border: tall #ffffff;
        background: #2b6cb0;
    }


    """

    TITLE = "BigHelp - Learn Linux Terminal!"
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("h", "home", "Home"),
        Binding("tab", "focus_next", "Next", show=False),
        Binding("shift+tab", "focus_previous", "Previous", show=False),
        Binding("up", "focus_previous", "Previous", show=False),
        Binding("down", "focus_next", "Next", show=False),
        Binding("enter", "select", "Select", show=False),
    ]

    def compose(self) -> ComposeResult:
        """Create the UI layout."""
        yield Header()
        yield Container(
            Static("Welcome to BigHelp! The friendly terminal assistant!", id="welcome"),
            VerticalScroll(
                MainMenu(),
                classes="menu-container"
            )
        )
        yield Footer()

    def on_mount(self) -> None:
        """Initialize the app when mounted."""
        # Focus the first button in the main menu
        buttons = self.query("Button")
        if buttons:
            buttons[0].focus()

    def action_home(self) -> None:
        """Return to the main menu."""
        self.clear_screen()
        self.mount(MainMenu())
        # Focus first button after returning home
        self.call_after_refresh(self._focus_first_button)

    def _focus_first_button(self) -> None:
        """Focus the first button."""
        buttons = self.query("Button")
        if buttons:
            buttons[0].focus()

    def action_quit(self) -> None:
        """Quit the application."""
        self.exit()

    def action_select(self) -> None:
        """Press the currently focused button."""
        focused = self.query("Button:focus")
        if focused:
            focused[0].press()