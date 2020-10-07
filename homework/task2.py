# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

while True:
    try:
        total_secs = int(input("Enter time in secs: "))
        break
    except ValueError:
        print("Wrong input. Try again.")
        continue

class TimeFormat:
    def __init__(self, secs):
        self.seconds = secs % 60
        self.minutes = secs // 60 % 60
        self.hours = secs // 3600 % 24

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

our_time = TimeFormat(total_secs)

print(f"{our_time}")
