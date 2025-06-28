"""Определяем функцию с именем get_mask_card_number"""


def get_mask_card_number(card_number: str) -> str:
    """Указываем, что она принимает один параметр - card_number"""

    masked_number = f"{card_number[:-17]}{card_number[-17:-12]} {card_number[-12:-10]}** **** {card_number[-4:]}"
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Определяем функцию маскировки номера счета"""

    masked_account = f"Счет **{account_number[-4:]}"
    return masked_account
