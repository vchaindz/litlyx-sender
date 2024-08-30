import unittest
from unittest.mock import patch, MagicMock
from litlyx_sender import LitLyxSender

class TestLitLyxSender(unittest.TestCase):
    def setUp(self):
        self.sender = LitLyxSender()

    @patch('litlyx_sender.sender.requests.post')
    def test_send_event(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = self.sender.send_event(name="test_event", metadata={"test": "value"})

        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once()

    @patch('litlyx_sender.sender.LitLyxSender.send_event')
    def test_event_decorator(self, mock_send_event):
        @self.sender.event_decorator(name="decorated_event", metadata={"decorated": True})
        def example_function():
            return "Function executed"

        result = example_function()

        self.assertEqual(result, "Function executed")
        mock_send_event.assert_called_once_with(None, "decorated_event", {"decorated": True}, None, None)

if __name__ == '__main__':
    unittest.main()