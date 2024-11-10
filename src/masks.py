from typing import Union

from src.file_logger import setup_logger

# Настраиваем логгер для модуля masks.
logger = setup_logger("masks", "masks")


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Маскирует номер банковской карты"""
    card_number_str = str(card_number)
    if card_number_str.isdigit() and int(card_number) != 0 and len(card_number_str) == 16:
        masked_number = " ".join([card_number_str[:4], card_number_str[4:6] + "*" * 2, "*" * 4, card_number_str[-4:]])
        logger.info("Успешно замаскирован номер карты.")
        return masked_number
    else:
        logger.error("Некорректно введен номер карты.")
        return "Некорректно введен номер карты"


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Маскирует номер банковского счета"""
    account_number_str = str(account_number)
    if account_number_str.isdigit() and int(account_number) != 0 and len(account_number_str) == 20:
        masked_account = "*" * 2 + account_number_str[-4:]
        logger.info("Успешно замаскирован номер счета.")
        return masked_account
    else:
        logger.error("Некорректно введен номер счета.")
        return "Некорректно введен номер счета"
