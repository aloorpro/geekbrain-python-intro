# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
from sys import argv
from googletrans import Translator


def translate_numbers(srcfile, destfile):
    trans = Translator()
    rus = lambda word: trans.translate(word, dest='ru').text.capitalize()
    with open(srcfile, 'r', encoding='utf-8') as rfile:
        with open(destfile, 'w', encoding='utf-8') as wfile:
            cons = rfile.readline().split()
            while cons:
                word = cons.pop(0)
                cons.insert(0, rus(word))
                wfile.write(f"{' '.join(cons)}\n")
                cons = rfile.readline().split()
    del trans


if __name__ == '__main__':
    try:
        file = argv[1]
        translate_numbers('example4', file)
        print('Succeess.')
    except IndexError:
        print('Fail. No dst file name')