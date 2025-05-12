"""
Application actions for BigHelp.

This module contains the business logic for various actions that can be performed.
"""

import subprocess
from textual.widgets import Static
from bighelp.utils import run_command, get_system_info, is_command_available


class AppActions:
    """Collection of actions that can be performed by the application."""
    
    @staticmethod
    def check_internet_connection(output_widget: Static) -> None:
        """Check if internet connection is working."""
        output_widget.update("🔍 Checking internet connection...")
        
        success, result = run_command(["ping", "-c", "1", "google.com"])
        
        if success:
            output_widget.update("✅ Internet connection is working!")
        else:
            output_widget.update("❌ No internet connection detected")
    
    @staticmethod
    def test_website_connection(output_widget: Static) -> None:
        """Test connection to a specific website."""
        # For now, test a few common websites
        websites = ["google.com", "github.com", "ubuntu.com"]
        results = []
        
        output_widget.update("🔍 Testing website connections...")
        
        for site in websites:
            success, _ = run_command(["ping", "-c", "1", site])
            status = "✅" if success else "❌"
            results.append(f"{status} {site}")
        
        output_widget.update("\n".join(results))
    
    @staticmethod
    def show_network_info(output_widget: Static) -> None:
        """Show network information."""
        output_widget.update("🔍 Getting network information...")
        
        # Try ip command first, then ifconfig
        if is_command_available("ip"):
            success, result = run_command(["ip", "addr", "show"])
        elif is_command_available("ifconfig"):
            success, result = run_command(["ifconfig"])
        else:
            output_widget.update("❌ No network tools available")
            return
        
        if success:
            # Extract key information
            lines = result.split('\n')
            info = "📡 Network Information:\n"
            for line in lines:
                if "inet " in line and "127.0.0.1" not in line:
                    ip = line.split()[1]
                    info += f"🌐 IP Address: {ip}\n"
            output_widget.update(info if info != "📡 Network Information:\n" else "❌ No active network connections")
        else:
            output_widget.update("❌ Error getting network information")
    
    @staticmethod
    def update_package_list(output_widget: Static) -> None:
        """Update the package list."""
        output_widget.update("🔄 Updating package list...")
        
        # Detect package manager
        if is_command_available("apt"):
            success, result = run_command(["sudo", "apt", "update"])
        elif is_command_available("yum"):
            success, result = run_command(["sudo", "yum", "check-update"])
        elif is_command_available("pacman"):
            success, result = run_command(["sudo", "pacman", "-Sy"])
        else:
            output_widget.update("❌ No supported package manager found")
            return
        
        if success:
            output_widget.update("✅ Package list updated successfully!")
        else:
            output_widget.update(f"❌ Error updating packages: {result}")
    
    @staticmethod
    def upgrade_packages(output_widget: Static) -> None:
        """Upgrade packages."""
        output_widget.update("⚠️ This action requires admin permissions")
        output_widget.update("💡 Run this from terminal: sudo apt upgrade")
    
    @staticmethod
    def search_package(output_widget: Static) -> None:
        """Search for a package."""
        # For demo, show how to search
        output_widget.update("🔍 To search for packages, use:\n")
        if is_command_available("apt"):
            output_widget.update("apt search <package_name>")
        elif is_command_available("yum"):
            output_widget.update("yum search <package_name>")
        elif is_command_available("pacman"):
            output_widget.update("pacman -Ss <package_name>")
        else:
            output_widget.update("No package manager found")
    
    @staticmethod
    def show_system_info(output_widget: Static) -> None:
        """Show system information."""
        output_widget.update("🔍 Getting system information...")
        
        info = get_system_info()
        display_text = f"""
💻 System Information:
━━━━━━━━━━━━━━━━━━━━
🖥️ Operating System: {info['os']}
🐧 Distribution: {info['distribution']}
📟 Terminal: {info['terminal']}
🔢 Kernel: {info['release']}
"""
        output_widget.update(display_text)
    
    @staticmethod
    def show_disk_space(output_widget: Static) -> None:
        """Show disk space information."""
        output_widget.update("💾 Checking disk space...")
        
        success, result = run_command(["df", "-h"])
        
        if success:
            # Parse and format the output
            lines = result.strip().split('\n')
            if len(lines) > 1:
                output_text = "💾 Disk Space Usage:\n━━━━━━━━━━━━━━━━━━━━\n"
                # Show only the main filesystem (usually the first one)
                for line in lines[1:]:
                    parts = line.split()
                    if len(parts) >= 6 and parts[5] == '/':
                        output_text += f"📁 Root: {parts[1]} total, {parts[2]} used, {parts[3]} available\n"
                        output_text += f"📊 Usage: {parts[4]}\n"
                        break
                output_widget.update(output_text)
            else:
                output_widget.update("❌ Unable to read disk information")
        else:
            output_widget.update("❌ Error getting disk space information")
    
    @staticmethod
    def show_processes(output_widget: Static) -> None:
        """Show running processes."""
        output_widget.update("🖥️ Getting process information...")
        
        success, result = run_command(["ps", "aux", "--sort=-%cpu"])
        
        if success:
            lines = result.split('\n')
            if len(lines) > 1:
                output_text = "🖥️ Top Processes (by CPU usage):\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                # Show header and top 5 processes
                header = lines[0]
                output_text += f"{header[:60]}...\n"
                output_text += "─" * 60 + "\n"
                
                for i, line in enumerate(lines[1:6]):
                    if line.strip():
                        parts = line.split(None, 10)
                        if len(parts) >= 11:
                            cpu = parts[2]
                            mem = parts[3]
                            command = parts[10][:30]
                            output_text += f"CPU: {cpu:>5}% | MEM: {mem:>5}% | {command}...\n"
                
                output_widget.update(output_text)
            else:
                output_widget.update("❌ Unable to read process information")
        else:
            output_widget.update("❌ Error getting process information")