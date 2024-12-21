import unittest
from typing import Any, Dict, Hashable, List
from unittest.mock import patch

import pandas as pd

from src.finance_reader import read_transactions_from_csv, read_transactions_from_excel


class TestFinanceReader(unittest.TestCase):
    """Тестовый класс для проверки функций чтения транзакций из CSV и Excel файлов."""

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv(self, mock_read_csv: Any) -> None:
        """Тестирование функции чтения транзакций из CSV файла.

        В данном тесте используется мок объекта pandas.read_csv для имитации
        чтения данных из CSV файла. Проверяется, что функция возвращает
        корректный список словарей, соответствующий ожидаемым данным.
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
        result: list[dict[Hashable, Any]] = read_transactions_from_csv("fake_path.csv")
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
        """Тестирование функции чтения транзакций из CSV файла с параметром nrows."""
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

        # Чтение только одной строки
        nrows = 1
        result: List[Dict[Hashable, Any]] = read_transactions_from_csv("fake_path.csv", nrows=nrows)

        # Ожидаемый результат
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

        # Проверка результата
        self.assertEqual(result, expected)

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel(self, mock_read_excel: Any) -> None:
        """Тестирование функции чтения транзакций из Excel файла.

        В этом тесте используется мок объекта pandas.read_excel для имитации
        чтения данных из Excel файла. Проверяется, что функция возвращает
        корректный список словарей, соответствующий ожидаемым данным.
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
        result: list[dict[Hashable, Any]] = read_transactions_from_excel("fake_path.xlsx")
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
        """Тестирование функции чтения транзакций из Excel файла с параметром nrows.

        Этот тест проверяет, что при использовании параметра nrows функция
        корректно загружает только указанное количество строк из Excel файла.
        В данном случае проверяется, что возвращается только первая строка.
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

        # Чтение только одной строки
        nrows = 1
        result: list[dict[Hashable, Any]] = read_transactions_from_excel("fake_path.xlsx", nrows=nrows)
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
        """Тестирование функции чтения транзакций из пустого CSV файла.

        В этом тесте проверяется, что функция возвращает пустой список,
        если CSV файл не содержит данных (т.е. он пустой).
        """
        mock_read_csv.return_value = pd.DataFrame(
            columns=["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
        )

        result: list[dict[Hashable, Any]] = read_transactions_from_csv("fake_path.csv")
        self.assertEqual(result, [])  # Проверяем, что возвращается пустой список

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_empty(self, mock_read_excel: Any) -> None:
        """Тестирование функции чтения транзакций из пустого Excel файла.

        В этом тесте проверяется, что функция возвращает пустой список,
        если Excel файл не содержит данных (т.е. он пустой).
        """
        mock_read_excel.return_value = pd.DataFrame(
            columns=["id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"]
        )

        result: list[dict[Hashable, Any]] = read_transactions_from_excel("fake_path.xlsx")
        self.assertEqual(result, [])  # Проверяем, что возвращается пустой список

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_file_not_found(self, mock_read_csv: Any) -> None:
        """Тестирование обработки ошибки при отсутствии файла CSV.

        В этом тесте проверяется, что функция корректно обрабатывает
        ситуацию, когда указанный CSV файл не найден, и выбрасывает
        исключение FileNotFoundError с соответствующим сообщением.
        """
        mock_read_csv.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError) as context:
            read_transactions_from_csv("fiction_path.csv")
        self.assertEqual(str(context.exception), "Файл 'fiction_path.csv' не найден.")

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_file_not_found(self, mock_read_excel: Any) -> None:
        """Тестирование обработки ошибки при отсутствии файла Excel.

        В этом тесте проверяется, что функция корректно обрабатывает
        ситуацию, когда указанный Excel файл не найден, и выбрасывает
        исключение FileNotFoundError с соответствующим сообщением.
        """
        mock_read_excel.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError) as context:
            read_transactions_from_excel("fiction_path.xlsx")
        self.assertEqual(str(context.exception), "Файл 'fiction_path.xlsx' не найден.")

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_value_error(self, mock_read_csv: Any) -> None:
        """Тестирование обработки ошибки формата файла CSV.

        В этом тесте проверяется, что функция корректно обрабатывает
        исключение ValueError, возникающее при попытке чтения
        некорректного формата CSV файла, и выбрасывает общее исключение
        с соответствующим сообщением.
        """
        mock_read_csv.side_effect = ValueError("Ошибка формата файла.")
        with self.assertRaises(Exception) as context:
            read_transactions_from_csv("fiction_path.csv")
        self.assertEqual(str(context.exception), "Ошибка при чтении CSV файла: Ошибка формата файла.")

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_value_error(self, mock_read_excel: Any) -> None:
        """Тестирование обработки ошибки формата файла Excel.

        В этом тесте проверяется, что функция корректно обрабатывает
        исключение ValueError, возникающее при попытке чтения
        некорректного формата Excel файла, и выбрасывает общее исключение
        с соответствующим сообщением.
        """
        mock_read_excel.side_effect = ValueError("Ошибка формата файла.")
        with self.assertRaises(Exception) as context:
            read_transactions_from_excel("fiction_path.xlsx")
        self.assertEqual(str(context.exception), "Ошибка при чтении Excel файла: Ошибка формата файла.")

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_general_exception(self, mock_read_csv: Any) -> None:
        """Тестирование обработки общего исключения при чтении CSV.

        В этом тесте проверяется, что функция корректно обрабатывает
        любые общие исключения, возникающие во время чтения CSV файла,
        и выбрасывает общее исключение с соответствующим сообщением.
        """
        mock_read_csv.side_effect = Exception("Общая ошибка")
        with self.assertRaises(Exception) as context:
            read_transactions_from_csv("dummy_path.csv")
        self.assertEqual(str(context.exception), "Ошибка при чтении CSV файла: Общая ошибка")

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_general_exception(self, mock_read_excel: Any) -> None:
        """Тестирование обработки общего исключения при чтении Excel.

        В этом тесте проверяется, что функция корректно обрабатывает
        любые общие исключения, возникающие во время чтения Excel файла,
        и выбрасывает общее исключение с соответствующим сообщением.
        """
        mock_read_excel.side_effect = Exception("Общая ошибка")
        with self.assertRaises(Exception) as context:
            read_transactions_from_excel("dummy_path.xlsx")
        self.assertEqual(str(context.exception), "Ошибка при чтении Excel файла: Общая ошибка")
