#!/usr/bin/env python3
"""
Main entry point for the BigHelp application.
"""

import sys
from bighelp.ui import BigHelpApp


def main():
    """
    Main function to start the BigHelp application.
    """
    try:
        app = BigHelpApp()
        app.run()
    except KeyboardInterrupt:
        print("\nGoodbye! Hope you learned something new today!")
        sys.exit(0)
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()