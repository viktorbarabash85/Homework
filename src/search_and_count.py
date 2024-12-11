import re
from collections import Counter
from typing import Any, Dict, List, Union


def search_operations_by_description(
    operations: List[Dict[str, Any]], search_term: str
) -> Union[str, List[Dict[str, Any]]]:
    """
    Функция для поиска операций по описанию с использованием регулярных выражений.
    :param operations: Список словарей с данными о банковских операциях.
    :param search_term: Строка для поиска в описании операций.
    :return: Список словарей из категорий, у которых в описании есть введенное слово или строка.
    """

    # Проверка на пустую строку
    search_term = search_term.lower()
    results = []

    sample_patterns = [
        r"перевод",
        r"открыт\s\w+",  # "открытие" с возможным продолжением
        r"закрытие\s\w+",  # "закрытие" с возможным продолжением
        r"вклад[а]?",  # "вклад" с возможным окончанием
        r"счет[а]?",  # "счет" с возможным окончанием
        r"организаци\w*",  # "организации" с возможным окончанием
    ]

    if not search_term:
        return "Необходимо ввести слово для поиска."

    # Обходим все операции
    for operation in operations:
        description = operation.get("description", "").lower()  # Получаем описание и приводим к нижнему регистру

        # Проверяем, есть ли совпадение с введенным словом
        if any(re.search(pattern, search_term) for pattern in sample_patterns) or search_term in description:
            if re.search(search_term, description):
                results.append(operation)  # Добавляем операцию в результаты

    return results


def count_operations_by_category(operations: list[Any], category_count: dict) -> dict:
    """
    Функция для подсчета количества операций по категориям.

    :param operations: Список словарей с данными о банковских операциях.
    :param category_count: Словарь для подсчета транзакций по описанию (по умолчанию пустой словарь).
    :return: Словарь, где ключи — это названия категорий, а значения — количество операций в каждой категории.
    """
    # Инициализация словаря для подсчета категорий, если он не передан
    if category_count is None:
        category_count = Counter()

    # Обходим все операции
    for operation in operations:
        description = operation.get("description", "Описание отсутствует")  # Используем значение по умолчанию

        # Проверяем, существует ли категория в словаре, если нет, инициализируем ее
        if description not in category_count:
            category_count[description] = 0

        # Увеличиваем счетчик для данной категории
        category_count[description] += 1

    return dict(category_count)
