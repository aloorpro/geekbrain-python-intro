# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
from sys import argv
from json import dumps


def firms(filename):
    profits = dict()
    for firm in open(filename, 'r', encoding='utf-8'):
        name, form, income, costs = firm.split()
        profits[name] = int(income) - int(costs)
    profitables = list(filter(lambda x: x > 0, profits.values()))
    return [profits, {'average_profit': round(sum(profitables) / len(profitables), 2)}]


if __name__ == '__main__':
    try:
        dstfile = argv[1]
        with open(dstfile, 'w', encoding='utf-8') as dst:
            dst.write(dumps(firms('example7')))
    except IndexError:
        print("Need filename")