import pytest

from src.widget import get_date, mask_account_card


# добавлена параметризация по функции mask_account_card
@pytest.mark.parametrize(
    "str_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ],
)
def test_mask_account_card_with_parametrize(str_number: str, expected: str) -> None:
    """добавлен тест по функции mask_account_card"""
    assert mask_account_card(str_number) == expected


def test_mask_account_card() -> None:
    """функция test_get_dateтестирует разные виды карт"""
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_get_date() -> None:
    """функция test_get_date тестирует разные вводные данные по дате"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


