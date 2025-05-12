# BigHelp - Interactive Linux Terminal Guide

A friendly and intuitive terminal helper designed to make learning Linux commands easy and accessible for everyone, with special focus on Arch Linux, Manjaro, and BigLinux distributions.

## 🌟 What is BigHelp?

BigHelp is an interactive terminal application built with Python and Textual that provides a user-friendly interface for learning and using Linux commands. Whether you're a complete beginner or someone looking for a convenient way to remember command syntax, BigHelp makes the terminal less intimidating and more approachable.

Originally created for BigLinux (based on Manjaro), BigHelp works perfectly with Arch Linux-based distributions and their unique package management system.

## ✨ Features

- **🎮 Interactive Interface**: Mouse and keyboard navigation with a modern TUI
- **📚 Comprehensive Tutorials**: Learn basic, network, and system commands with detailed explanations
- **🛡️ Safe Learning Environment**: Try commands safely without affecting your system
- **🎯 Beginner-Friendly**: Simple explanations and practical examples for each command
- **🔧 Practical Tools**: Built-in utilities for common tasks like checking internet connectivity and system information
- **⚡ Quick Access**: Just type `bighelp` in your terminal to get started
- **📦 Arch-Focused**: Special attention to pacman and AUR commands

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Arch Linux, Manjaro, BigLinux, or other Arch-based distribution

### Install from PyPI (Coming Soon)
```bash
pip install bighelp
```

### Install from Source
```bash
git clone https://github.com/yourusername/bighelp.git
cd bighelp
pip install -e .
```

### Arch-Based Distributions
```bash
# Using yay (AUR helper)
yay -S bighelp

# or using pamac (Manjaro)
pamac install bighelp
```

## 💡 How to Use

Simply open your terminal and type:
```bash
bighelp
```

Navigate through the menu using your mouse or keyboard arrows. The interface is divided into several sections:

1. **📚 Learn Terminal Commands**: Interactive tutorials organized by category
   - Basic Commands (ls, cd, mv, cp, etc.)
   - Network Commands (ping, wget, curl, etc.)
   - System Commands (ps, df, free, etc.)
   - Arch-Specific Commands (pacman, makepkg)

2. **🌐 Connect to Internet**: Tools for testing connectivity and network information

3. **📦 Manage Packages**: Helpers for pacman and AUR package management

4. **⚙️ System Settings**: Utilities for system information and monitoring

## 📋 Available Commands by Category

### Basic Commands
- `ls` - List directory contents
- `cd` - Change directory
- `pwd` - Print working directory
- `mkdir` - Create directories
- `cp` - Copy files and directories
- `mv` - Move/rename files and directories
- `cat` - Display file contents
- `less` - View file contents page by page

### Network Commands
- `ping` - Test network connectivity
- `wget` - Download files from the internet
- `curl` - Transfer data from/to servers
- `ip` - Network configuration (replacement for ifconfig)

### System Commands
- `ps` - Display running processes
- `df` - Show disk space usage
- `free` - Display memory usage
- `whoami` - Show current username
- `date` - Display system date and time
- `history` - Show command history
- `systemctl` - Control systemd services

### Arch-Specific Commands
- `pacman` - Package manager for Arch Linux
- `makepkg` - Build packages from PKGBUILD
- `yay/paru` - AUR helpers
- `pacman-mirrors` - Mirror management (Manjaro)

## 🎨 User Interface

BigHelp features a clean, colorful interface with:
- Easy-to-read menus
- Color-coded categories
- Keyboard shortcuts for quick navigation
- Detailed command explanations with examples
- Safe command simulation for learning
- Arch Linux theme and styling

## 🎯 Key Benefits

1. **No More Googling**: All common commands explained in one place
2. **Learn by Doing**: Interactive examples you can try safely
3. **Build Confidence**: Start with guided examples before using real commands
4. **Quick Reference**: Fast access to command syntax and options
5. **Arch-Focused**: Special tutorials for pacman and AUR
6. **BigLinux Ready**: Perfect for BigLinux users starting their Linux journey

## 🐧 Distribution Support

### Primary Support
- **Arch Linux**: Native support for pacman and Arch ecosystem
- **Manjaro**: Full compatibility with Manjaro tools and mirrors
- **BigLinux**: Optimized for BigLinux user experience

### Also Works On
- ArcoLinux
- EndeavourOS
- Garuda Linux
- Any Arch-based distribution

## 🛠️ Development

### Project Structure
```
bighelp/
├── bighelp/
│   ├── main.py          # Entry point
│   ├── ui.py            # Main UI components
│   ├── utils.py         # Utility functions
│   ├── app/             # Application logic
│   └── tutorials/       # Command documentation
├── pyproject.toml       # Project configuration
└── README.md           # This file
```

### Built With
- [Textual](https://github.com/Textualize/textual) - Modern Text User Interface framework
- [Rich](https://github.com/Textualize/rich) - Rich text and beautiful formatting

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Adding New Commands

To add new commands to the tutorials:

1. Edit the appropriate file in `bighelp/tutorials/`
2. Follow the existing format for command documentation
3. Include examples and safety notes
4. Test the interface to ensure proper display

### Arch-Specific Contributions

We especially welcome contributions that:
- Add more pacman tutorials
- Include AUR helper explanations
- Document Arch-specific system administration
- Add BigLinux-specific customizations

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to the [Textual](https://github.com/Textualize/textual) team for creating an amazing TUI framework
- BigLinux team for inspiring accessible Linux education
- Manjaro and Arch Linux communities for their excellent documentation
- Built with ❤️ for the Arch ecosystem

## 📞 Support

If you encounter any issues or have questions:
- Create an issue on GitHub
- Check the documentation in the app's "About" section
- Visit the BigLinux or Manjaro forums
- Look through existing issues for solutions

---

*Made with ❤️ specifically for Arch Linux, Manjaro, and BigLinux users*
