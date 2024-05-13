# Conditional Directory Creator

This repository contains a shell script named `ifExample.sh` which is designed to demonstrate conditional directory creation on a macOS system.

## Description

The `ifExample.sh` script provides a simple example of using conditional statements in a shell script to manage directories based on certain conditions. Specifically, it:
- Checks for the existence of a directory named `new_folder`.
- Creates a directory named `if_folder` if `new_folder` exists.
- Uses an if-else structure to create a directory named `hyperionDev` if `if_folder` exists, or creates `new-projects` otherwise.

## Getting Started

### Prerequisites

Ensure you are using a macOS or other Unix-like operating system to run the shell script as intended. You might need to grant execution permissions to the script by running:

```bash
chmod +x ifExample.sh
```

### Installation

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/dreamVaux/my_bootcamp_tasks.git
```

### Usage

To run the script, navigate to the directory where the script is located, and execute it from the terminal:
```bash
./ifExample.sh
```

### Contributing

We welcome contributions to this project! Please fork the repository and submit a pull request with your enhancements.

### License

This project is licensed under the MIT License - see the LICENSE file for details.