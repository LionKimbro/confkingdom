import unittest

import os
import shutil
import pathlib

import confkingdom
import confkingdom.confkingdom


EXAMPLE_TAGURI = "tag:taoriver.net,2023-07-25:conf-kingdom-test-system"
RESULTING_FOLDERNAME = "taoriver_net_2023-07-25_conf-kingdom-test-system"

a_dictionary = {"foo": 1, "bar": 2, "baz": 3}

test_text = """foo
bar
baz

boz biz
"""


class TestConfKingdom(unittest.TestCase):
    
    def setUp(self):
        confkingdom_env = os.getenv("CONFKINGDOM")
        if confkingdom_env is None:
            raise unittest.SkipTest("You must set CONFKINGDOM environment variable for this test.")
        if not pathlib.Path(confkingdom_env).is_dir():
            raise unittest.SkipTest("CONFKINGDOM is defined, but must point to a valid directory.")
        confkingdom.setup(EXAMPLE_TAGURI)
        if confkingdom.confkingdom.base_path().exists():
            confkingdom.rmdir()
    
    def tearDown(self):
        if confkingdom.confkingdom.base_path().exists():
            confkingdom.rmdir()
    
    def test_os_environ_verification(self):
        confkingdom.setup(EXAMPLE_TAGURI)
        self.assertEqual(confkingdom.folder_name(), RESULTING_FOLDERNAME)
    
    def test_valid_environ(self):
        confkingdom.mkdir()
        self.assertTrue(confkingdom.valid_environ())
        confkingdom.rmdir()
    
    def test_makedir_deletedir(self):
        confkingdom.setup(EXAMPLE_TAGURI)
        confkingdom.mkdir()
        confkingdom.rmdir()

    def test_reading_and_writing_text(self):
        confkingdom.mkdir()
        filename = "test.txt"
        confkingdom.write_text(filename, test_text)
        self.assertEqual(confkingdom.text(filename), test_text)
        confkingdom.path_to(filename).unlink()
        confkingdom.rmdir()
    
    def test_writing_and_reading_TOML(self):
        confkingdom.mkdir()
        filename = "test.toml"
        confkingdom.write_TOML(filename, a_dictionary)
        self.assertEqual(confkingdom.TOML(filename), a_dictionary)
        confkingdom.path_to(filename).unlink()
        confkingdom.rmdir()
    
    def test_writing_and_reading_JSON(self):
        confkingdom.mkdir()
        filename = "test.json"
        confkingdom.write_JSON(filename, a_dictionary)
        self.assertEqual(confkingdom.JSON(filename), a_dictionary)
        confkingdom.path_to(filename).unlink()
        confkingdom.rmdir()


if __name__ == '__main__':
    unittest.main()

