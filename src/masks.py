from typing import Union

from src.file_logger import setup_logger

# Настраиваем логгер для модуля masks.
logger = setup_logger("masks", "masks")


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """
    Маскирует номер банковской карты

    :param card_number: принимает на вход номер карты
    :return: возвращает замаскированный номер карты в формате XXXX XX** **** XXXX
    """
    # Преобразуем номер карты в строку и удаляем пробелы
    card_number_str = str(card_number).strip()

    # Убираем пробелы и проверяем, что длина номера 16 и состоит только из цифр
    card_number_str = card_number_str.replace(" ", "")

    if len(card_number_str) == 16 and card_number_str.isdigit():
        masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        logger.info("Успешно замаскирован номер карты.")
        return masked_number
    else:
        logger.error("Некорректно введен номер карты.")
        return "Некорректно введен номер карты"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """
    Маскирует номер банковского счета

    :param account_number: принимает на вход номер банковского счета
    :return: замаскированный номер банковского счета в формате **XXXX
    """
    account_number_str = str(account_number)
    if account_number_str.isdigit() and int(account_number) != 0 and len(account_number_str) == 20:
        masked_account = "*" * 2 + account_number_str[-4:]
        logger.info("Успешно замаскирован номер счета.")
        return masked_account
    else:
        logger.error("Некорректно введен номер счета.")
        return "Некорректно введен номер счета"
