"""
System commands tutorial for kids.

This module contains information about system-related Linux commands.
"""

SYSTEM_COMMANDS = {
    "whoami": {
        "name": "whoami",
        "category": "System Information",
        "description": "Show who you are (your username)",
        "explanation": """
        'whoami' tells you what your username is on the computer.
        It's like asking 'What's my name on this computer?'
        """,
        "examples": [
            {
                "command": "whoami",
                "explanation": "Show your username"
            }
        ],
        "tip": "This is useful to know which user account you're using!",
        "safety": "This only shows information - completely safe."
    },
    
    "date": {
        "name": "date",
        "category": "System Information",
        "description": "Show the current date and time",
        "explanation": """
        'date' shows what day and time it is right now,
        like looking at a clock and calendar!
        """,
        "examples": [
            {
                "command": "date",
                "explanation": "Show current date and time"
            },
            {
                "command": "date +%Y-%m-%d",
                "explanation": "Show date in a specific format"
            }
        ],
        "tip": "The computer's time might be different from your local time!",
        "safety": "This only shows information - safe to use."
    },
    
    "ps": {
        "name": "ps",
        "category": "System Information",
        "description": "Show what programs are running",
        "explanation": """
        'ps' shows all the programs that are currently running on your computer,
        like seeing all the apps that are open!
        """,
        "examples": [
            {
                "command": "ps",
                "explanation": "Show your running programs"
            },
            {
                "command": "ps aux",
                "explanation": "Show all programs running on the computer"
            }
        ],
        "tip": "Each line shows a different program that's running!",
        "safety": "This only shows information - doesn't change anything."
    },
    
    "df": {
        "name": "df",
        "category": "System Information",
        "description": "Show how much space is left on your computer",
        "explanation": """
        'df' shows how much storage space you have left, like checking how much room
        is left in your toy box!
        """,
        "examples": [
            {
                "command": "df -h",
                "explanation": "Show disk space in a human-readable format"
            }
        ],
        "tip": "The -h flag makes numbers easier to read (like 5G instead of 5000000000)!",
        "safety": "This only shows information - safe to use."
    },
    
    "free": {
        "name": "free",
        "category": "System Information",
        "description": "Show how much memory (RAM) is being used",
        "explanation": """
        'free' shows how much memory your computer is using right now.
        Think of it like checking how much of your desk space is being used!
        """,
        "examples": [
            {
                "command": "free -h",
                "explanation": "Show memory usage in human-readable format"
            }
        ],
        "tip": "If 'Used' is close to 'Total', your computer might be slow!",
        "safety": "This only shows information - completely safe."
    },
    
    "history": {
        "name": "history",
        "category": "System Information",
        "description": "Show the last commands you typed",
        "explanation": """
        'history' shows a list of all the commands you've typed recently,
        like a diary of what you've been doing in the terminal!
        """,
        "examples": [
            {
                "command": "history",
                "explanation": "Show all recent commands"
            },
            {
                "command": "history | tail -10",
                "explanation": "Show only the last 10 commands"
            }
        ],
        "tip": "Use the up arrow key to repeat previous commands!",
        "safety": "This only shows your command history - safe to use."
    },
    
    "reboot": {
        "name": "reboot",
        "category": "System Control",
        "description": "Restart the computer",
        "explanation": """
        'reboot' restarts your computer, like turning it off and on again.
        Make sure to save your work first!
        """,
        "examples": [
            {
                "command": "sudo reboot",
                "explanation": "Restart the computer (needs admin permission)"
            }
        ],
        "tip": "ALWAYS save your work before rebooting!",
        "safety": "CAREFUL! This will restart your computer and close all programs."
    },
    
    "shutdown": {
        "name": "shutdown",
        "category": "System Control",
        "description": "Turn off the computer",
        "explanation": """
        'shutdown' turns off your computer safely. It's like pressing the power button
        but in a safe way that doesn't damage your files.
        """,
        "examples": [
            {
                "command": "sudo shutdown now",
                "explanation": "Turn off the computer immediately"
            },
            {
                "command": "sudo shutdown +5",
                "explanation": "Turn off the computer in 5 minutes"
            }
        ],
        "tip": "Always save your work before shutting down!",
        "safety": "CAREFUL! This will turn off your computer."
    }
}