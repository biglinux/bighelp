"""
Tutorial modules for BigHelp.

This package contains educational content for teaching Linux commands to kids.
"""

from .basic import BASIC_COMMANDS
from .network import NETWORK_COMMANDS
from .system import SYSTEM_COMMANDS

# Combine all commands into a single dictionary for easy access
ALL_TUTORIALS = {
    "basic": BASIC_COMMANDS,
    "network": NETWORK_COMMANDS,
    "system": SYSTEM_COMMANDS,
}