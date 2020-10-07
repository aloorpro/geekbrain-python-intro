# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

while True:
    try:
        total_secs = int(input("Enter time in secs: "))
        break
    except ValueError:
        print("Wrong input. Try again.")
        continue

total_minutes = total_secs // 60
seconds = total_secs % 60
minutes = total_minutes % 60
hours = total_minutes // 60 % 24
def xx(val):
    if val < 10:
        val = '0' + str(val)
    return val

print("{}:{}:{}".format(xx(hours), xx(minutes), xx(seconds)))
