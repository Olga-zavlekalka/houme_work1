import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
# функция проверяет ожидаемое значение
def test_filter_by_state_with_parametrize(list_dict: list[dict], state: str, expected: list[dict]) -> None:
    assert filter_by_state(list_dict, state) == expected


# функция проверяет сортировку по дате
def test_sort_by_date(list_dict: list[dict]) -> None:
    assert sort_by_date(list_dict, reverse=True)
    assert sort_by_date(list_dict, reverse=False)
