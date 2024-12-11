from typing import Any, Dict, List
from unittest.mock import patch

import pytest

from src.search_and_count import count_operations_by_category, search_operations_by_description

mock_operations: List[Dict[str, Any]] = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 12345678,
        "state": "EXECUTED",
        "date": "2020-01-01T12:00:00",
        "operationAmount": {"amount": "1000.00", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Открытие вклада",
        "from": "",
        "to": "Счет 12345678901234567890",
    },
]


@pytest.mark.parametrize(
    "search_term, expected",
    [
        (
            "перевод",
            [  # Ожидаем, что будут найдены операции с описанием "Перевод организации"
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                },
            ],
        ),
        (
            "открытие",
            [  # Ожидаем, что будет найдена операция с описанием "Открытие вклада"
                {
                    "id": 12345678,
                    "state": "EXECUTED",
                    "date": "2020-01-01T12:00:00",
                    "operationAmount": {"amount": "1000.00", "currency": {"name": "EUR", "code": "EUR"}},
                    "description": "Открытие вклада",
                    "from": "",
                    "to": "Счет 12345678901234567890",
                }
            ],
        ),
        ("закрытие", []),  # Ожидаем, что не будет найдено ни одной операции
        ("", "Необходимо ввести слово для поиска."),  # Ожидаем сообщение об ошибке при пустом запросе
    ],
)
def test_search_operations_by_description(operations: List[Dict[str, Any]], search_term: str, expected: Any) -> None:
    """
    Тестирование функции поиска операций по описанию.

    :param operations: Список операций, предоставленных фикстурой.
    :param search_term: Строка для поиска в описаниях операций.
    :param expected: Ожидаемый результат поиска.
    """
    result = search_operations_by_description(operations, search_term)
    assert result == expected  # Проверяем, совпадает ли результат с ожидаемым


def test_count_operations_by_category(operations: List[Dict[str, Any]]) -> None:
    """
    Тестирование функции подсчета операций по категориям.

    :param operations: Список операций, предоставленных фикстурой.
    """
    expected_count: Dict[str, int] = {
        "Перевод организации": 2,  # Ожидаем, что будет 2 операции с этой категорией
        "Открытие вклада": 1,  # Ожидаем, что будет 1 операция с этой категорией
    }

    result = count_operations_by_category(operations, {})
    assert result == expected_count  # Проверяем, совпадает ли результат с ожидаемым


@patch("src.search_and_count.search_operations_by_description")
def test_search_operations_with_mock(mock_get_operations, operations: List[Dict[str, Any]]) -> None:
    """
    Тестирование функции поиска операций с использованием mock.

    :param mock_get_operations: Имитация функции получения операций.
    """
    # Настраиваем mock, чтобы он возвращал наши тестовые данные
    mock_get_operations.return_value = mock_operations

    # Теперь вызываем функцию, которая использует get_operations
    operations = mock_get_operations()  # Получаем операции через mock
    search_term = "перевод"
    expected = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]

    result = search_operations_by_description(operations, search_term)
    assert result == expected  # Проверяем, совпадает ли результат с ожидаемым


@patch("src.search_and_count.count_operations_by_category")
def test_count_operations_with_mock(mock_get_operations, operations: List[Dict[str, Any]]) -> None:
    """
    Тестирование функции подсчета операций с использованием mock.

    :param mock_get_operations: Имитация функции получения операций.
    """
    # Настраиваем mock, чтобы он возвращал наши тестовые данные
    mock_get_operations.return_value = mock_operations

    # Теперь вызываем функцию, которая использует get_operations
    operations = mock_get_operations()  # Получаем операции через mock
    expected_count: Dict[str, int] = {
        "Перевод организации": 2,  # Ожидаем, что будет 2 операции с этой категорией
        "Открытие вклада": 1,  # Ожидаем, что будет 1 операция с этой категорией
    }

    result = count_operations_by_category(operations, {})
    assert result == expected_count  # Проверяем, совпадает ли результат с ожидаемым
