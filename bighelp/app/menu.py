"""
Menu components for BigHelp application.

This module contains all the menu interfaces used in the application.
"""

from textual.widgets import Button, Static, VerticalScroll, Markdown
from textual.containers import Container, Vertical, Horizontal
from textual.binding import Binding
from textual.screen import Screen
from textual.app import ComposeResult
from textual import events
from typing import Optional

from bighelp.tutorials import ALL_TUTORIALS
from bighelp.app.actions import AppActions


class MainMenu(Vertical):
    """Main menu with all the available options."""
    
    def compose(self) -> ComposeResult:
        """Create the main menu layout."""
        yield Static("🚀 What would you like to do today?", classes="menu-title")
        yield Button("📚 Learn Terminal Commands", id="learn-commands", variant="primary")
        yield Button("🌐 Connect to Internet", id="connect-internet") 
        yield Button("📦 Manage Packages", id="manage-packages")
        yield Button("⚙️ System Settings", id="system-settings")
        yield Button("ℹ️ About BigHelp", id="about", variant="success")
        yield Button("👋 Exit", id="exit", variant="warning")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        if event.button.id == "learn-commands":
            self.app.push_screen(TutorialMenu())
        elif event.button.id == "connect-internet":
            self.app.push_screen(NetworkActionsScreen())
        elif event.button.id == "manage-packages":
            self.app.push_screen(PackageActionsScreen())
        elif event.button.id == "system-settings":
            self.app.push_screen(SystemActionsScreen())
        elif event.button.id == "about":
            self.app.push_screen(AboutScreen())
        elif event.button.id == "exit":
            self.app.exit()


