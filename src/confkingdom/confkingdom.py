"""confkingdom.py  -- Lion's configuration kingdom.

Basically, set the environment variable CONFKINGDOM to an empty
directory, where configuration file directories will be kept.

Each program or module (or whatever) that gets configured, is assigned
by the developer of the program (or module or whatever) a TAG URI.

So, one might be:

  tag:taoriver.net,2023-07-21:conf-kingdom

That TAG URI is converted like so:

  taoriver_net_2023-07-21_conf-kingdom

That is, everything that's not a valid file character (in Windows, at
least) is replaced with an underscore.


And then:

  %CONFKINGDOM%/taoriver_net_2023-07-21_conf-kingdom/

...is the directory that the configuration files for that program,
live in.

Config files can be anything, but I've programmed support for reading
TOML or JSON files.

Feel free to extend this with other formats, and I'll pull your
changes into the distribution.  I greatly enjoy and welcome
collaboration!
"""

import os
import shutil
import pathlib
import json
import toml


allowed_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !#$%&'()-@^_`{}~"

g = {"TAGURI": None,
     "FOLDERNAME": None,
     "ENCODING": None}


def valid_environ():
    return "CONFKINGDOM" in os.environ and base_path().exists() and base_path().is_dir()


def setup(taguri, encoding="utf-8"):
    """Declare the Tag URI identifier for this program.
    
    It should be of the form (copied from Wikipedia here:)
      "tag:" authorityName "," YYYY-MM-DD-date ":" specific [ "#" fragment ]
    
    So for example:
      "tag:taoriver.net,2023-07-21:conf-kingdom"
    
    An AssertionError will be raised if it does not start with "tag:", as expected.
    No more validation than that is performed.
    
    Call this before attempting to read any configuration files.
    
    For testing purposes, this function must be idempotent.
    
    encoding: typically "utf-8", the encoding to use for file read/write purposes
    """
    assert taguri.startswith("tag:")
    g["TAGURI"] = taguri
    L = [ch if ch in allowed_characters else "_" for ch in taguri[4:]]
    g["FOLDERNAME"] = "".join(L)
    g["ENCODING"] = encoding

def folder_name():
    return g["FOLDERNAME"]


def base_path():
    return pathlib.Path(os.environ.get("CONFKINGDOM")) / g["FOLDERNAME"]

def path_to(filename):
    """Return path to a filename within the conf directory.
    
    Call declare_taguri(taguri), first.
    """
    return base_path() / filename

def mkdir(exist_ok=False):
    """Make the directory for this project.
    
    Call declare_taguri(taguri), first.
    """
    base_path().mkdir(parents=False, exist_ok=exist_ok)

def rmdir():
    """Remove the directory for this project."""
    shutil.rmtree(base_path())


def text(text_filename):
    """Read a specified text file out of the configuration directory."""
    with open(path_to(text_filename), "r", encoding=g["ENCODING"]) as f:
        return f.read()

def TOML(toml_filename):
    """Read a specific TOML file out of the configuration directory."""
    with open(path_to(toml_filename), "r", encoding=g["ENCODING"]) as f:
        return toml.load(f)

def JSON(json_filename):
    """Read a specific JSON file out of the configuration directory."""
    with open(path_to(json_filename), "r", encoding=g["ENCODING"]) as f:
        return json.load(f)

def write_text(text_filename, content):
    with open(path_to(text_filename), "w", encoding=g["ENCODING"]) as f:
        f.write(content)

def write_TOML(toml_filename, content):
    with open(path_to(toml_filename), 'w', encoding=g["ENCODING"]) as f:
        toml.dump(content, f)

def write_JSON(json_filename, content):
    with open(path_to(json_filename), 'w', encoding=g["ENCODING"]) as f:
        json.dump(content, f)

