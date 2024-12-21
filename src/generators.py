# Модуль generators содержит функции для работы с массивами транзакций

from typing import Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator[dict]:
    """
    Функция, которая возвращает итератор отфильтрованных транзакций с поочередной выдачей по выбранной валюте.

    :param transactions: Принимает список словарей, представляющих транзакции
    :param currency_code: указывает тит валюты USD)
    :return: возвращает итератор, который поочередно выдает транзакции по заданной валюте
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction  # Возвращаем транзакцию, если она соответствует валюте


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """
    Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров.
    """
    for num in range(start, stop + 1):
        number = "0" * (16 - len(str(num))) + str(num)

        string_to_return = ""
        block_counter = 0

        for digit in number:
            block_counter += 1
            if block_counter <= 4:
                string_to_return += digit
            else:
                string_to_return += " " + digit
                block_counter = 1

        yield string_to_return
