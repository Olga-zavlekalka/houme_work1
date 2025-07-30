import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("start, stop, expected", [(1, 5, "0000 0000 0000 0001")])
def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    assert next(card_number_generator(start, stop)) == expected


def test_transaction_descriptions(transactions: list[dict]) -> None:
    assert next(transaction_descriptions(transactions)) == "Перевод организации"


def test_filter_by_currency(transactions: list[dict]) -> None:
    assert next(filter_by_currency(transactions, "USD")) == {
        "date": "2018-06-30T02:08:58.425572",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "id": 939719570,
        "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "Счет 11776614605963066702",
    }
