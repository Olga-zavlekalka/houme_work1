import pytest

from src.masks import get_mask_account, get_mask_card_number


# функция проверяет работу маскировку карты
def test_get_mask_card_number() -> None:
    assert get_mask_card_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert get_mask_card_number("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


# функция проверяет которкий ввод данных карты
def test_get_mask_card_number_shot() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")


# функция проверяет длинный ввод данных карты
def test_get_mask_card_number_long() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("MasterCard 7158300734726758             ")


# функция проверяет ввод данных карты
def test_get_mask_account() -> None:
    assert get_mask_account("Счет 64686473678894779589") == "Счет **9589"
    assert get_mask_account("Счет 35383033474447895560") == "Счет **5560"


# функция проверяет которкий ввод данных карты
def test_get_mask_account_shot() -> None:
    with pytest.raises(ValueError):
        get_mask_account("")


# функция проверяет длинный ввод данных карты
def test_get_mask_account_long() -> None:
    with pytest.raises(ValueError):
        get_mask_account("Счет 64686473678894779589    ")
