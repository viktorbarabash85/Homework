import os
from typing import List, Dict, Union  # Убедитесь, что вы импортируете необходимые типы
from src.utils import read_json_file  # Импорт функции для чтения данных из JSON-файлов
from src.finance_reader import read_transactions_from_csv, read_transactions_from_excel  # Импорт функций для чтения транзакций из CSV и Excel
from src.processing import filter_by_state, sort_by_date  # Импорт функций для фильтрации и сортировки транзакций
from src.widget import get_date, mask_account_card  # Импорт функций для форматирования даты и маскирования данных карт и счетов
from src.search_and_count import search_operations_by_description, count_operations_by_category  # Импорт функций для поиска и подсчета операций

def main():
    """
    Программа по работе с банковскими транзакциями
    """
    while True:
        print("_" * 40)
        print("\nПривет! Добро пожаловать в программу работы с банковскими транзакциями.")

        transactions = []  # Список для хранения загруженных транзакций
        sorted_transactions = []  # Список для хранения отсортированных транзакций

        # Выбор JSON-, CSV- или XLSX-файла с транзакциями для дальнейшей работы с ним
        while not transactions:
            print("\nВыберите необходимый пункт меню:")
            print("1. Получить информацию о транзакциях из JSON-файла")
            print("2. Получить информацию о транзакциях из CSV-файла")
            print("3. Получить информацию о транзакциях из XLSX-файла")

            choice = input(">>> ")

            if choice == "1":
                transactions = read_json_file(os.path.join("data", "operations.json"))
                print("Для обработки выбран JSON-файл.")
            elif choice == "2":
                transactions = read_transactions_from_csv(os.path.join("data", "transactions.csv"), delimiter=';')
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
                    "amount": str(t.get("operationAmount", {}).get("amount", t.get("amount", ''))),
                    "currency": {
                        "name": t.get("operationAmount", {}).get("currency", {}).get("name", t.get("currency_name", "")),
                        "code": t.get("operationAmount", {}).get("currency", {}).get("code", t.get("currency_code", ""))
                    }
                },
                "description": t.get("description"),
                "from": t.get("from"),
                "to": t.get("to")
            }
            for t in transactions
        ]

        # Проверка корректности формата данных транзакций
        if not isinstance(transactions, list) or not all(isinstance(t, dict) for t in transactions):
            print("Ошибка: данные транзакций имеют неверный формат.")
            return

        # Фильтрация транзакций по статусу
        valid_states = ["EXECUTED", "CANCELED", "PENDING"]

        while True:
            state = input(
                f"\nВведите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки статусы: "
                f"{', '.join(valid_states)}\n>>> ")

            if state == "":
                print("Статус не введен. По умолчанию выбран статус \"EXECUTED\".")
                state = "EXECUTED"  # Устанавливаем статус по умолчанию

            # Используем обновленную функцию filter_by_state
            filtered_transactions = filter_by_state(transactions, state.upper())

            # Проверяем результат фильтрации
            if isinstance(filtered_transactions, str):  # Если результат - строка, значит, это сообщение об ошибке
                print(filtered_transactions)  # Показываем сообщение пользователю
            else:
                print(f"\nОперации отфильтрованы по статусу \"{state.upper()}\"")
                break

        # Фильтрация транзакций по дате
        if filtered_transactions:
            while True:
                sort_choice = input("\nОтсортировать операции по дате? Да/Нет\n>>> ").lower()

                if sort_choice in ["да"]:
                    while True:
                        order = input("\nОтсортировать по возрастанию или по убыванию?\n>>> ")
                        if order.lower() == "по убыванию":
                            reverse = True
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
            currency_choice = input("\nВыводить только рублевые транзакции? Да/Нет\n>>> ").lower()
            if currency_choice in ["да"]:
                sorted_transactions = [t for t in sorted_transactions if t["operationAmount"]["currency"]["code"] == "RUB"]
                break
            elif currency_choice in ["нет"]:
                break
            else:
                print("Введен некорректный ответ. Пожалуйста, ответьте 'Да' или 'Нет'.")

        # Фильтрация по описанию транзакций
        search_term = ""  # Задаем значение по умолчанию для search_term
        while True:
            description_filter = input(
                "\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n>>> ").lower()

            if description_filter in ["да"]:
                while True:
                    search_term = input("\nВведите слово для поиска в описании"
                                        "\n(например: перевод, открытие, закрытие, вклад, счет, организации и т.д.): "
                                        "\n>>> ").strip()

                    # Применяем функцию search_operations_by_description для поиска операций по описанию
                    filtered_transactions = search_operations_by_description(sorted_transactions, search_term)

                    # Применяем функцию count_operations_by_category для подсчета операций по категориям
                    count = count_operations_by_category(filtered_transactions, {})

                    sorted_transactions = filtered_transactions
                    break
                break
            elif description_filter in ["нет"]:
                # Если пользователь выбрал "нет", то просто сохраняем все транзакции
                filtered_transactions = sorted_transactions
                count = count_operations_by_category(filtered_transactions, {})
                break
            else:
                print("Введен некорректный ответ. Пожалуйста, ответьте 'Да' или 'Нет'.")

        print("_" * 40)  # разделитель
        print("Распечатываю итоговый список транзакций...")
        print("_" * 40)  # разделитель

        if filtered_transactions:
            print(f"\nВсего банковских операций в выборке: {len(filtered_transactions)}")

            # Выводим информацию по категориям, если она была подсчитана
            if 'count' in locals():
                print(f"\nНайдены следующие транзакции:")
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
            repeat_choice = input("Желаете еще раз повторить работу с банковскими транзакциями? Да/Нет\n>>> ").lower()
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


# Запуск основной функции программы
if __name__ == "__main__":
    main()
