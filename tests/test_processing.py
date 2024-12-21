import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_number(filter_by_state_incorrect_number: list[dict]) -> None:
    """
    Тестирование правильности фильтрации списка словарей по некорректному статусу.

    :param filter_by_state_incorrect_number: Фикстура, возвращающая список словарей с некорректным статусом.
    """

    # Ожидаем, что вызов функции filter_by_state с некорректным статусом вызовет ValueError
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(filter_by_state_incorrect_number, "11111")

    # Проверяем, что сообщение об ошибке соответствует ожидаемому
    assert str(exc_info.value) == (
        'Ошибка. Статус "11111" введен некорректно. ' "Допустимые статусы ('EXECUTED', 'CANCELED', 'PENDING')"
    )


def test_filter_by_state_correct(filter_by_state_correct: list[dict]) -> None:
    """
    Тестирование правильности фильтрации списка словарей по заданному статусу state: CANCELED.

    :param filter_by_state_correct: Ожидаемый результат фильтрации по статусу CANCELED.
    """
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
        == filter_by_state_correct
    )


def test_filter_by_state_incorrect(filter_by_state_incorrect: list[dict[str, str]]) -> None:
    """
    Тестирование корректности функции при отсутствии словарей с заданным статусом state.

    :param filter_by_state_incorrect: Ожидаемый результат фильтрации при отсутствии статуса CANCELED.
    """
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
        )
        == filter_by_state_incorrect
    )


def test_filter_without_state_correct(filter_without_state_correct: list[dict[str, str]]) -> None:
    """
    Тестирование правильности фильтрации списка словарей при отсутствии статуса state
    (по умолчанию 'EXECUTED').

    :param filter_without_state_correct: Ожидаемый результат фильтрации по умолчанию.
    """
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == filter_without_state_correct
    )


@pytest.mark.parametrize(
    "transactions, state, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(transactions: list, state: str, expected: list) -> None:
    """
    Тестирование фильтрации списка словарей по статусу state с различными входными данными.

    :param transactions: Список словарей с транзакциями.
    :param state: Статус, по которому производится фильтрация.
    :param expected: Ожидаемый результат фильтрации.
    """
    assert filter_by_state(transactions, state) == expected


def test_sort_by_date_true(sort_by_date_true_correct: list) -> None:
    """
    Тестирование сортировки списка словарей по датам в порядке убывания
    (по умолчанию — убывание: True).

    :param sort_by_date_true_correct: Ожидаемый результат сортировки по убыванию.
    """
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == sort_by_date_true_correct
    )


def test_sort_by_date_false(sort_by_date_false_correct: list[dict[str, str]]) -> None:
    """
    Тестирование сортировки списка словарей по датам в порядке возрастания.

    :param sort_by_date_false_correct: Ожидаемый результат сортировки по возрастанию.
    """
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        )
        == sort_by_date_false_correct
    )


@pytest.mark.parametrize(
    "transactions_2, reverse, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            None,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_sort_by_date(transactions_2: list, reverse: bool, expected: list) -> None:
    """
    Тестирование сортировки списка словарей по дате с различными входными данными.

    :param transactions_2: Список словарей с транзакциями.
    :param reverse: Параметр для указания порядка сортировки (True для убывания, False для возрастания).
    :param expected: Ожидаемый результат сортировки.
    """
    if reverse is None:
        reverse = True  # Установим значение по умолчанию, если оно None
    assert sort_by_date(transactions_2, reverse) == expected
