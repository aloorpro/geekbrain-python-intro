# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def person(**kwargs):
    res_string = ""
    for key, value in kwargs.items():
        res_string += f"{key}: {value}; "
    return res_string


while True:
    try:
        the_man = dict(zip(('name', 'soname', 'year', 'city', 'email', 'phone'),
                           list((input("Enter name soname year city email phone: ").split(" ")))))
        name = the_man['name']
        last_name = the_man['soname']
        year = the_man['year']
        city = the_man['city']
        email = the_man['email']
        phone = the_man['phone']
        print(f"Result is: {person(name=name, last_name=last_name, year=year, city=city, email=email, phone=phone)}")
        break
    except KeyError:
        print("Use more spaces")
