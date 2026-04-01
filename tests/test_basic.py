import unittest
from unittest.mock import patch

from main import main


class TestMain(unittest.TestCase):
    @patch("builtins.print")
    def test_main_prints_greeting(self, mock_print: object) -> None:
        main()
        mock_print.assert_called_once_with("Hello from uncertainty-aware-rag!")


if __name__ == "__main__":
    unittest.main()
