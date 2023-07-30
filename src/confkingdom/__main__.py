# __main__.py

import os
import shutil
import argparse
from . import confkingdom


command_help = """use "confinstall" to install configuration files for this module, and "confuninstall" to clear ALL configuration files for ALL modules"""


def create_confkingdom_directory():
    # Get the value of the environment variable CONFKINGDOM
    confkingdom_path = os.environ.get('CONFKINGDOM')

    if not confkingdom_path:
        print("Environment variable CONFKINGDOM is not set.")
        print("CONFKINGDOM should be set to the path of a folder where configuration folders will be created.")
        return

    # Check if the specified path exists, if not, create the directory
    if not os.path.exists(confkingdom_path):
        try:
            os.makedirs(confkingdom_path)
            print("CONFKINGDOM directory created.")
            print(f"  -> {confkingdom_path}")
        except OSError as e:
            print("Error creating CONFKINGDOM directory.")
            print(f"  -> {confkingdom_path}")
            print(f"error: {e}")
    else:
        print("CONFKINGDOM directory already exists. No action taken.")
        print(f"  -> {confkingdom_path}")


def erase_confkingdom_directory():
    # Get the value of the environment variable CONFKINGDOM_PATH
    confkingdom_path = os.environ.get('CONFKINGDOM')

    if not confkingdom_path:
        print("""Environment variable CONFKINGDOM is not set.""")
        print("""CONFKINGDOM is the path of a folder where configuration folders are kept.""")
        return

    # Check if the specified path exists, and if so, delete the directory
    if not os.path.exists(confkingdom_path):
        print("CONFKINGDOM directory does not exist.  No action taken.")
        print(f"  -> {confkingdom_path}")
    else:
        shutil.rmtree(confkingdom_path)
        print("CONFKINGDOM directory and all subdirectories erased.")
        print(f"  -> {confkingdom_path}")


def confinstall():
    create_confkingdom_directory()

def confuninstall():
    erase_confkingdom_directory()
    
    
def main():
    # Initialize the parser
    parser = argparse.ArgumentParser()

    # Define subparsers
    subparsers = parser.add_subparsers(dest='command')

    # confinstall command
    parser_install = subparsers.add_parser('confinstall', help='create CONFKINGDOM directory')
    parser_install.set_defaults(func=confinstall)

    # confuninstall command
    parser_uninstall = subparsers.add_parser('confuninstall', help='recursively delete CONFKINGDOM directory')
    parser_uninstall.set_defaults(func=confuninstall)

    # Parse arguments
    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
    else:
        # Execute the function associated with the command
        args.func()


if __name__ == "__main__":
    main()

