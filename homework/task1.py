# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, list_of_lists):
        min_len = min(map(len, list_of_lists))
        self.matrix = list(map(lambda x: x[:min_len], list_of_lists))

    def __str__(self):
        longest_num = max(map(lambda y: max(map(lambda x: len(str(x)), y)), self.matrix))
        result = ""
        for nums in self.matrix:
            line = ""
            for num in nums:
                line += f"{num:{longest_num + 1}}"
            result += f"{line}\n"
        return result

    def __add__(self, other):
        result = []
        for i in range(min(map(len, (self.matrix, other.matrix)))):
            result.append(list(map(sum, zip(self.matrix[i], other.matrix[i]))))
        return Matrix(result)


neo = Matrix([[3,5,32],[2,4.234,6],[-1,64,-8]])
triniti = Matrix([[1,2,3,4], [5,6,7,8], [964, 342, 4235, 3], [0,0,0,0,0]])
print(neo + triniti)
