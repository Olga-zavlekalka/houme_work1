from _pytest.capture import CaptureFixture

from src.decorators import log


# тест проверяет работу декоратора
def test_log(capsys: CaptureFixture) -> None:
    @log()
    def my_function(x: int, y: int) -> float:
        return x / y

    my_function(0, 3)
    captured = capsys.readouterr()
    assert "my_function выполнилась с результатом 0.0" in captured.out

    @log(filename="logs/1.txt")
    def my_function1(x: int, y: int) -> float:
        return x / y

    my_function1(3, 0)
    f = open("logs/1.txt", encoding="utf-8")
    data = f.read()
    assert "my_function, ZeroDivisionError: division by zero, inputs:(3, 0), {}" in data
    f.close()
