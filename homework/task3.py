# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    return (x + y + z) - min(x, y, z)


while True:
    try:
        xs = tuple(map(int, (input("3 numbers with spaces: ").split(" "))[:3]))
        print(f"Result is: {my_func(xs[0], xs[1], xs[2])}")
        break
    except ValueError:
        print("Enter numbers")
    except IndexError:
        print("Use spaces")