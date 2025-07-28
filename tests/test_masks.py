from src.masks import get_mask_card_number
import pytest

def test_get_mask_card_number():
    assert get_mask_card_number('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert get_mask_card_number('MasterCard 7158300734726758') == 'MasterCard 7158 30** **** 6758'


def test_get_mask_card_number_shot():
    with pytest.raises(ValueError):
       get_mask_card_number('')


def test_get_mask_card_number_long():
    with pytest.raises(ValueError):
       get_mask_card_number('MasterCard 7158300734726758     ')
