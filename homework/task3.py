# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    try:
        number = input("Enter a number: ")
        n = int(number)
        nn = int(number*2)
        nnn = int(number*3)
        break
    except ValueError:
        print("Try again")

print(f"n + nn + nnn = {n + nn + nnn}")
