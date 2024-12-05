import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"


def api_convert_currency(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли через API.

    :param transaction: Словарь, представляющий транзакцию, содержащий информацию о сумме и валюте.
    :return: Конвертированная сумма в рублях. Возвращает 0.0 в случае ошибки или если валюта не поддерживается.
    """
    amount = transaction.get("operationAmount", {}).get("amount", 0.0)  # Default to 0.0
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "")  # Default to empty string

    if currency == "RUB":
        return float(amount)  # Ensure it's returned as float
    elif currency in ["USD", "EUR"]:
        try:
            response = requests.get(
                API_URL.format(to="RUB", from_=currency, amount=amount), headers={"apikey": API_KEY}
            )
            if response.status_code == 200:
                data = response.json()
                return float(data.get("result", 0.0))  # Ensure it's returned as float
            else:
                print(f"Ошибка при конвертации валюты: {response.status_code}")
                return 0.0  # Returning float
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при конвертации валюты: {e}")
            return 0.0  # Returning float
    else:
        return 0.0  # Returning float
