import unittest
from typing import Any, Dict, List
from unittest.mock import patch

import pandas as pd

from src.finance_reader import read_transactions_from_csv, read_transactions_from_excel


class TestFinanceReader(unittest.TestCase):
    """Тестовый класс для проверки функций чтения транзакций из CSV и Excel файлов."""

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv(self, mock_read_csv: Any) -> None:
        """
        Тестирование функции чтения транзакций из CSV файла.

        :param mock_read_csv: Мок объекта для функции pandas.read_csv.
        """
        mock_read_csv.return_value = pd.DataFrame(
            {
                "id": [1],
                "state": ["EXECUTED"],
                "date": ["2023-01-01"],
                "amount": [100],
                "currency_name": ["Dollar"],
                "currency_code": ["USD"],
                "from": ["Счет 58803664561298323391"],
                "to": ["Счет 39745660563456619397"],
                "description": ["Перевод организации"],
            }
        )
        result: List[Dict[str, Any]] = read_transactions_from_csv("fake_path.csv")
        expected: List[Dict[str, Any]] = [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-01-01",
                "amount": 100,
                "currency_name": "Dollar",
                "currency_code": "USD",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        self.assertEqual(result, expected)

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_with_nrows(self, mock_read_csv: Any) -> None:
        """
        Тестирование функции чтения транзакций из CSV файла с параметром nrows.

        :param mock_read_csv: Мок объекта для функции pandas.read_csv.
        """
        mock_read_csv.return_value = pd.DataFrame(
            {
                "id": [1, 2],
                "state": ["completed", "pending"],
                "date": ["2023-01-01", "2023-01-02"],
                "amount": [100, 200],
                "currency_name": ["USD", "USD"],
                "currency_code": ["USD", "USD"],
                "from": ["Alice", "Bob"],
                "to": ["Bob", "Charlie"],
                "description": ["Payment", "Transfer"],
            }
        )

        result: List[Dict[str, Any]] = read_transactions_from_csv("fake_path.csv", nrows=1)
        expected: List[Dict[str, Any]] = [
            {
                "id": 1,
                "state": "completed",
                "date": "2023-01-01",
                "amount": 100,
                "currency_name": "USD",
                "currency_code": "USD",
                "from": "Alice",
                "to": "Bob",
                "description": "Payment",
            }
        ]
        self.assertEqual(result, expected)

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel(self, mock_read_excel: Any) -> None:
        """
        Тестирование функции чтения транзакций из Excel файла.

        :param mock_read_excel: Мок объекта для функции pandas.read_excel.
        """
        mock_read_excel.return_value = pd.DataFrame(
            {
                "id": [1],
                "state": ["EXECUTED"],
                "date": ["2023-01-01"],
                "amount": [100],
                "currency_name": ["Dollar"],
                "currency_code": ["USD"],
                "from": ["Счет 58803664561298323391"],
                "to": ["Счет 39745660563456619397"],
                "description": ["Перевод организации"],
            }
        )
        result: List[Dict[str, Any]] = read_transactions_from_excel("fake_path.xlsx")
        expected: List[Dict[str, Any]] = [
            {
                "id": 1,
                "state": "EXECUTED",
                "date": "2023-01-01",
                "amount": 100,
                "currency_name": "Dollar",
                "currency_code": "USD",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        self.assertEqual(result, expected)

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_with_nrows(self, mock_read_excel: Any) -> None:
        """
        Тестирование функции чтения транзакций из Excel файла с параметром nrows.

        :param mock_read_excel: Мок объекта для функции pandas.read_excel.
        """
        mock_read_excel.return_value = pd.DataFrame(
            {
                "id": [1, 2],
                "state": ["completed", "pending"],
                "date": ["2023-01-01", "2023-01-02"],
                "amount": [100, 200],
                "currency_name": ["USD", "USD"],
                "currency_code": ["USD", "USD"],
                "from": ["Alice", "Bob"],
                "to": ["Bob", "Charlie"],
                "description": ["Payment", "Transfer"],
            }
        )

        result: List[Dict[str, Any]] = read_transactions_from_excel("fake_path.xlsx", nrows=1)
        expected: List[Dict[str, Any]] = [
            {
                "id": 1,
                "state": "completed",
                "date": "2023-01-01",
                "amount": 100,
                "currency_name": "USD",
                "currency_code": "USD",
                "from": "Alice",
                "to": "Bob",
                "description": "Payment",
            }
        ]
        self.assertEqual(result, expected)

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_empty(self, mock_read_csv: Any) -> None:
        """
        Тестирование функции чтения транзакций из пустого CSV файла.

        :param mock_read_csv: Мок объекта для функции pandas.read_csv.
        """
        mock_read_csv.return_value = pd.DataFrame(
            columns=["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
        )

        result: List[Dict[str, Any]] = read_transactions_from_csv("fake_path.csv")
        self.assertEqual(result, [])  # Проверяем, что возвращается пустой список

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_empty(self, mock_read_excel: Any) -> None:
        """
        Тестирование функции чтения транзакций из пустого Excel файла.

        :param mock_read_excel: Мок объекта для функции pandas.read_excel.
        """
        mock_read_excel.return_value = pd.DataFrame(
            columns=["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
        )

        result: List[Dict[str, Any]] = read_transactions_from_excel("fake_path.xlsx")
        self.assertEqual(result, [])  # Проверяем, что возвращается пустой список

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_file_not_found(self, mock_read_csv: Any) -> None:
        """
        Тестирование обработки ошибки при отсутствии файла CSV.

        :param mock_read_csv: Мок объекта для функции pandas.read_csv.
        """
        mock_read_csv.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError) as context:
            read_transactions_from_csv("fiction_path.csv")
        self.assertEqual(str(context.exception), "Файл 'fiction_path.csv' не найден.")

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_file_not_found(self, mock_read_excel: Any) -> None:
        """
        Тестирование обработки ошибки при отсутствии файла Excel.

        :param mock_read_excel: Мок объекта для функции pandas.read_excel.
        """
        mock_read_excel.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError) as context:
            read_transactions_from_excel("fiction_path.xlsx")
        self.assertEqual(str(context.exception), "Файл 'fiction_path.xlsx' не найден.")

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_value_error(self, mock_read_csv: Any) -> None:
        """
        Тестирование обработки ошибки формата файла CSV.

        :param mock_read_csv: Мок объекта для функции pandas.read_csv.
        """
        mock_read_csv.side_effect = ValueError("Ошибка формата файла.")
        with self.assertRaises(Exception) as context:
            read_transactions_from_csv("fiction_path.csv")
        self.assertEqual(str(context.exception), "Ошибка при чтении CSV файла: Ошибка формата файла.")

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_value_error(self, mock_read_excel: Any) -> None:
        """
        Тестирование обработки ошибки формата файла Excel.

        :param mock_read_excel: Мок объекта для функции pandas.read_excel.
        """
        mock_read_excel.side_effect = ValueError("Ошибка формата файла.")
        with self.assertRaises(Exception) as context:
            read_transactions_from_excel("fiction_path.xlsx")
        self.assertEqual(str(context.exception), "Ошибка при чтении Excel файла: Ошибка формата файла.")

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_general_exception(self, mock_read_csv: Any) -> None:
        """
        Тестирование обработки общего исключения при чтении CSV.

        :param mock_read_csv: Мок объекта для функции pandas.read_csv.
        """
        mock_read_csv.side_effect = Exception("Общая ошибка")
        with self.assertRaises(Exception) as context:
            read_transactions_from_csv("dummy_path.csv")
        self.assertEqual(str(context.exception), "Ошибка при чтении CSV файла: Общая ошибка")

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_general_exception(self, mock_read_excel: Any) -> None:
        """
        Тестирование обработки общего исключения при чтении Excel.

        :param mock_read_excel: Мок объекта для функции pandas.read_excel.
        """
        mock_read_excel.side_effect = Exception("Общая ошибка")
        with self.assertRaises(Exception) as context:
            read_transactions_from_excel("dummy_path.xlsx")
        self.assertEqual(str(context.exception), "Ошибка при чтении Excel файла: Общая ошибка")
