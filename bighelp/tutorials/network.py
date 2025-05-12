"""
Network commands tutorial for kids.

This module contains information about network-related Linux commands.
"""

NETWORK_COMMANDS = {
    "ping": {
        "name": "ping",
        "category": "Network Commands",
        "description": "Test if you can reach a website or computer",
        "explanation": """
        'ping' is like knocking on someone's door to see if they're home!
        It sends a message to another computer and waits for a reply.
        """,
        "examples": [
            {
                "command": "ping google.com",
                "explanation": "Check if you can reach Google"
            },
            {
                "command": "ping -c 4 google.com",
                "explanation": "Send only 4 pings and stop"
            }
        ],
        "tip": "Use Ctrl+C to stop pinging!",
        "safety": "This only tests connections - it's harmless."
    },
    
    "wget": {
        "name": "wget",
        "category": "Network Commands",
        "description": "Download files from the internet",
        "explanation": """
        'wget' is like a robot that goes to the internet and brings back files for you!
        You give it a web address, and it downloads the file.
        """,
        "examples": [
            {
                "command": "wget https://example.com/file.txt",
                "explanation": "Download a file from the internet"
            },
            {
                "command": "wget -O newname.txt https://example.com/file.txt",
                "explanation": "Download and give it a different name"
            }
        ],
        "tip": "Always be careful what you download from the internet!",
        "safety": "Only download files from trusted websites."
    },
    
    "curl": {
        "name": "curl",
        "category": "Network Commands",
        "description": "Get or send data from/to servers",
        "explanation": """
        'curl' is like a messenger that can talk to websites and servers.
        It can ask for information or send messages.
        """,
        "examples": [
            {
                "command": "curl https://example.com",
                "explanation": "Get a webpage's content"
            },
            {
                "command": "curl -I https://example.com",
                "explanation": "Get information about a webpage"
            }
        ],
        "tip": "curl is very powerful - ask an adult before using it!",
        "safety": "Be careful - curl can send data to the internet."
    },
    
    "ifconfig": {
        "name": "ifconfig",
        "category": "Network Commands",
        "description": "See your computer's network information",
        "explanation": """
        'ifconfig' shows your computer's network details, like your address on the internet!
        It's like checking your postal address.
        """,
        "examples": [
            {
                "command": "ifconfig",
                "explanation": "Show all network information"
            },
            {
                "command": "ip addr",
                "explanation": "A modern way to see network info"
            }
        ],
        "tip": "Look for 'inet' to find your IP address!",
        "safety": "This only shows information - it's completely safe."
    }
}