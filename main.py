from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    # Пример использования функции

    # Входной аргумент
    card_number = "7000792289606361"

    print(get_mask_card_number(card_number))

    # Входной аргумент
    account_number = "73654108430135874305"

    # Вызов функции и вывод результата
    print(get_mask_account(account_number))  # должно вывести: **4305
