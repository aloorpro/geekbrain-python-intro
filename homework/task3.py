# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

months_list = [None, 'зима', 'зима', 'весна', 'весна',
               'весна', 'лето', 'лето', 'лето',
               'осень', 'осень', 'осень', 'зима'
               ]
months_dict = {1 : 'зима', 2: 'зима', 3 : 'весна', 4 : 'весна',
               5 : 'весна', 6 : 'лето', 7 : 'лето', 8 : 'лето',
               9 : 'осень', 10 : 'осень', 11 : 'осень', 12 : 'зима'
               }

while True:
    try:
        month = int(input('Enter a number from 1 to 12: '))
        if not 1 <= month <= 12:
            print('Try again')
            continue
        print(f"from list: {month} is {months_list[month]}")
        print(f"from dict: {month} is {months_dict[month]}")
        break
    except ValueError:
        print('Try again')