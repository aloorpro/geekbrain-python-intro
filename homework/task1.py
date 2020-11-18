# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
from sys import argv


def write_to_file(name, method):
    with open(name, method, encoding='utf-8') as file:
        string = input("Prompt: ")
        while string:
            file.write(f'{string}\n')
            string = input("Prompt: ")


if __name__ == '__main__':
    try:
        filename = argv[1]
        write_to_file(filename, 'w')
    except IndexError:
        print("need filename as arg")