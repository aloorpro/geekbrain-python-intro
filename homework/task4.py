# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

while True:
    try:
        number = int(input("Enter a pos. integer: "))
    except ValueError:
        print("Not a number")
        continue
    if number > 0:
        break
    else:
        print("Not positive")


def max_digit(num, digit):
    i = num % 10
    if i > digit:
        digit = i
    if num >= 10:
        return max_digit(num // 10, digit)
    else:
        return digit


print("The biggest digit in {} is {}".format(number, max_digit(number, 0)))

k = 0
while number > 0:
    if number % 10 > k:
        k = number % 10
    number = number // 10

print(f"With while cycle result is also {k}")
