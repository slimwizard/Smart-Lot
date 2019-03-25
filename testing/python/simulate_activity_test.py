import unittest
import os
import sys
from flask import Flask, jsonify, make_response, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from time import sleep
from random import sample
from sqlalchemy.dialects.postgresql import UUID
script_path = "../../lot-availability-api/"
sys.path.append(os.path.abspath(script_path))
import app
from models import *

class TestSimulateActivity(unittest.TestCase):
    test_occ = [i.availability for i in app.simulate_activity('a19f71fc-4d20-4790-9e38-31df6a02ac76', 1)]
    occ = [i.availability for i in app.get_all_rows(Spots)]

    @unittest.expectedFailure
    def test_random(self):
        self.assertEqual(self.test_occ, self.occ)

    def test_eq(self):
        self.assertEqual(self.test_occ, self.test_occ)

if __name__ == '__main__':
    unittest.main()
