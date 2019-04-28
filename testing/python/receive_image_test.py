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
    occ = [i.occupied for i in application.get_all_rows(Spots)[::-1]]
    output1 = subprocess.Popen(['curl', '-i', '-X', 'POST',
        '-F', 'file=@{}'.format(os.path.abspath('../resources/api_test2.png')),
        'localhost:5000/smart-lot/upload/a19f71fc-4d20-4790-9e38-31df6a02ac76/shoop'],
        stdout=subprocess.PIPE)


    anticipated_response = [{"spot":"1","status":"occupied"},{"spot":"2","status":"occupied"},{"spot":"3","status":"occupied"},{"spot":"4","status":"occupied"},{"spot":"5","status":"unoccupied"},{"spot":"6","status":"occupied"},{"spot":"7","status":"occupied"},{"spot":"8","status":"occupied"},{"spot":"9","status":"unoccupied"},{"spot":"10","status":"occupied"},{"spot":"11","status":"unoccupied"},{"spot":"12","status":"occupied"},{"spot":"13","status":"occupied"},{"spot":"14","status":"occupied"},{"spot":"15","status":"occupied"},{"spot":"16","status":"occupied"},{"spot":"17","status":"occupied"},{"spot":"18","status":"unoccupied"}]

    # test for correct response when wrong key is sent
    output2 = subprocess.Popen(['curl', '-i', '-X', 'POST',
        '-F', 'file=@{}'.format(os.path.abspath('../resources/api_test2.png')),
        'localhost:5000/smart-lot/upload/a19f71fc-4d20-4790-9e38-31df6a02ac76/wrongkey'],
        stdout=subprocess.PIPE)

    comm1 = output1.communicate()[0].decode('utf-8').split('\n')
    comm2 = output2.communicate()[0].decode('utf-8').split('\n')
    
    http_code1 = comm1[2]
    http_code2 = comm2[2]

    def test_update(self):
        self.assertIn(self.anticipated_response, comm1[1])

    def test_http_code(self):
        self.assertIn('200', self.http_code1)

    def test_wrong_key(self):
        self.assertIn('405', self.http_code2)

if __name__ == '__main__':
    unittest.main()
