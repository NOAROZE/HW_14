def my_ascending(x: int, y: int):
    print(f"{y} ,{x}" if x > y else f"{x} ,{y}")


def my_details(string):
    length: int = len(string)
    half: int = length // 2 - 1
    print(f"The first char is:{string[0]}")
    print(f"The last char is:{string[-1]}")
    print(f"The middle character:{string[half]}")


def say_bool(bool1):
    print("yes" if bool1 == True else "no")


def print_zugi(numbers: list[int]):
    for num in numbers:
        print("even" if num % 2 == 0 else "odd")


def my_statistics(scores: list[float]):
    high: float = 0
    for score in scores:
        if score > high:
            high = score
    print(f"The highest score is: {high}")
    low: float = 0
    for score in scores:
        if score < low:
            low = score
    print(f"The lowest score is: {low}")
    average: float = 0
    counter: int = 0
    for score in scores:
        average += score
        counter += 1
    print(f"The average of scores is: {average / counter}")
