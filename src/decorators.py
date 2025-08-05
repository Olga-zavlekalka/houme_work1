from functools import wraps
from typing import Any, Callable


def writting_log(log_message: str, filename: str) -> None:
    """запись в переменную логирования выполнения функции"""
    if filename:
        with open(filename, "a", encoding="utf-8") as e:
            e.write(f"{log_message}\n")
    else:
        print(log_message)


def log(filename: Any = None) -> Callable:
    """результат логирования функции"""

    def my_decorator(func: Callable) -> Any | None:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any | None:
            message = ""
            result = None
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} выполнилась с результатом {result}"

            except Exception as error:
                message = f"{func.__name__}, {type(error).__name__}: {error}, inputs:{args}, {kwargs}"
            finally:
                writting_log(message, filename)
            return result

        return wrapper

    return my_decorator
