from typing import Any
from unittest.mock import patch

import pytest

from src.search_and_count import count_operations_by_category, search_operations_by_description

mock_operations: list[dict] = [
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
                    "to": "Счет 12345678901234567890",
                }
            ],
        ),
        ("закрытие", []),  # Ожидаем пустой список, что не будет найдено ни одной операции
        ("", []),  # Ожидаем пустой список, т.к. не введено слово для поиска
    ],
)
def test_search_operations_by_description(operations: list[dict], search_term: str, expected: Any) -> None:
    """
    Тестирование функции поиска операций по описанию.

    :param operations: Список операций, предоставленных фикстурой.
    :param search_term: Строка для поиска в описаниях операций.
    :param expected: Ожидаемый результат поиска.
    """
    result = search_operations_by_description(operations, search_term)
    assert result == expected  # Проверяем, совпадает ли результат с ожидаемым


@patch("src.search_and_count.search_operations_by_description")
def test_search_operations_with_mock(mock_get_operations: Any, operations: list[dict]) -> None:
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


def test_count_operations_by_category(operations: list[dict], categories: list[str]) -> None:
    """
    Тестирование функции подсчета операций по категориям.

    :param operations: Список операций, предоставленных фикстурой.
    """
    expected_count = {
        "Перевод с карты на карту": 0,
        "Открытие вклада": 1,
        "Закрытие вклада": 0,
        "Перевод организации": 2,
        "Перевод со счета на счет": 0,
    }

    result = count_operations_by_category(operations, categories)
    assert result == expected_count  # Проверяем, совпадает ли результат с ожидаемым


# Дополнительный тест для проверки работы с категориями, которых нет в транзакциях
def test_count_operations_no_matches() -> None:
    """
    Тестируем функцию count_operations_by_category, когда нет совпадений с категориями.
    Ожидаем, что все категории будут иметь значение 0.
    """

    transactions = [
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
    ]
    categories = ["Перевод организации", "Закрытие вклада", "Перевод на счет"]

    # Ожидаемый результат
    expected_result = {"Перевод организации": 0, "Закрытие вклада": 0, "Перевод на счет": 0}

    # Выполнение тестируемой функции
    result = count_operations_by_category(transactions, categories)

    # Проверка результата
    assert result == expected_result


def test_count_operations_by_category_with_empty_categories() -> None:
    """
    Тестирование функции count_operations_by_category с пустым списком категорий.
    Ожидаем, что функция вызовет ValueError.
    """
    transactions = [{"description": "Перевод организации"}]
    categories: list[str] = []

    try:
        count_operations_by_category(transactions, categories)
    except ValueError as e:
        assert str(e) == "Отсутствует описание категории."


# Дополнительный тест для проверки работы с пустыми данными
def test_count_operations_empty() -> None:
    """
    Тестируем функцию count_operations_by_category с пустым списком транзакций.
    Ожидаем, что все категории будут иметь значение 0.
    """

    transactions: list[dict] = []
    categories = ["Перевод с карты на карту", "Открытие вклада", "Перевод организации"]

    try:
        count_operations_by_category(transactions, categories)
    except ValueError as e:
        assert str(e) == "Отсутствует список транзакций."
