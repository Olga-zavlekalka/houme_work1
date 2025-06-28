from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

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
