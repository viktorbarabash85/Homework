import os

import pandas as pd

from src.finance_reader import read_transactions_from_csv, read_transactions_from_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search_and_count import count_operations_by_category, search_operations_by_description
from src.utils import read_json_file
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Программа по работе с банковскими транзакциями.
    """

    print(f"{"_" * 40}\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")

    transactions: list[dict] = []
    sorted_transactions: list[dict] = []

    # Шаг 1: Выбор файла
    while not transactions:
        print("\nВыберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        choice = input(">>> ").strip().lower()

        if choice == "1":
            transactions = read_json_file(os.path.join("data", "operations.json"))
            print("\nДля обработки выбран JSON-файл.")
        elif choice == "2":
            transactions = read_transactions_from_csv(os.path.join("data", "transactions.csv"), delimiter=";")
            print("\nДля обработки выбран CSV-файл.")
        elif choice == "3":
            transactions = read_transactions_from_excel(os.path.join("data", "transactions_excel.xlsx"))
            print("\nДля обработки выбран XLSX-файл.")
        else:
            print("Некорректный выбор. Пожалуйста, выберите один из предложенных пунктов.")

    # Преобразование транзакций
    transactions = [
        {
            "id": t.get("id"),
            "state": t.get("state"),
            "date": t.get("date"),
            "operationAmount": {
                "amount": str(t.get("operationAmount", {}).get("amount", t.get("amount", ""))),
                "currency": {
                    "name": t.get("operationAmount", {}).get("currency", {}).get("name", t.get("currency_name", "")),
                    "code": t.get("operationAmount", {}).get("currency", {}).get("code", t.get("currency_code", "")),
                },
            },
            "description": t.get("description"),
            "from": t.get("from") if t.get("from") else "",
            "to": t.get("to") if t.get("to") else "",
        }
        for t in transactions
    ]

    # Шаг 2: Фильтрация по статусу
    valid_states = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(valid_states)}")

        state = input(">>> ").strip().upper()

        if state not in valid_states:
            print(f"Статус операции {state} недоступен. Введите один из доступных статусов.")
            continue
        else:
            break

    filtered_transactions = filter_by_state(transactions, state)
    print(f'\nОперации отфильтрованы по статусу "{state}"')

    # Шаг 3: Сортировка по дате
    if filtered_transactions:
        while True:
            print("\nОтсортировать операции по дате? Да/Нет")

            sort_choice = input(">>> ").strip().lower()

            if sort_choice == "да":
                while True:
                    print("\nОтсортировать по возрастанию или по убыванию?")

                    order = input(">>> ").strip().lower()  # ввод пользователя

                    if order == "по убыванию":
                        reverse = True
                        sorted_transactions = sort_by_date(filtered_transactions, reverse)
                        break
                    elif order == "по возрастанию":
                        reverse = False
                        sorted_transactions = sort_by_date(filtered_transactions, reverse)
                        break
                    else:
                        print("Некорректный ввод. Пожалуйста, выберите 'по возрастанию' или 'по убыванию'.")
                break

            elif sort_choice == "нет":
                sorted_transactions = filtered_transactions
                break

            else:
                print("Введен некорректный ответ. Пожалуйста, ответьте 'Да' или 'Нет'.")

    # Шаг 4: Фильтрация по валюте
    while True:
        print("\nВыводить только рублевые транзакции? Да/Нет")

        currency_choice = input(">>> ").strip().lower()

        if currency_choice == "да":
            sorted_transactions = list(filter_by_currency(sorted_transactions, "RUB"))
            break
        elif currency_choice == "нет":
            sorted_transactions = filtered_transactions
            break
        else:
            print("Введен некорректный ответ. Пожалуйста, ответьте 'Да' или 'Нет'.")

    # Шаг 5: Фильтрация по описанию
    search_term = ""
    while True:
        print("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет")

        description_filter = input(">>> ").strip().lower()

        if description_filter == "да":
            while True:
                print("\nВведите слово для поиска интересующих транзакций:")
                print("(например: перевод, открытие, закрытие, вклад, счет, организации и т.д.):")

                search_term = input(">>> ").strip().lower()

                if not search_term:
                    print("Необходимо ввести слово для поиска.")
                    continue

                filtered_transactions = search_operations_by_description(sorted_transactions, search_term)

                categories = list(set(t["description"] for t in filtered_transactions))
                count = count_operations_by_category(filtered_transactions, categories)
                sorted_transactions = filtered_transactions
                break
            break

        elif description_filter == "нет":
            filtered_transactions = sorted_transactions
            categories = list(set(t["description"] for t in filtered_transactions))
            count = count_operations_by_category(filtered_transactions, categories)
            break
        else:
            print("Введен некорректный ответ. Пожалуйста, ответьте 'Да' или 'Нет'.")

    # Шаг 6: Итоговый вывод
    print(f"{"_" * 40}\nРаспечатываю итоговый список транзакций...\n{"_" * 40}")

    if filtered_transactions:
        print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")

        if "count" in locals():
            print("\nНайдены следующие транзакции:")
            for category, category_count in count.items():
                print(f"{category}: {category_count}")

        print(f"{"_" * 40}\n")

        # Вывод информации о каждой транзакции
        for t in filtered_transactions:
            try:
                date = get_date(t["date"])
                amount = t["operationAmount"]["amount"]
                currency = t["operationAmount"]["currency"]["code"]
                masked_from = mask_account_card(str(t["from"])) if pd.notna(t["from"]) else ""
                masked_to = mask_account_card(str(t["to"])) if pd.notna(t["to"]) else ""
                description = t["description"]

                print(f"{date} {description}")
                if masked_from:  # Проверяем, есть ли значение masked_from
                    print(f"{masked_from} -> {masked_to}")
                else:
                    print(masked_to)
                print(f"Сумма: {amount} {currency}\n")

            except KeyError as e:
                print(f"Ошибка: отсутствует ключ {e} в транзакции: {t}\n")
            except Exception as e:
                print(f"Неизвестная ошибка при обработке транзакции: {e}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
