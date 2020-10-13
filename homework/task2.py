# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
new_list = []
while True:
    elem = input("element: ")
    if not elem:
        break
    my_list.append(elem)

for i, v in enumerate(my_list[:]):
    if not i % 2:
        try:
            vv = my_list[i+1]
            new_list.append(vv)
        except IndexError:
            pass
        finally:
            new_list.append(v)

print(my_list)
print(new_list)
