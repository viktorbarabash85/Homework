from unittest.mock import patch

from main import main


def test_main_debug() -> None:
    """
    Тест для функции main() с использованием mock для input() и read_json_file().
    """
    # Список значений для input()
    inputs = [
        "1",  # Выбор JSON файла
        "EXECUTED",  # Фильтрация по статусу
        "да",  # Сортировка по дате
        "по убыванию",  # Порядок сортировки
        "нет",  # Фильтрация по рублевым транзакциям
        "да",  # Фильтрация по описанию
        "вклад",  # Поиск по слову
    ]

    # JSON данные для мока read_json_file
    mock_transactions = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]

    # Mock для input()
    def mock_input(prompt: str) -> str:
        if not inputs:
            print(f"Input prompt: {prompt}")
            raise RuntimeError("Список inputs опустел, но программа продолжает запрашивать ввод.")
        value = inputs.pop(0)
        print(f"{prompt} {value}")
        return value

    # Mock функции read_json_file
    with patch("main.read_json_file",
               return_value=mock_transactions), patch("builtins.input", side_effect=mock_input):
        try:
            print("DEBUG: Запуск main()")
            main()
        except RuntimeError as e:
            print(f"DEBUG: Ошибка выполнения: {e}")


if __name__ == "__main__":
    test_main_debug()
