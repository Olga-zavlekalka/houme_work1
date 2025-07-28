from src.widget import mask_account_card
import pytest


def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert mask_account_card("Счет 64686473678894779589") == "Счет **9589"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"



