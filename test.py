import unittest
from unittest.mock import patch
import json
import joblib
import sklearn

import app

URL = 'http://127.0.0.1:5000/api/load'

class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_post_ham(self):
        input = {"input": "test input"}
        response = self.app.post(URL, data=json.dumps(input), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_spam(self):
        input = {"input": "You have been hacked. Call 1-800-unlock-me for help. This is totally not spam."}
        response = self.app.post(URL, data=json.dumps(input), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_not_string(self):
        input = {"input": 4}
        response = self.app.post(URL, data=json.dumps(input), content_type='application/json')
        self.assertEqual(response.status_code, 422)

    def test_post_missing_input(self):
        input = {"stuff": "test"}
        response = self.app.post(URL, data=json.dumps(input), content_type='application/json')
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()