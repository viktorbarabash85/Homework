from typing import Any, Dict, List, Optional

import pandas as pd


def read_transactions_from_csv(
    file_path: str, nrows: Optional[int] = None, delimiter: str = ","
) -> List[Dict[str, Any]]:
    """
    Чтение транзакций из CSV файла.
    Вход:
    - file_path Путь к CSV файлу.
    - nrows: Количество строк для чтения. Если None, читаются все строки.
    - delimiter: Символ-разделитель в CSV файле (, или ;).
    Выход:
    Список транзакций, где каждая транзакция представлена в виде словаря.
    """
    try:
        df = pd.read_csv(file_path, nrows=nrows, delimiter=delimiter)
        if df.empty:
            return []  # Возвращаем пустой список вместо выбрасывания исключения
        result = df.iloc[:nrows].to_dict(orient="records")
        return result
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")
    except pd.errors.EmptyDataError:
        return []  # Возвращаем пустой список для пустых файлов
    except Exception as e:
        raise Exception(f"Ошибка при чтении CSV файла: {str(e)}")


def read_transactions_from_excel(file_path: str, nrows: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Чтение транзакций из Excel файла.
    Вход:
    - file_path: Путь к Excel файлу.
    - nrows: Количество строк для чтения. Если None, читаются все строки.
    Выход:
    - Список транзакций, где каждая транзакция представлена в виде словаря.
    """
    try:
        df = pd.read_excel(file_path, nrows=nrows)
        if df.empty:
            return []  # Возвращаем пустой список вместо выбрасывания исключения
        result = df.iloc[:nrows].to_dict(orient="records")
        return result
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")
    except Exception as e:
        raise Exception(f"Ошибка при чтении Excel файла: {str(e)}")