class TutorialMenu(Screen):
    """Screen for choosing which tutorial category to explore."""
    
    BINDINGS = [
        Binding("escape", "back", "Back"),
        Binding("q", "quit", "Quit")
    ]
    
    def compose(self) -> ComposeResult:
        """Create the tutorial menu layout."""
        yield Container(
            Static("📖 Choose a Topic to Learn", classes="menu-title"),
            Button("📁 Basic Commands (ls, cd, mkdir...)", id="basic", variant="primary"),
            Button("🌐 Network Commands (ping, wget...)", id="network"),
            Button("⚙️ System Commands (ps, df, date...)", id="system"),
            Button("🔙 Back to Main Menu", id="back", variant="warning"),
            classes="tutorial-menu"
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle tutorial category selection."""
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id in ["basic", "network", "system"]:
            self.app.push_screen(CommandListScreen(event.button.id))
    
    def action_back(self) -> None:
        """Go back to the previous screen."""
        self.app.pop_screen()


class CommandListScreen(Screen):
    """Screen showing all commands in a category."""
    
    BINDINGS = [
        Binding("escape", "back", "Back"),
        Binding("q", "quit", "Quit")
    ]
    
    def __init__(self, category: str) -> None:
        super().__init__()
        self.category = category
        self.commands = ALL_TUTORIALS[category]
    
    def compose(self) -> ComposeResult:
        """Create the command list layout."""
        category_title = {
            "basic": "📁 Basic Commands",
            "network": "🌐 Network Commands", 
            "system": "⚙️ System Commands"
        }
        
        yield Container(
            Static(category_title[self.category], classes="menu-title"),
            VerticalScroll(
                *[Button(f"{cmd['name']} - {cmd['description']}", 
                        id=f"cmd-{name}", variant="default")
                  for name, cmd in self.commands.items()],
                Button("🔙 Back", id="back", variant="warning"),
                classes="command-list"
            )
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle command selection."""
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id.startswith("cmd-"):
            command_name = event.button.id.replace("cmd-", "")
            self.app.push_screen(CommandDetailView(self.category, command_name))
    
    def action_back(self) -> None:
        """Go back to the previous screen."""
        self.app.pop_screen()


class CommandDetailView(Screen):
    """Detailed view of a specific command with examples."""
    
    BINDINGS = [
        Binding("escape", "back", "Back"),
        Binding("q", "quit", "Quit"),
        Binding("t", "try_command", "Try Command")
    ]
    
    def __init__(self, category: str, command: str) -> None:
        super().__init__()
        self.category = category
        self.command = command
        self.command_info = ALL_TUTORIALS[category][command]
    
    def compose(self) -> ComposeResult:
        """Create the command detail layout."""
        # Build the content markdown
        content = f"""
# 🚀 {self.command_info['name']}

## Description
{self.command_info['description']}

## What does it do?
{self.command_info['explanation']}

## Examples:
"""
        
        for example in self.command_info['examples']:
            content += f"""
### `{example['command']}`
{example['explanation']}
"""
        
        content += f"""
## 💡 Tip
{self.command_info['tip']}

## ⚠️ Safety Note
{self.command_info['safety']}
"""
        
        yield Container(
            VerticalScroll(
                Markdown(content),
                classes="command-detail"
            ),
            Horizontal(
                Button("🔧 Try This Command", id="try", variant="primary"),
                Button("🔙 Back", id="back", variant="warning"),
                classes="action-buttons"
            )
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "try":
            self.app.push_screen(InteractiveTerminal(self.command_info))
    
    def action_back(self) -> None:
        """Go back to the previous screen."""
        self.app.pop_screen()
    
    def action_try_command(self) -> None:
        """Open the interactive terminal to try the command."""
        self.app.push_screen(InteractiveTerminal(self.command_info))


class InteractiveTerminal(Screen):
    """Interactive terminal for trying commands safely."""
    
    BINDINGS = [
        Binding("escape", "back", "Back"),
        Binding("q", "quit", "Quit")
    ]
    
    def __init__(self, command_info: dict) -> None:
        super().__init__()
        self.command_info = command_info
    
    def compose(self) -> ComposeResult:
        """Create the interactive terminal layout."""
        yield Container(
            Static(f"🔧 Try the '{self.command_info['name']}' command", classes="menu-title"),
            Static("Select an example to try:", classes="instruction"),
            VerticalScroll(
                *[Button(f"Run: {example['command']}", 
                        id=f"run-{i}", variant="default")
                  for i, example in enumerate(self.command_info['examples'])],
                Button("📖 Read More About This Command", id="info", variant="success"),
                Button("🔙 Back", id="back", variant="warning"),
                classes="example-list"
            ),
            Static("", id="output", classes="terminal-output")
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle example selection."""
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "info":
            # Go back to the command detail view
            self.app.pop_screen()
        elif event.button.id.startswith("run-"):
            example_index = int(event.button.id.replace("run-", ""))
            self.run_example(example_index)
    
    def run_example(self, index: int) -> None:
        """Run the selected example command."""
        example = self.command_info['examples'][index]
        command = example['command']
        
        # For safety, we'll simulate some commands instead of actually running them
        output_widget = self.query_one("#output", Static)
        
        if command.startswith(('rm', 'sudo', 'reboot', 'shutdown')):
            output_widget.update(f"🚫 For safety, '{command}' is not executed in demo mode")
        else:
            # Simulate safe commands
            if command == "whoami":
                output_widget.update("student")
            elif command == "pwd":
                output_widget.update("/home/student")
            elif command.startswith("ls"):
                output_widget.update("Documents  Pictures  Music  Videos  Downloads")
            elif command == "date":
                output_widget.update("Mon Dec 25 10:30:00 EST 2023")
            else:
                output_widget.update(f"✅ Command '{command}' would run here safely")
    
    def action_back(self) -> None:
        """Go back to the previous screen."""
        self.app.pop_screen()


class NetworkActionsScreen(Screen):
    """Screen for network-related actions."""
    
    BINDINGS = [
        Binding("escape", "back", "Back"),
    ]
    
    def compose(self) -> ComposeResult:
        """Create network actions layout."""
        yield Container(
            Static("🌐 Network Tools", classes="menu-title"),
            Button("📡 Check Internet Connection", id="check-internet"),
            Button("🔍 Test Website Connection", id="test-website"),
            Button("📊 Show Network Information", id="network-info"),
            Button("🔙 Back", id="back", variant="warning"),
            Static("", id="result", classes="result-display")
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle network action buttons."""
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "check-internet":
            AppActions.check_internet_connection(self.query_one("#result", Static))
        elif event.button.id == "test-website":
            AppActions.test_website_connection(self.query_one("#result", Static))
        elif event.button.id == "network-info":
            AppActions.show_network_info(self.query_one("#result", Static))
    
    def action_back(self) -> None:
        """Go back to the previous screen."""
        self.app.pop_screen()


class PackageActionsScreen(Screen):
    """Screen for package management actions."""
    
    BINDINGS = [
        Binding("escape", "back", "Back"),
    ]
    
    def compose(self) -> ComposeResult:
        """Create package management layout."""
        yield Container(
            Static("📦 Package Management", classes="menu-title"),
            Static("⚠️ These actions might need admin permission", classes="warning"),
            Button("🔄 Update Package List", id="update-packages"),
            Button("🆕 Upgrade Packages", id="upgrade-packages"),
            Button("🔍 Search for Package", id="search-package"),
            Button("🔙 Back", id="back", variant="warning"),
            Static("", id="result", classes="result-display")
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle package management buttons."""
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "update-packages":
            AppActions.update_package_list(self.query_one("#result", Static))
        elif event.button.id == "upgrade-packages":
            AppActions.upgrade_packages(self.query_one("#result", Static))
        elif event.button.id == "search-package":
            AppActions.search_package(self.query_one("#result", Static))
    
    def action_back(self) -> None:
        """Go back to the previous screen."""
        self.app.pop_screen()


class SystemActionsScreen(Screen):
    """Screen for system-related actions."""
    
    BINDINGS = [
        Binding("escape", "back", "Back"),
    ]
    
    def compose(self) -> ComposeResult:
        """Create system actions layout.""" 
        yield Container(
            Static("⚙️ System Tools", classes="menu-title"),
            Button("📊 Show System Information", id="system-info"),
            Button("💾 Check Disk Space", id="disk-space"),
            Button("🖥️ Show Running Processes", id="processes"),
            Button("🔙 Back", id="back", variant="warning"),
            Static("", id="result", classes="result-display")
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle system action buttons."""
        if event.button.id == "back":
            self.app.pop_screen()
        elif event.button.id == "system-info":
            AppActions.show_system_info(self.query_one("#result", Static))
        elif event.button.id == "disk-space":
            AppActions.show_disk_space(self.query_one("#result", Static))
        elif event.button.id == "processes":
            AppActions.show_processes(self.query_one("#result", Static))
    
    def action_back(self) -> None:
        """Go back to the previous screen."""
        self.app.pop_screen()


class AboutScreen(Screen):
    """About screen with information about BigHelp."""
    
    BINDINGS = [
        Binding("escape", "back", "Back"),
    ]
    
    def compose(self) -> ComposeResult:
        """Create about screen layout."""
        about_text = """
# 🚀 BigHelp - Learn Linux Terminal!

## What is BigHelp?
BigHelp is a friendly tool designed to help kids learn the Linux terminal. 
It makes learning commands fun and safe!

## Version
0.1.0

## Features
- 📚 Interactive tutorials for Linux commands
- 🛡️ Safe learning environment  
- 🎮 Easy-to-use interface with mouse support
- 👶 Designed for beginners and kids

## How to Use
1. Click on "Learn Terminal Commands" to start
2. Choose a category (Basic, Network, or System)
3. Pick a command to learn about
4. Try it out safely!

## Tips for Learning
- Take your time
- Try the examples
- Don't be afraid to explore
- Ask for help when needed

Made with ❤️ for young Linux learners!
"""
        yield Container(
            VerticalScroll(
                Markdown(about_text),
                classes="about-content"
            ),
            Button("🔙 Back to Main Menu", id="back", variant="primary")
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle back button."""
        if event.button.id == "back":
            self.app.pop_screen()
    
    def action_back(self) -> None:
        """Go back to the previous screen."""
        self.app.pop_screen()