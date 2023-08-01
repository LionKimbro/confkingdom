# Lion's Conf Kingdom: A Configuration Management System

written: 2023-07-21

note: This document primarily produced via ChatGPT.  [(source conversation)](https://chat.openai.com/c/b8338949-aab9-4587-a57e-3b71657190e8)


## Introduction

Lion's Conf Kingdom is a configuration management system designed for simplicity, human readability, and conflict-free operation. Conceived and developed by Lion Kimbro, for himself and other programmers in general, it uses TAG URIs and filesystem directories as a basis for unique, human-readable configuration storage.

This system is founded on a series of principles:

- **Conflict-Free:** Using modified TAG URIs ensures that programs written by different people coexist peacefully.
- **Human Readable:** Using human-readable names (via TAG URIs), not GUIDs.
- **Single-System Assumption:** The system is intended for global configuration of programs on a single computer.
- **TOML or JSON format:** These accessible, widely used, and standardized formats are the preferred choice for configuration.
- **Programmatically Easily Readable:** It should be straightforward for a program to access its configuration.
- **One Environment Variable:** A single environment variable points to your configuration root.

## How It Works

### Set the Environment Variable

Start by setting the `CONFKINGDOM` environment variable to the path of the root of your filesystem (no trailing slash). This will act as the root for your configuration directories.

If CONFKINGDOM is not set, the system will default to creating a directory "CONFKINGDOM" within the user's home directory.

### Construct the Configuration Directory Name

The programmer will create a unique Tag URI for a program, based on the syntax defined in [RFC 4151](http://www.faqs.org/rfcs/rfc4151.html), though it's easier to understand the process as described on [taguri.org](http://www.taguri.org/).

The system will convert the Tag URI to a unique folder name, by removing the "tag:" at the front of the URI, and then replacing any  characters that are not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !#$%&'()-@^_`{}~" with an underscore.  (This is a list of valid Windows filesystem characters, excluding a period.)

For example, a Tag URI like `tag:taoriver.net,2023-07-21:conf-kingdom` will become folder name: `taoriver_net_2023-07-21_conf-kingdom`.

### Use the Configuration Directory

Once you have the name of the configuration directory, you can use it for all of the configuration files of your program. Files should preferably be in TOML or JSON format.

### Install Convention

To make your program compatible with Conf Kingdom, consider supporting a convention such as `<program.exe> confinstall`. For Python programs, this would be: `python -m <package-name> confinstall`.  This command would instruct your program to create its configuration in the `CONFKINGDOM` directory, using the Tag URI-based directory naming scheme. Optional command-line arguments can further configure the installation.

### Uninstallation

While an uninstall convention like `<program.exe> confuninstall` may be beneficial, it's not required. The primary means of uninstalling the config files should be simply erasing the directory.

### Python Auto-Self-Installation

For Python, I've written a module: `confkingdom.py`.  This module supports automatic installation, so that a program, package, or module does NOT need to be run with `confinstall`.  It requires a little bit of programmer support, because the programmer needs to call an initialization routine, so that the program initialition procedures are controlled, and execute in the right order.  Each module registers itself with `confkingdom.py`, and then `confkingdom.py` takes an inventory of which programs do not yet have configuration folders.  It creates those folders, and populates them with defaults.

## Conclusion

Lion's Conf Kingdom is a streamlined, flexible, and human-readable configuration system. While it offers some guidelines and conventions, it's also flexible and leaves room for individual creativity. Remember, though, with great power comes great responsibility. Play nice!  (-- Lion's note: I'm leaving this in.  ChatGPT has a personality.  I'm fine with it.)

---

Please note that this document is intended for experienced programmers. The principles described herein are not exhaustive and do not cater to edge cases. It is, therefore, up to each developer to respect the guidelines and use the system responsibly.
