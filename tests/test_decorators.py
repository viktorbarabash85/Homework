import os

import pytest

from src.decorators import log


def test_log_file() -> None:
    """
    Тест записи в файл при успешной работе функции.

    Проверяет, что функция example_function корректно записывает результат
    в файл mylog.txt при успешном выполнении.
    """

    @log(filename="mylog.txt")
    def example_function(x: int, y: int) -> int:
        return x * y

    result = example_function(5, 100)

    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function ok. Result: 500\n"
    assert result == 500


def test_log_console(capsys: pytest.CaptureFixture) -> None:
    """
    Тест вывода в консоль при успешной работе функции.

    Проверяет, что функция example_function корректно выводит результат
    в консоль при успешном выполнении.
    """

    @log()
    def example_function(x: int, y: int) -> int:
        return x * y

    result = example_function(5, 100)

    captured = capsys.readouterr()

    assert captured.out == "example_function ok. Result: 500\n"
    assert result == 500


def test_log_file_raise() -> None:
    """
    Тест записи в файл, если произошла ошибка.

    Проверяет, что при возникновении исключения TypeError функция
    example_function записывает информацию об ошибке в файл mylog.txt.
    """

    log_file_path = os.path.join("logs", "mylog.txt")

    # Удаляем файл, если он существует, чтобы избежать накопления логов
    if os.path.exists(log_file_path):
        os.remove(log_file_path)

    @log(filename="mylog.txt")
    def example_function(x: int, y: int) -> None:
        raise TypeError("Что-то пошло не так")

    with pytest.raises(TypeError, match="Что-то пошло не так"):
        example_function(5, 100)

    # Чтение из файла с указанием кодировки
    with open(log_file_path, "rt", encoding="utf-8") as file:
        log_lines = file.readlines()

    # Проверка последней строки лога
    expected_log_line = "example_function TypeError: Что-то пошло не так. Inputs: (5, 100), {}\n"
    assert log_lines[-1] == expected_log_line


def test_log_console_raise(capsys: pytest.CaptureFixture) -> None:
    """
    Тест вывода в консоль, если произошла ошибка.

    Проверяет, что при возникновении исключения ValueError функция
    example_function выводит информацию об ошибке в консоль.
    """

    @log()
    def example_function(x: int, y: int) -> None:
        raise ValueError("Что-то пошло не так")

    with pytest.raises(ValueError, match="Что-то пошло не так"):
        example_function(5, 100)

    captured = capsys.readouterr()

    print(captured.out == "example_function ValueError: Что-то пошло не так. Inputs: (5, 100), {}\n")
