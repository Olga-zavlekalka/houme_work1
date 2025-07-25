#которая принимает список словарей и опционально значение
# для ключа state(по умолчанию 'EXECUTED'). Функция возвращает новый
# список словарей, содержащий только те словари, у которых ключ state
# cответствует указанному значению.
from typing import List, Dict, Any
from datetime import datetime


def filter_by_state(list_dict: List[Dict[str, Any]], state:str ='EXECUTED') ->List[Dict]:
    list_1 = []
    for dic in list_dict:
        if dic.get('state') == state:
            list_1.append(dic)
    return list_1






#которая принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
# Функция должна возвращать новый список, отсортированный по дате (date).
def sort_by_date(list_dict: List[Dict[str, Any]], reverse: bool = True) ->List[Dict[str, Any]]:
    list_2 = sorted(list_dict, key=lambda k:  datetime.fromisoformat(k['date']), reverse=reverse)
    return list_2

