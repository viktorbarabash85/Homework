import re
from collections import Counter


def search_operations_by_description(operations: list[dict], search_term: str) -> list[dict]:
    """
    Функция для поиска операций по описанию с использованием регулярных выражений.
    :param operations: Список словарей с данными о банковских операциях.
    :param search_term: Строка для поиска в описании операций.
    :return: Список словарей из категорий, у которых в описании есть введенное слово или строка.
    """

    sample_patterns = [
        r"перевод",
        r"открыт\s\w+",  # "открытие" с возможным продолжением
        r"закрытие\s\w+",  # "закрытие" с возможным продолжением
        r"вклад[а]?",  # "вклад" с возможным окончанием
        r"счет[а]?",  # "счет" с возможным окончанием
        r"организаци\w*",  # "организации" с возможным окончанием
    ]

    # Проверка на пустую строку
    if search_term == "":
        # raise TypeError("Необходимо ввести слово для поиска.")
        return []

    search_term = search_term.lower()
    results = []

    # Обходим все операции
    for operation in operations:  # Получаем описание и приводим к нижнему регистру
        description = operation.get("description")
        if description is None:
            continue
        description = description.lower()

        # Проверяем, есть ли совпадение с введенным словом
        if any(re.search(pattern, search_term) for pattern in sample_patterns) or search_term in description:
            if re.search(search_term, description):
                results.append(operation)  # Добавляем операцию в результаты

    return results


def count_operations_by_category(transactions: list[dict], categories: list[str]) -> dict[str, int]:
    """
    Функция для подсчета количества операций определенного типа.

    :param transactions: Список словарей с данными о банковских операциях.
    :param categories: Список категорий для подсчета транзакций по описанию. По умолчанию None.
    :return: Словарь, где ключи — это названия категорий, а значения — количество операций в каждой категории.
    """

    # Извлекаем описания операций из транзакций
    descriptions = [transaction["description"] for transaction in transactions]

    # Используем Counter для подсчета количества операций по описаниям
    description_count = Counter(descriptions)

    # Создаем словарь для хранения результатов по заданным категориям
    category_count = {category: description_count.get(category, 0) for category in categories}

    return category_count
