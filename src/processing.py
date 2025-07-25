from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(list_dict: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict]:
    """которая принимает список словарей и опционально значение
    для ключа state(по умолчанию 'EXECUTED'). Функция возвращает новый
    список словарей, содержащий только те словари, у которых ключ state
    cответствует указанному значению."""
    list_dictionary = []
    for dic in list_dict:
        if dic.get("state") == state:
            list_dictionary.append(dic)
    return list_dictionary


def sort_by_date(list_dict: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date)"""
    list_dictionary_2 = sorted(list_dict, key=lambda k: datetime.fromisoformat(k["date"]), reverse=reverse)

    return list_dictionary_2
