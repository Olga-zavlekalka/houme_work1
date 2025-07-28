from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card
from src.processing import sort_by_date, filter_by_state

if __name__ == "__main__":
    # Пример использования функции

    # Входной аргумент
    card_number = "7000792289606361"

    print(get_mask_card_number(card_number))

    # Входной аргумент
    account_number = "73654108430135874305"

    # Вызов функции и вывод результата
    print(get_mask_account(account_number))  # должно вывести: **4305

    str_number = "Maestro 1596837868705199"
    str_number1 = "Счет 64686473678894779589"
    str_number2 = "MasterCard 7158300734726758"
    str_number3 = "Счет 35383033474447895560"
    str_number4 = "Visa Classic 6831982476737658"
    str_number5 = "Visa Platinum 8990922113665229"
    str_number6 = "Visa Gold 5999414228426353"
    str_number7 = "Счет 73654108430135874305"
    print(mask_account_card(str_number))
    print(mask_account_card(str_number1))
    print(mask_account_card(str_number2))
    print(mask_account_card(str_number3))
    print(mask_account_card(str_number4))
    print(mask_account_card(str_number5))
    print(mask_account_card(str_number6))
    print(mask_account_card(str_number7))

    str_date = "2024-03-11T02:26:18.671407"
    print(get_date(str_date))

list_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(sort_by_date(list_dict))
print(filter_by_state(list_dict))


