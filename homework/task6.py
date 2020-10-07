# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

while True:
    try:
        a = float(input("First day result: "))
        b = float(input("Target result: "))
        break
    except ValueError:
        print("Just numbers")

day = 1
while True:
    print(f"{a:.2f}km at {day} day")
    if a >= b: break
    day += 1
    a = a * 1.1

print(f"You succeed at {day} day")
