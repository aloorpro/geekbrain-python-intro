# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы. Подсказка: матрица — система некоторых математических
# величин, расположенных в виде прямоугольной схемы. Примеры матриц вы найдете в методичке. Следующий шаг —
# реализовать перегрузку метода __str__() для вывода матрицы в привычном виде. Далее реализовать перегрузку метода
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна
# быть новая матрица. Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, list_of_lists):
        self.length = min(map(len, list_of_lists))
        self.height = len(list_of_lists)
        self.matrix = list(map(lambda x: x[:self.length], list_of_lists))

    def __str__(self):
        longest_num = max(map(lambda y: max(map(lambda x: len(str(x)), y)), self.matrix))
        result = ""
        for nums in self.matrix:
            line = ""
            for num in nums:
                line += f"{num:{longest_num + 2}}"
            result += f"{line}\n"
        return result

    def __add__(self, other):
        x = self.matrix
        y = other.matrix
        if self.height > other.height:
            y += [[0] * other.length] * (self.height - other.height)
        elif self.height < other.height:
            x += [[0] * self.length] * (other.height - self.height)
        if self.length > other.length:
            y = list(map(lambda line: line + [0] * (self.length - other.length), y))
        elif other.length > self.length:
            x = list(map(lambda line: line + [0] * (other.length - self.length), x))
        result = []
        for i in range(max(self.height, other.height)):
            result.append(list(map(sum, zip(x[i], y[i]))))
        return Matrix(result)


neo = Matrix([[3,5,32],[2,4.234,6],[-1,64,-8]])
trinity = Matrix([[1,2,3,4], [5,6,7,8], [964, 342, 4235, 3], [1, 2, 3, 4, 5]])
print(neo + trinity)
