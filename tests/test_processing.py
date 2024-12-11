import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_correct(filter_by_state_correct: list[dict[str, str]]) -> None:
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
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "INVALID_STATE",
            "Информация отсутствует или некорректно введен запрашиваемый статус",
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


def test_sort_by_date_incorrect(sort_by_date_incorrect: list[dict[str, str]]) -> None:
    """
    Тестирование сортировки списка словарей при некорректно введенной дате
    (пустая дата, без T, изменена структура даты, изменена структура времени,
    введены нереальные значения даты и времени).

    :param sort_by_date_incorrect: Ожидаемый результат сортировки при некорректной дате.
    """
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": ""},
                {"id": 939719570, "state": "EXECUTED", "date": "2018/06/30 02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018.09.12(T21:27:25.241689)"},
                {"id": 615064591, "state": "CANCELED", "date": "14.10.2018_T_08:21:33"},
            ]
        )
        == sort_by_date_incorrect
    )


@pytest.mark.parametrize(
    "transactions, reverse, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.222222"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-10-14T08:21:33.111111"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T08:21:33.444444"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.333333"},
            ],
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-10-14T08:21:33.111111"},
                {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.222222"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.333333"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-10-14T08:21:33.444444"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": ""},
                {"id": 939719570, "state": "EXECUTED", "date": "2018.06.30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018_09_12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018/10/14T08:21:33"},
            ],
            None,
            "Введен некорректный или нестандартный формат даты",
        ),
    ],
)
def test_sort_by_date(transactions: list, reverse: bool, expected: list) -> None:
    """
    Тестирование сортировки списка словарей по дате с различными входными данными.

    :param transactions: Список словарей с транзакциями.
    :param reverse: Параметр для указания порядка сортировки (True для убывания, False для возрастания).
    :param expected: Ожидаемый результат сортировки.
    """
    assert sort_by_date(transactions, reverse) == expected
