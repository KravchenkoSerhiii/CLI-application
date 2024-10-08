import unittest
import json
from unittest.mock import patch
from app import app


class TestFileClient(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('requests.get')
    def test_stat_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "create_datetime": "2024-10-08T12:34:56Z",
            "size": 1234,
            "mimetype": "text/plain",
            "name": "example.txt"
        }

        response = self.app.get('/file/0858cf1a-769c-46ab-88fb-12710f8f44a7/stat/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], "example.txt")
        self.assertEqual(data['size'], 1234)

    @patch('requests.get')
    def test_read_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = b'This is an example file.\n'

        response = self.app.get('/file/0858cf1a-769c-46ab-88fb-12710f8f44a7/read/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'This is an example file.\n')


if __name__ == '__main__':
    unittest.main()
