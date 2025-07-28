"""Определяем функцию с именем get_mask_card_number"""


def get_mask_card_number(card_number: str) -> str:
    """Указываем, что она принимает один параметр - card_number"""
    if len(card_number) == 0:
        raise ValueError("Вы не ввели номер карты")
    elif len(card_number):
        raise ValueError("Вы ввели слишком длинный номер карты")

    masked_number = f"{card_number[:-17]}{card_number[-17:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Определяем функцию маскировки номера счета"""

    masked_account = f"Счет **{account_number[-4:]}"
    return masked_account
