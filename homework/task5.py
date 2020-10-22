# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
def make_file(name):
    while True:
        try:
            string = input('Enter nums with spaces: ')
            nums = list(map(int, string.split()))
            break
        except ValueError:
            print('Try again')
    with open(name, 'w', encoding='utf-8') as file:
        file.write(f'{string}\n')
    return nums


if __name__ == '__main__':
    nums = make_file('example5')
    print(f'Sum is {sum(nums)}')