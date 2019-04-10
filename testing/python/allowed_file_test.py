import unittest
import os
import sys
import requests
import json
script_path = "../../lot-availability-api/"
sys.path.append(os.path.abspath(script_path))
import application

class TestAllowedFile(unittest.TestCase):
    pdf = 'test.pdf'
    png = 'test.png'
    junk = 'afnbwuvqewiboibvuesruib48305w7ertdufhj skdnf'
    
    def test_junk_string(self):
        self.assertFalse(application.allowed_file(self.junk))

    def test_not_in_extensions(self):
        self.assertFalse(application.allowed_file(self.pdf))

    def test_in_extensions(self):
        self.assertTrue(application.allowed_file(self.png))

if __name__ == '__main__':
    unittest.main()
