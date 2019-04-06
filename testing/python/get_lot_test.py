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
from pprint import pprint as pp
script_path = "../../lot-availability-api/"
sys.path.append(os.path.abspath(script_path))
import application
from models import *



class TestGetLot(unittest.TestCase):
    output = subprocess.Popen(['curl', '-i', '-X', 'GET', 
        'localhost:5000/smart-lot/lots/a19f71fc-4d20-4790-9e38-31df6a02ac76'],
        stdout=subprocess.PIPE)
    
    comm = output.communicate()[0].decode('utf-8').split('\n')
    
    lots = json.loads(list(filter(None, comm))[-1])

    http_code = comm[0]

    def test_http_code(self):
        self.assertIn('200', self.http_code)

    def test_non_empty_response(self):
        self.assertNotEqual(0, len(self.lots))

if __name__ == '__main__':
    unittest.main()

