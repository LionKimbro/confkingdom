## How to use the Python confkingdom Module
written: 2023-07-30

### How to Use "confkingdom" In a Python Module

    import confkingdom
    
    PROGRAM_TAG = "tag:<your domain or email address here>,<YYYY-MM-DD here>:<unique-name-here>"
    # example:
    # PROGRAM_TAG = "tag:my-email-address@example.net,2023-07-30:identifier-for-my-program"
    
    config = None  # configuration data, will be populated during init() call
    
    ...
    
    def init():
        global config
        ...
        confkingdom.setup(PROGRAM_TAG)
        config = confkingdom.TOML("config.toml")
        ...
        

### How to  Add "confinstall" and "confuninstall" Commands to a  Python Package

1. create your Python package
2. add a dependency on "confkingdom" (in pyproject.toml)
3. include a `__main__.py` file

#### `__main__.py`

    import argparse
    import confkingdom
    
    PROGRAM_TAG = "tag:<your domain or email address here>,<YYYY-MM-DD here>:<unique-name-here>"
    # example:
    # PROGRAM_TAG = "tag:my-email-address@example.net,2023-07-30:identifier-for-my-program"
    
    initial_conf_text = """
    [user]
    # Set the default username here.
    username = "default-username-not-set"
    
    [CLI]
    color = false
    """"
    
    def confinstall():
        confkingdom.mkdir(exist_ok=True)
        confkingdom.write_text("conf.toml", initial_conf_text)
        print("installed")
    
    def confuninstall():
        confkingdom.rmdir()
        print("uninstalled")
    
    def main():
        # Setup confkingdom
        confkingdom.setup(PROGRAM_TAG)
        
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

