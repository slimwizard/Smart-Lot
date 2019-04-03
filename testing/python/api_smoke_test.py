import unittest
import os
import sys
import requests

class ApiSmokeTest(unittest.TestCase):
    req = requests.get('http://api.smart-lot.io')

    def test_return_code(self):
        self.assertEqual(self.req.status_code, 200)

if __name__ == '__main__':
    unittest.main()                                                            
