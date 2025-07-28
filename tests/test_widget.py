from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize ('str_number, expected', [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'), ('Счет 64686473678894779589', 'Счет **9589'), ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758')])
def test_mask_account_card_with_parametrize(str_number, expected):
    assert mask_account_card(str_number) == expected


def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

def test_get_date_short():
    with pytest.raises(ValueError):
        get_date('')

