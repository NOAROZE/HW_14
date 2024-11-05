# a
while True:
    num: int = int(input("Enter a number:"))
    if 0 <= num < 9999:
        break
digit1: int = num % 10
bool_list: list[bool] = []
num = num // 10
while num > 0:
    digit: int = num % 10
    if digit1 == digit:
        bool_list.append(True)
        digit = digit1
    else:
        bool_list.append(False)
        break
    num = num // 10
print("True" if all(bool_list) else "False")
#

# b
num: int = int(input("Enter the purchase price of the purchase:"))
price: int = num
ten_discount: int = 0
twenty_discount: int = 0
thirty_discount: int = 0
forty_discount: int = 0
fifty_discount: int = 0
if num > 0:
    if num > 100:
        ten_discount = 10
        num -= 100
    else:
        ten_discount = int(num / 100 * 10)
        num -= num
if num > 0:
    if num > 100:
        twenty_discount = 20
        num -= 100
    else:
        twenty_discount = int(num / 100 * 20)
        num -= num
if num > 0:
    if num > 300:
        thirty_discount = 30
        num -= 300
    else:
        thirty_discount = int(num / 100 * 30)
        num -= num
if num > 0:
    if num > 300:
        forty_discount = 40
        num -= 100
    else:
        forty_discount = int(num / 100 * 40)
        num -= num
if num > 0:
    fifty_discount= int(num // 100 * 50)
print(price - ten_discount -twenty_discount - thirty_discount - forty_discount - fifty_discount)
#

# c
num1: float = float(input("enter a number:"))
num2: float = float(input("enter a number:"))
num3: float = float(input("enter a number:"))
print("True" if num1 + num2 == num3 or num2 + num3 == num1 or num3 + num1 == num2 else "False")
#

# d
word: str = input("Enter a word:")
word1: str = ""
bool_l: list[bool] = []
while True:
    letter: str = input("Enter a letter:")
    if letter == "*":
        break
    word1 += letter
print(word1)
for l in word1:
        bool_l.append(True if l in word else False)
print("True" if all(bool_l) else "False")
#
