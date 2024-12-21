import json
import unittest
from typing import Any, List
from unittest.mock import MagicMock, mock_open, patch

from src.utils import read_json_file


class TestExternalAPI(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": "data1"}, {"transaction": "data2"}]')
    def test_read_json_file_correct(self, mock_file: MagicMock) -> None:
        """
        Тестирование корректности существующего файла
        """
        expected_data: List[dict[str, str]] = [{"transaction": "data1"}, {"transaction": "data2"}]
        result: Any = read_json_file("fake_path.json")
        self.assertEqual(result, expected_data)
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_read_json_file_invalid_connect(self, mock_file: MagicMock) -> None:
        """
        Тестирование корректности файла при нарушенном соединении
        """
        result: Any = read_json_file("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_json_file_empty(self, mock_file: MagicMock) -> None:
        """
        Тестирование работоспособности при пустом файле
        """
        result: Any = read_json_file("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_json_file_not_found(self, mock_file: MagicMock) -> None:
        """
        Тестирование работоспособности при отсутствующем json-файле
        """
        result: Any = read_json_file("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": "data"}')
    @patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
    def test_read_json_file_decode_error(self, mock_json_load: MagicMock, mock_file: MagicMock) -> None:
        """
        Тестирование декодирования чтения json-файла с ошибкой
        """
        result: Any = read_json_file("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")
        mock_json_load.assert_called_once()
