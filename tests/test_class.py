import unittest
import pandas as pd
from qa.app import app

class TestAskMe(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    def tearDown(self):
        pass

    def test_page(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_faulty_page(self):
        response = self.app.get('/faulty', follow_redirects=True)
        self.assertEqual(response.status_code, 404)