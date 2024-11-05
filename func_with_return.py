from os import stat_result


def my_avg(x: int, y: int):
    avg: float = (x + y) / 2
    return avg
def my_headline(string):
    str1: str = string.upper() + "!"
    return str1
def concat_list(l1: list[int],l2: list[int],l3: list[int]):
    all_l:list[int] = l1 + l2 +l3
    return all_l