from typing import Generator, Iterator


def filter_by_currency(transactions: list[dict], currency_code: str) -> Iterator:
    '''принимает на вход список словарей, представляющих транзакции'''
    transaction_filter = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_code, transactions)
    return transaction_filter


def transaction_descriptions(transactions: list[dict]) -> Generator:
    '''принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.'''
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    '''генератор, который выдает номера банковских карт в формате
XXXX XXXX XXXX XXXX, где X — цифра номера карты'''
    for num in range(start, stop + 1):
        card_number = str(num).zfill(16)
        yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
