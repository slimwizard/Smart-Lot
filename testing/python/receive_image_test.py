import unittest
import os
import sys
from flask import Flask, jsonify, make_response, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from time import sleep
from random import sample
from sqlalchemy.dialects.postgresql import UUID
import subprocess
import json
script_path = "../../lot-availability-api/"
sys.path.append(os.path.abspath(script_path))
import application
from models import *


class TestReceiveImage(unittest.TestCase): 
    occ = [i.availability for i in application.get_all_rows(Spots)[::-1]]
    output = subprocess.Popen(['curl', '-i', '-X', 'POST',
        '-F', 'file=@{}'.format(os.path.abspath('../resources/test_image.png')),
        'localhost:5000/smart-lot/upload/a19f71fc-4d20-4790-9e38-31df6a02ac76/shoop'],
        stdout=subprocess.PIPE)

    comm = output.communicate()[0].decode('utf-8').split('\n')
    
    occ_list = json.loads(list(filter(None, comm))[-1])

    http_code = comm[2]

    def test_update(self):
        for i in self.occ_list:
            self.assertFalse(self.occ_list[i])

    def test_http_code(self):
        self.assertIn('200', self.http_code)

if __name__ == '__main__':
    unittest.main()
