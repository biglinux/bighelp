"""
Utility functions for BigHelp.

This module contains various helper functions used throughout the application.
"""

import os
import platform
import subprocess
from typing import Tuple, List, Optional


def is_command_available(command: str) -> bool:
    """
    Check if a command is available in the system.
    
    Args:
        command: The command to check
        
    Returns:
        True if the command is available, False otherwise
    """
    try:
        subprocess.run(
            ["which", command], 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            check=False,
            text=True
        )
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False


def get_system_info() -> dict:
    """
    Get basic system information.
    
    Returns:
        A dictionary with system information
    """
    info = {
        "os": platform.system(),
        "distribution": "",
        "release": platform.release(),
        "terminal": os.environ.get("TERM", "Unknown"),
    }
    
    # Try to get Linux distribution name
    if info["os"] == "Linux":
        try:
            with open("/etc/os-release", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("NAME="):
                        info["distribution"] = line.split("=")[1].strip().strip('"')
                        break
        except (FileNotFoundError, PermissionError):
            pass
            
    return info


def run_command(command: List[str], timeout: int = 5) -> Tuple[bool, str]:
    """
    Run a command safely and return its output.
    
    Args:
        command: List of command and arguments to run
        timeout: Maximum time to wait for the command to complete
        
    Returns:
        A tuple (success, output)
    """
    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=timeout,
            text=True
        )
        
        if result.returncode == 0:
            return True, result.stdout
        else:
            return False, result.stderr
    except subprocess.TimeoutExpired:
        return False, "Command timed out"
    except Exception as e:
        return False, f"Error running command: {e}"


def format_command_help(command: str, description: str, example: str) -> str:
    """
    Format help text for a command in a child-friendly way.
    
    Args:
        command: The command name
        description: Simple description of what the command does
        example: Example usage of the command
        
    Returns:
        Formatted help text
    """
    return f"""
    ✨ [bold]{command}[/bold] ✨
    
    {description}
    
    [green]Try this:[/green]
    [yellow]{example}[/yellow]
    """