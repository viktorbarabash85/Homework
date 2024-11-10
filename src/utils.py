import json
from typing import Dict, List

from src.file_logger import setup_logger

# Настраиваем логгер для модуля utils
logger = setup_logger("utils", "utils")


def read_json_file(file_path: str) -> List[Dict]:
    """Читает JSON-файл и возвращает список словарей с данными о транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
        if isinstance(repos, list):
            logger.info("Успешно прочитан JSON-файл.")
            return repos
        else:
            logger.warning("JSON-файл не содержит список.")
            return []
    except Exception as e:
        logger.error(f"Ошибка при чтении файла: {e}")
        return []
