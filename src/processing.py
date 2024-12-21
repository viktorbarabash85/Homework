from datetime import datetime

from src.widget import get_date


def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция фильтрует список словарей по значению ключа state.

    :param transactions: Список словарей с данными о банковских операциях.
    :param state: (str, optional) Значение для ключа state (по умолчанию 'EXECUTED').
    :return list[dict]: Список словарей, у которых ключ state соответствует указанному значению.
    Исключения:
    ValueError: Если state не является одним из допустимых значений.
    """
    valid_states = ("EXECUTED", "CANCELED", "PENDING")
    if state not in valid_states:
        raise ValueError(f'Ошибка. Статус "{state}" введен некорректно. Допустимые статусы {valid_states}')
    return [transaction for transaction in transactions if transaction.get("state") == state]


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список транзакций по дате.

    :param transactions: список транзакций
    :param reverse: если True, сортирует по убыванию
    :return: отсортированный список транзакций или сообщение об ошибке
    """

    for transaction in transactions:

        # Проверка формата даты функцией get_date из модуля widget.py
        date_str = get_date(str(transaction["date"]))
        if date_str.startswith("Введен некорректный или нестандартный формат даты"):
            raise ValueError("Введен некорректный или нестандартный формат даты")

    # Сортируем транзакции по дате
    return sorted(transactions, key=lambda x: datetime.fromisoformat(x["date"][:-1]), reverse=reverse)
