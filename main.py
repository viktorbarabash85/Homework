import os
from typing import Any, List

from src.finance_reader import read_transactions_from_csv, read_transactions_from_excel
from src.processing import filter_by_state, sort_by_date
from src.search_and_count import count_operations_by_category, search_operations_by_description
from src.utils import read_json_file
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Программа по работе с банковскими транзакциями.
    """
    while True:
        print("_" * 40)
        print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")

        transactions: Any = []  # Добавлено аннотирование типа
        sorted_transactions: Any = []  # Добавлено аннотирование типа

        # Выбор JSON-, CSV- или XLSX-файла с транзакциями для дальнейшей работы с ним
        while not transactions:
            print("\nВыберите необходимый пункт меню:")
            print("1. Получить информацию о транзакциях из JSON-файла")
            print("2. Получить информацию о транзакциях из CSV-файла")
            print("3. Получить информацию о транзакциях из XLSX-файла")

            choice: str = input(">>> ")

            if choice == "1":
                transactions = read_json_file(os.path.join("data", "operations.json"))
                print("Для обработки выбран JSON-файл.")
            elif choice == "2":
                transactions = read_transactions_from_csv(os.path.join("data", "transactions.csv"), delimiter=";")
                print("Для обработки выбран CSV-файл.")
            elif choice == "3":
                transactions = read_transactions_from_excel(os.path.join("data", "transactions_excel.xlsx"))
                print("Для обработки выбран XLSX-файл.")
            else:
                print("Некорректный выбор. Пожалуйста, выберите один из предложенных вариантов 1/2/3.")

        # Преобразование транзакций в нужный формат из-за отличия в последовательности и наименовании ключей
        transactions = [
            {
                "id": t.get("id"),
                "state": t.get("state"),
                "date": t.get("date"),
                "operationAmount": {
                    "amount": str(t.get("operationAmount", {}).get("amount", t.get("amount", ""))),
                    "currency": {
                        "name": t.get("operationAmount", {})
                        .get("currency", {})
                        .get("name", t.get("currency_name", "")),
                        "code": t.get("operationAmount", {})
                        .get("currency", {})
                        .get("code", t.get("currency_code", "")),
                    },
                },
                "description": t.get("description"),
                "from": t.get("from"),
                "to": t.get("to"),
            }
            for t in transactions
        ]

        # Проверка корректности формата данных транзакций
        if not isinstance(transactions, list) or not all(isinstance(t, dict) for t in transactions):
            print("Ошибка: данные транзакций имеют неверный формат.")
            return

        # Фильтрация транзакций по статусу
        valid_states: List[str] = ["EXECUTED", "CANCELED", "PENDING"]

        while True:
            state: str = input(
                f"\nВведите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: "
                f"{', '.join(valid_states)}\n>>> "
            )

            if state == "":
                print('Статус не введен. По умолчанию выбран статус "EXECUTED".')
                state = "EXECUTED"

            # Применяем функцию filter_by_state
            filtered_transactions: Any = filter_by_state(transactions, state.upper())

            if isinstance(filtered_transactions, str):
                print(filtered_transactions)
            else:
                print(f'\nОперации отфильтрованы по статусу "{state.upper()}"')
                break

        # Фильтрация транзакций по дате
        if filtered_transactions:
            while True:
                sort_choice: str = input("\nОтсортировать операции по дате? Да/Нет\n>>> ").lower()

                if sort_choice in ["да"]:
                    while True:
                        order: str = input("\nОтсортировать по возрастанию или по убыванию?\n>>> ")
                        if order.lower() == "по убыванию":
                            reverse: bool = True

                            # Применяем функцию sort_by_date для сортировки транзакций по дате
                            sorted_transactions = sort_by_date(filtered_transactions, reverse)
                            break
                        elif order.lower() == "по возрастанию":
                            reverse = False
                            # Применяем функцию sort_by_date для сортировки транзакций по дате
                            sorted_transactions = sort_by_date(filtered_transactions, reverse)
                            break
                        else:
                            print("Некорректный ввод. Пожалуйста, выберите 'по возрастанию' или 'по убыванию'.")
                    break
                elif sort_choice in ["нет"]:
                    sorted_transactions = filtered_transactions
                    break
                else:
                    print("Введен некорректный ответ. Пожалуйста, ответьте 'Да' или 'Нет'.")

        # Фильтрация по валюте
        while True:
            currency_choice: str = input("\nВыводить только рублевые транзакции? Да/Нет\n>>> ").lower()
            if currency_choice in ["да"]:
                sorted_transactions = [
                    t for t in sorted_transactions if t["operationAmount"]["currency"]["code"] == "RUB"
                ]
                break
            elif currency_choice in ["нет"]:
                break
            else:
                print("Введен некорректный ответ. Пожалуйста, ответьте 'Да' или 'Нет'.")

        # Фильтрация по описанию транзакций
        search_term: str = ""
        while True:
            description_filter: str = input(
                "\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n>>> "
            ).lower()

            if description_filter in ["да"]:
                while True:
                    search_term = input(
                        "\nВведите слово для поиска в описании"
                        "\n(например: перевод, открытие, закрытие, вклад, счет, организации и т.д.): "
                        "\n>>> "
                    ).strip()

                    # Применяем функцию search_operations_by_description для поиска операций по описанию
                    filtered_transactions = search_operations_by_description(sorted_transactions, search_term)

                    # Применяем функцию count_operations_by_category для подсчета операций по категориям
                    count = count_operations_by_category(filtered_transactions, {})
                    sorted_transactions = filtered_transactions
                    break
                break
            elif description_filter in ["нет"]:
                filtered_transactions = sorted_transactions
                count = count_operations_by_category(filtered_transactions, {})
                break
            else:
                print("Введен некорректный ответ. Пожалуйста, ответьте 'Да' или 'Нет'.")

        print("_" * 40)
        print("Распечатываю итоговый список транзакций...")
        print("_" * 40)

        # Выводим информацию по категориям, если она была подсчитана
        if filtered_transactions:
            print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")

            if "count" in locals():
                print("\nНайдены следующие транзакции:")
                for category, category_count in count.items():
                    print(f"{category}: {category_count}")

            print("_" * 40)
            print()

            # Вывод информации о каждой транзакции
            for transaction in filtered_transactions:
                try:
                    # Применяем функцию get_date для форматирования даты
                    date = get_date(transaction["date"])

                    amount = transaction["operationAmount"]["amount"]
                    currency = transaction["operationAmount"]["currency"]["code"]

                    # Применяем функцию mask_account_card для маскирования данных отправителя
                    masked_from = mask_account_card(transaction["from"])

                    # Применяем функцию mask_account_card для маскирования данных получателя
                    masked_to = mask_account_card(transaction["to"])
                    description = transaction["description"]

                    print(f"{date} {description}")
                    print(f"{masked_from} -> {masked_to}")
                    print(f"Сумма: {amount} {currency}\n")
                except KeyError as e:
                    print(f"Ошибка: отсутствует ключ {e} в транзакции: {transaction}")
                except Exception as e:  # Обработка других ошибок
                    print(f"Неизвестная ошибка при обработке транзакции: {e}")
        else:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")

        # Запрос на повторное использование программы
        while True:
            print("_" * 40)
            repeat_choice: str = input(
                "Желаете еще раз повторить работу с банковскими транзакциями? Да/Нет" "\n>>> "
            ).lower()
            if repeat_choice in ["да"]:
                print("_" * 40)
                print("Перезапускаем программу...")
                break
            elif repeat_choice in ["нет"]:
                print("Спасибо за использование программы. До свидания!")
                print("_" * 40)
                return
            else:
                print("Некорректный ввод. Пожалуйста, ответьте 'Да' или 'Нет'.")


if __name__ == "__main__":
    main()
