# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

while True:
    try:
        natural = int(input("Enter a natural number: "))
        rational = float(input("Enter a rational number: "))
        phrase = input("Enter anything: ")
        break
    except ValueError:
        print("Please type what you've asked for. Try again")
        continue

print("Got some values: \n\rNatural: {}\n\rRational: {}\n\rSome string: {}"\
      .format(natural, rational, phrase))