import unittest
import os
import sys
import requests
import json

class TestGetLotsByLocation(unittest.TestCase):
    req = requests.get('http://api.smart-lot.io/smart-lot/lots/by_location/32.5232,-92.6379')

    lots = json.loads(req.text)

    def test_not_null(self):
        self.assertNotEqual(0, len(self.lots))

    def test_attrs_exist(self):
        for lot in self.lots:
            with self.subTest(lot=lot):
                self.assertIn('campus_id', lot)
                self.assertIn('description', lot)
                self.assertIn('latitude', lot)
                self.assertIn('longitude', lot)
                self.assertIn('lot_id', lot)
                self.assertIn('lot_name', lot)
                self.assertIn('lot_number', lot)
if __name__ == '__main__':
    unittest.main()                                                    
