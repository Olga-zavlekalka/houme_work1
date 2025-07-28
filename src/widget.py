from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(str_number: str) -> str:
    """функция, которая обрабатывает информацию о данных карт"""
    if "Счет" in str_number:
        return get_mask_account(str_number)
    else:
        return get_mask_card_number(str_number)


def get_date(str_date: str) -> str:
    """функция которая форматирует дату"""
    if len(str_date) == 0:
        raise ValueError("Вы не ввели дату")
    return f"{str_date[8:10]}.{str_date[5:7]}.{str_date[:4]}"
