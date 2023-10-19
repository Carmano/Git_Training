import json

# Доработаем задачу 1. Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.


# class Factorial:
#     def __init__(self, k):
#         self.k = k
#         self.res_list = []
#
#     def __call__(self, num):
#         res = 1
#         for i in range(1, num + 1):
#             res *= i
#
#         self.res_list.append((num, res))
#         if len(self.res_list) > self.k:
#             self.res_list.pop(0)
#
#         return res
#
#     def __str__(self):
#         return str(self.res_list)
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         my_dict = {}
#         for key, value in self.res_list:
#             my_dict[key] = value
#         with open('res_json.json', 'w', encoding='utf-8') as f_json:
#             json.dump(my_dict, f_json)
#
#
# with Factorial(4) as my_fact:
#     print(my_fact(5))
#     print(my_fact(6))
#     print(my_fact(7))
#     print(my_fact(2))
#     print(my_fact(10))
#     print(my_fact(11))
#
#
# class Fact_gen:
#     def __init__(self, *args):
#         if len(args) == 3:
#             self.start, self.stop, self.step = args
#         elif len(args) == 2:
#             self.start, self.stop = args
#             self.step = 1
#         else:
#             self.stop = args[0]
#             self.start = 1
#             self.step = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.start < self.stop:
#             fact = 1
#             for num in range(1, self.start + 1):
#                 fact *= num
#             self.start += self.step
#             return fact
#         raise StopIteration
#
#
# gener = Fact_gen(1, 50)
# for fact in gener:
#     print(fact)


# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

class Rectangle:
    def __init__(self, length, width=None):
        if not width:
            self._width = length
        else:
            self._width = width
        self._length = length

    @property
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @width.setter
    def width(self, value):
        if value >= 0:
            self._width = value
        else:
            raise ValueError('Не правильный аргумент')

    @length.setter
    def length(self, value):
        if value >= 0:
            self._length = value
        else:
            raise ValueError('Не правильный аргумент')

    def get_perimetr(self):
        return 2 * self._length + 2 * self._width

    def get_area(self):
        return self._length * self._width

    def __add__(self, other):
        width = self._width
        perimetr = self.get_perimetr() + other.get_perimetr()
        length = (perimetr - 2 * width) / 2
        return Rectangle(width, length)

    def __sub__(self, other):
        perimetr = abs(self.get_perimetr() - other.get_perimetr())
        length = int(perimetr / 4)
        width = perimetr / 2
        return Rectangle(length, width)

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()


rect1 = Rectangle(30, 5)
rect2 = Rectangle(26, 6)
print(rect1.width)
rect1.width = -100
print(rect1.width)
