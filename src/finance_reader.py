from typing import Any, Hashable, List, Optional

import pandas as pd


def read_transactions_from_csv(
    file_path: str, nrows: Optional[int] = None, delimiter: str = ";"
) -> List[dict[Hashable, Any]]:
    """
    Чтение транзакций из CSV файла.

    :param file_path: Путь к CSV файлу.
    :param nrows: Количество строк для чтения. Если None, читаются все строки.
    :param delimiter: Символ-разделитель в CSV файле (например, ',' или ';').
    :return: Список транзакций, где каждая транзакция представлена в виде словаря.

    :raises FileNotFoundError: Если файл не найден.
    :raises Exception: Если произошла ошибка при чтении CSV файла.
    """
    try:
        df = pd.read_csv(file_path, nrows=nrows, sep=delimiter)
        if df.empty:
            return []  # Возвращаем пустой список для пустых файлов
        result = df.iloc[:nrows].to_dict(orient="records")  # Преобразуем только нужные строки в словари
        return result
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")
    except Exception as e:
        raise Exception(f"Ошибка при чтении CSV файла: {str(e)}")


def read_transactions_from_excel(file_path: str, nrows: Optional[int] = None) -> List[dict[Hashable, Any]]:
    """
    Чтение транзакций из Excel файла.

    :param file_path: Путь к Excel файлу.
    :param nrows: Количество строк для чтения. Если None, читаются все строки.
    :return: Список транзакций, где каждая транзакция представлена в виде словаря.

    :raises FileNotFoundError: Если файл не найден.
    :raises Exception: Если произошла ошибка при чтении Excel файла.
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
