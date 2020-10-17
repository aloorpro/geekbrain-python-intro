# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter
# должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
# и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.

def map_until(func, iterable):
    for i in iterable:
        try:
            yield func(i)
        except ValueError:
            global interrupt
            interrupt = True
            break


my_sum = 0
interrupt = False
while not interrupt:
    nums = list(map_until(float, input("Enter nums or not nums for interrupt: ").split()))
    my_sum += sum(nums)
    print(f"Sum is {my_sum}")
