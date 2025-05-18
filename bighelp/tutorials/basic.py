"""
Basic Linux commands tutorial for kids.

This module contains information about fundamental Linux terminal commands.
"""

BASIC_COMMANDS = {
    "ls": {
        "name": "ls",
        "category": "File and Directory Commands",
        "description": "List what's inside a folder (like looking in a box!)",
        "explanation": """
        The 'ls' command shows you all the files and folders in your current location.
        It's like looking inside a box to see what toys are there!
        """,
        "examples": [
            {
                "command": "ls",
                "explanation": "Show all files and folders"
            },
            {
                "command": "ls -l",
                "explanation": "Show files with more details (like size and date)"
            },
            {
                "command": "ls -a",
                "explanation": "Show hidden files too (files that start with a dot)"
            }
        ],
        "tip": "Try 'ls -la' to see everything with details!",
        "safety": "This command only looks at files - it doesn't change anything."
    },

    "cd": {
        "name": "cd",
        "category": "File and Directory Commands",
        "description": "Change directory - move to a different folder",
        "explanation": """
        The 'cd' command helps you move around folders, like walking to different rooms
        in your house! Each folder is like a room with different things inside.
        """,
        "examples": [
            {
                "command": "cd Documents",
                "explanation": "Go into the Documents folder"
            },
            {
                "command": "cd ..",
                "explanation": "Go back to the parent folder (like going up one level)"
            },
            {
                "command": "cd ~",
                "explanation": "Go to your home folder (your personal space)"
            },
            {
                "command": "cd /",
                "explanation": "Go to the root folder (the very top of the computer)"
            }
        ],
        "tip": "Always remember: '..' means 'go back one folder'",
        "safety": "This command only moves you around - it doesn't delete anything."
    },

    "pwd": {
        "name": "pwd",
        "category": "File and Directory Commands",
        "description": "Print working directory - show me where I am",
        "explanation": """
        When you're lost, 'pwd' tells you exactly where you are! It shows the full path
        from the top of the computer to your current location, like your address.
        """,
        "examples": [
            {
                "command": "pwd",
                "explanation": "Show exactly where you are right now"
            }
        ],
        "tip": "Use this command when you get lost in folders!",
        "safety": "This command only shows information - it's completely safe."
    },

    "mkdir": {
        "name": "mkdir",
        "category": "File and Directory Commands",
        "description": "Make directory - create a new folder",
        "explanation": """
        'mkdir' creates new folders, like making a new box to put things in!
        You give it a name, and it makes the folder for you.
        """,
        "examples": [
            {
                "command": "mkdir MyFolder",
                "explanation": "Create a folder called 'MyFolder'"
            },
            {
                "command": "mkdir Games Pictures",
                "explanation": "Create two folders at once"
            },
            {
                "command": "mkdir -p Documents/Projects/NewProject",
                "explanation": "Create nested folders (folders inside folders)"
            }
        ],
        "tip": "Use -p to create multiple levels of folders at once!",
        "safety": "This creates new folders - it won't overwrite existing ones."
    },

    "rmdir": {
        "name": "rmdir",
        "category": "File and Directory Commands",
        "description": "Remove directory - delete an empty folder",
        "explanation": """
        'rmdir' removes empty folders. Think of it like throwing away an empty box.
        It only works if the folder has nothing inside it!
        """,
        "examples": [
            {
                "command": "rmdir EmptyFolder",
                "explanation": "Remove a folder that has nothing inside"
            }
        ],
        "tip": "The folder must be completely empty for this to work!",
        "safety": "BE CAREFUL! This deletes folders, but only empty ones."
    },

    "cp": {
        "name": "cp",
        "category": "File and Directory Commands",
        "description": "Copy files and folders",
        "explanation": """
        'cp' makes copies of files or folders, like using a copy machine!
        You can copy something and put the copy in a different place.
        """,
        "examples": [
            {
                "command": "cp myfile.txt copy_of_myfile.txt",
                "explanation": "Make a copy of a file"
            },
            {
                "command": "cp myfile.txt Documents/",
                "explanation": "Copy a file to the Documents folder"
            },
            {
                "command": "cp -r MyFolder NewFolder",
                "explanation": "Copy a whole folder and everything inside it"
            }
        ],
        "tip": "Use -r to copy folders and everything inside them!",
        "safety": "This makes copies - the original files stay safe."
    },

    "mv": {
        "name": "mv",
        "category": "File and Directory Commands",
        "description": "Move or rename files and folders",
        "explanation": """
        'mv' can move files to different folders OR rename them. It's like picking up
        your toy and putting it in a different box, or giving it a new name!
        """,
        "examples": [
            {
                "command": "mv oldname.txt newname.txt",
                "explanation": "Rename a file"
            },
            {
                "command": "mv myfile.txt Documents/",
                "explanation": "Move a file to the Documents folder"
            },
            {
                "command": "mv MyFolder NewLocation/",
                "explanation": "Move a folder to a new place"
            }
        ],
        "tip": "mv can both move AND rename - it's like magic!",
        "safety": "BE CAREFUL! This moves files - they might not be in the same place!"
    },

    "cat": {
        "name": "cat",
        "category": "File Viewing Commands",
        "description": "Show the contents of a file",
        "explanation": """
        'cat' shows you what's written inside a file, like opening a book to read it!
        It displays the text right on your screen.
        """,
        "examples": [
            {
                "command": "cat story.txt",
                "explanation": "Show what's written in story.txt"
            },
            {
                "command": "cat file1.txt file2.txt",
                "explanation": "Show the contents of multiple files"
            }
        ],
        "tip": "Great for reading small text files quickly!",
        "safety": "This only shows files - it doesn't change them."
    },

    "less": {
        "name": "less",
        "category": "File Viewing Commands",
        "description": "View file contents one page at a time",
        "explanation": """
        'less' shows big files one screen at a time, like reading a book page by page!
        You can scroll up and down, and press 'q' to quit.
        """,
        "examples": [
            {
                "command": "less bigfile.txt",
                "explanation": "View a big file one page at a time"
            }
        ],
        "tip": "Use arrows to navigate, 'q' to quit, '/' to search",
        "safety": "This only views files - it's safe to use."
    },

    "touch": {
        "name": "touch",
        "category": "File and Directory Commands",
        "description": "Create new empty files or update file timestamps",
        "explanation": """
        The 'touch' command is like magic fingers that can:
        1. Create brand new empty files (like getting a new notebook)
        2. Update the timestamp of existing files (like writing the current date on a file)
        """,
        "examples": [
            {
                "command": "touch myfile.txt",
                "explanation": "Create a new empty file called 'myfile.txt'"
            },
            {
                "command": "touch notes.txt homework.pdf",
                "explanation": "Create multiple files at once"
            },
            {
                "command": "touch existing_file.txt",
                "explanation": "Update the last modified time of an existing file"
            },
            {
                "command": "touch -t 202401011200 special.txt",
                "explanation": "Create a file with a specific timestamp (Jan 1, 2024 at noon)"
            }
        ],
        "tip": "Great for quickly creating files before editing them with nano/vim!",
        "safety": "BE CAREFUL! Won't ask before overwriting existing files with -c flag"
    }
}
