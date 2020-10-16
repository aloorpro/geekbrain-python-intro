# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide(x, y):
    return x / y


while True:
    try:
        n = float(input("Divident: "))
        m = float(input("Divisor: "))
        print(f"Division is: {divide(n, m)}")
        break
    except ValueError:
        print("Enter numbers")
    except ZeroDivisionError:
        print("Don't enter zero as divisor")