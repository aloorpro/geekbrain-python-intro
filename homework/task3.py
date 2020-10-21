# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
# кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
# дохода сотрудников.
from random import randint


def make_salary_list(filename):
    names = ['Иванов', 'Горбунов', 'Smith', 'Петров', 'Горбунов',
             'Jones', 'Sanchez', 'Дуров', 'Trump', 'Касперский',
             'Morgan', 'Rivera', 'Пушкин', 'Тургенев', 'Taylor',
             'Лавров', 'Sanders', 'Ross', 'Хлестов']
    with open(filename, 'x', encoding='utf-8') as file:
        file.writelines(list(map(lambda name: f"{name} {randint(15000, 50000)}\n", names)))


def analyze(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        salaries = []
        cons = file.readline().split()
        while cons:
            name, salary = cons
            if int(salary) <= 20000:
                print(name)
            salaries.append(int(salary))
            cons = file.readline().split()
    return round(sum(salaries) / len(salaries), 2)


if __name__ == '__main__':
    filename = 'example3'
    try:
        make_salary_list(filename)
    except FileExistsError:
        pass
    print("The poorest employees:")
    try:
        mean = analyze(filename)
        print(f'Mean salary is {mean}')
    except ValueError:
        print("File is in wrong format")
