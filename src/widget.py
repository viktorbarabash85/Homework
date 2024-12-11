from typing import Any, Union

from src.masks import get_mask_account, get_mask_card_number

# import datetime


def mask_account_card(card_info: dict | str) -> Any:
    """
    Маскирует информацию о карте или счете с применением функций из masks.py
    """
    # Проверка на пустое значение или неверный тип
    if not isinstance(card_info, str) or card_info.strip() == "":
        return "Неизвестный тип карты или данные отсутствуют"

    # Маскируем номер карты с добавлением типа карты
    card_types = [
        "МИР",
        "Visa Classic",
        "Visa Gold",
        "Visa Platinum",
        "Visa",
        "Maestro",
        "MasterCard",
        "Discover",
        "American Express",
    ]
    for card_type in card_types:
        if card_type.lower() in card_info.lower():
            card_number = card_info.split()[-1]
            return f"{card_type} {get_mask_card_number(str(card_number))}"

    # Проверка на наличие слова "Счет"
    if "Счет" in card_info:
        account_number = card_info.split()[-1]
        return f"{card_info.split()[0]} {get_mask_account(str(account_number))}"

    return "Неизвестный тип карты или данные отсутствуют"


def get_date(date_str: Union[str]) -> Any:
    """
    Конвертирует строку с датой в формат "ДД.ММ.ГГГГ"
    Вход: "2024-03-11T02:26:18.671407Z"
    Выход: "11.03.2024"
    """
    error_message = "Введен некорректный или нестандартный формат даты"

    if not date_str:
        return error_message

    # Удаляем 'Z' в конце строки, если он присутствует
    if date_str.endswith("Z"):
        date_str = date_str[:-1]

    parts = date_str.split("T")
    if len(parts) != 2:
        return error_message

    date_parts = parts[0].split("-")
    time_parts = parts[1].split(":")

    # Учитываем, что время может содержать миллисекунды
    seconds_parts = time_parts[2].split(".")

    if len(date_parts) != 3 or len(time_parts) < 3 or len(seconds_parts) < 1:
        return error_message

    year, month, day = date_parts
    hours, minutes = time_parts[0], time_parts[1]
    seconds = seconds_parts[0]  # Берем только секунды, игнорируем миллисекунды

    if (
        not (year.isdigit() and 1900 <= int(year) <= 2100)
        or not (month.isdigit() and 1 <= int(month) <= 12)
        or not (day.isdigit() and 1 <= int(day) <= 31)
        or not (hours.isdigit() and 0 <= int(hours) <= 23)
        or not (minutes.isdigit() and 0 <= int(minutes) <= 59)
        or not (seconds.isdigit() and 0 <= int(seconds) <= 59)
    ):
        return error_message

    result = f"{day}.{month}.{year}"
    return result


# """ Реализация функции для конвертирования строки с датой
#     в формат "ДД.ММ.ГГГГ" с помощью встроенного модуля datetime """
# def get_date(date_str: Union[str]) -> Union[str]:
#     """
#     Конвертирует строку с датой в формат "ДД.ММ.ГГГГ".
#     Вход: "2024-03-11T02:26:18.671407"
#     Выход: "11.03.2024"
#     """
#     dt = datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
#     return dt.strftime("%d.%m.%Y")
