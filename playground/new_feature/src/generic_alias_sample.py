# refer: https://qiita.com/nicco_mirai/items/c1810ed2a6fc8c53c006#%E3%82%B8%E3%82%A7%E3%83%8D%E3%83%AA%E3%83%83%E3%82%AF%E5%9E%8B%E3%82%A8%E3%82%A4%E3%83%AA%E3%82%A2%E3%82%B9
from typing import TypeVar, Union, overload

T = TypeVar("T")
Err = Union[tuple[T, None], tuple[None, Exception]]


@overload
def my_div(num1: int, num2: int) -> Err[float]:
    ...


@overload
def my_div() -> Err[float]:
    ...


def my_div(num1=1, num2=1):
    try:
        return num1 / num2, None
    except (ZeroDivisionError, ValueError) as e:
        return None, e


if __name__ == "__main__":
    res, err = my_div(1, 2)
    assert not err
    print(f"{res=}, {err=}")

    res, err = my_div(1, 0)
    assert err
    print(f"{res=}, {err=}")

    res, err = my_div()
    assert not err
    print(f"{res=}, {err=}")
