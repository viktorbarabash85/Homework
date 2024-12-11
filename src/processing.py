from datetime import datetime
from typing import Any, Union

from src.widget import get_date


def filter_by_state(transactions: list[Any], state: str = "EXECUTED") -> str | list[Any]:
    """
    Функция фильтрует список словарей по значению ключа state.

    Вход:
    transactions (list): Список словарей с данными о банковских операциях.
    state (str, optional): Значение для ключа state (по умолчанию 'EXECUTED').

    Выход:
    str: Сообщение, если статус не введен или информация отсутствует.
    list: Новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
    """
    # Проверяем, был ли введен статус. Если статус None или пустая строка, возвращаем сообщение.
    if state is None or state.strip() == "":
        return "Статус не введен. По умолчанию выбран статус 'EXECUTED'."

    # Фильтруем список transactions, оставляя только транзакции со значением ключа "state" с заданным статусом.
    filtered_transactions = [transaction for transaction in transactions if transaction.get("state") == state]

    if not filtered_transactions:
        return "Информация отсутствует или некорректно введен запрашиваемый статус"

    return filtered_transactions


def sort_by_date(transactions: list, reverse: bool = True) -> Union[str, list]:
    """
    Сортирует список транзакций по дате.

    :param transactions: список транзакций
    :param reverse: если True, сортирует по убыванию
    :return: отсортированный список транзакций или сообщение об ошибке
    """
    # Проверяем, что все элементы - это словари
    if not all(isinstance(transaction, dict) for transaction in transactions):
        raise ValueError("Все элементы должны быть словарями.")

    for transaction in transactions:
        date_str = get_date(str(transaction["date"]))
        if date_str.startswith("Введен некорректный или нестандартный формат даты"):
            return "Введен некорректный или нестандартный формат даты"

    # Сортируем транзакции по дате
    result = sorted(transactions, key=lambda x: datetime.fromisoformat(x["date"][:-1]), reverse=reverse)
    return result
