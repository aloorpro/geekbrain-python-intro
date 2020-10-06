# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

while True:
    try:
        proceeds = int(input("Profit: "))
        costs = int(input("Costs: "))
        break
    except ValueError:
        print("Error. Again")

profit = proceeds - costs

if profit <= 0:
    print("No profit. Work better")
    exit()

print(f'Profitability is {profit / proceeds}')

while True:
    try:
        staff = int(input("Staff number : "))
        break
    except ValueError:
        print("Error. Again")

print(f"Mean profit is {profit / staff:.2f}")
