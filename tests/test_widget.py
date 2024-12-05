import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_correct(card_info_correct: str) -> None:
    """
    Тестирование корректности маскирования информации о карте или счете.

    :param card_info_correct: Ожидаемый результат маскирования корректной информации о карте.
    """
    assert mask_account_card("Visa Platinum 7000792289606361") == card_info_correct


def test_mask_account_card_incorrect(card_info_incorrect: str) -> None:
    """
    Тестирование некорректности маскирования информации о карте или счете.

    :param card_info_incorrect: Ожидаемый результат маскирования некорректной информации о карте.
    """
    assert mask_account_card("Unknown Card 7000792289606361") == card_info_incorrect


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Classic 4000000000000002", "Visa Classic 4000 00** **** 0002"),
        ("Maestro 5000000000000004", "Maestro 5000 00** **** 0004"),
        ("MasterCard 5100000000000004", "MasterCard 5100 00** **** 0004"),
        ("Unknown Card 7000792289606361", "Неизвестный тип карты или данные отсутствуют"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Неизвестный тип карты или данные отсутствуют"),
    ]
)
def test_mask_account_card(value: str, expected: str) -> None:
    """
    Тестирование маскирования информации о карте или счете с различными входными данными.

    :param value: Исходная строка с информацией о карте или счете.
    :param expected: Ожидаемый результат маскирования.
    """
    assert mask_account_card(value) == expected


def test_get_date_correct(date_str_correct: str) -> None:
    """
    Применение фикстур. Тестирование корректности конвертации строки с датой.

    :param date_str_correct: Ожидаемая строка с корректной датой после конвертации.
    """
    assert get_date("2024-03-11T02:26:18.671407") == date_str_correct


def test_get_date_incorrect(date_str_incorrect: str) -> None:
    """
    Применение фикстур. Тестирование некорректности конвертации строки с датой.

    :param date_str_incorrect: Ожидаемый результат при некорректной строке с датой.
    """
    assert get_date("") == date_str_incorrect


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2023-02-20T12:00:00.000000", "20.02.2023"),
        ("2025-03-11 02:26:18.671407", "Введен некорректный или нестандартный формат даты"),
        ("", "Введен некорректный или нестандартный формат даты"),
        ("2024/03T02:26:18T671407", "Введен некорректный или нестандартный формат даты"),
        ("2101-13-33T02:26:18T672407", "Введен некорректный или нестандартный формат даты"),
        ("2024.03.12T02:60:18.671407", "Введен некорректный или нестандартный формат даты")
    ]
)
def test_get_date(value: str, expected: str) -> None:
    """
    Тестирование конвертации строки с датой с различными входными данными.

    :param value: Исходная строка с датой для конвертации.
    :param expected: Ожидаемый результат конвертации.
    """
    assert get_date(value) == expected
