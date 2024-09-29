#code written by: syeda Nida and Amrutha

import unittest
from unittest.mock import patch
from mastodon_service import create_post, retrieve_post, delete_post

class TestMastodonService(unittest.TestCase):

    # Test for creating a post
    @patch('mastodon.Mastodon.status_post')
    def test_create_post(self, mock_status_post):
        mock_status_post.return_value = {"id": "123", "content": "Test post"}
        response = create_post("Test post")
        self.assertEqual(response["content"], "Test post")

    # Test for retrieving a post
    @patch('mastodon.Mastodon.status')
    def test_retrieve_post(self, mock_status):
        mock_status.return_value = {"id": "123", "content": "Test post"}
        response = retrieve_post("123")
        self.assertEqual(response["content"], "Test post")

    # Test for deleting a post
    @patch('mastodon.Mastodon.status_delete')
    def test_delete_post(self, mock_status_delete):
        delete_post("123")
        mock_status_delete.assert_called_once_with("123")

if __name__ == '__main__':
    unittest.main()
