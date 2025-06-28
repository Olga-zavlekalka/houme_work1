from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(str_number: str) ->str:
    if "Счет" in str_number:
        return get_mask_account(str_number)
    else:
        return get_mask_card_number(str_number)


#"2024-03-11T02:26:18.671407"
#  и возвращает строку с датой в формате
# "ДД.ММ.ГГГГ"
#  (
# "11.03.2024"
# ).
def get_date(str_date: str) ->str:
    return f"{str_date[8:10]}.{str_date[5:7]}.{str_date[:4]}"
