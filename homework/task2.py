# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
from sys import path
from os import getcwd
path.insert(0, getcwd())
from task1 import write_to_file

def wc(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lengths = list(map(lambda x: len(x.split()), lines))
        return len(lines), lengths


if __name__ == '__main__':
    print("Writing to file example2, leave empty for stop:")
    file = 'example2'
    write_to_file(file, 'a')
    results = wc(file)
    print(f'Number of lines: {results[0]}')
    print("Number of words by line:")
    for i, num in enumerate(results[1], 1):
        print(f'{i}: {num}')