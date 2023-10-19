import time


# Создайте класс МояСтрока где будут доступны все возможности
# str и дополнительно хранится имя автора строки и время создания (time.time)

class Mystr(str):
    def __new__(cls, value, name):
        """ Создание нового объекта """
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.time()
        return instance


# my_str = Mystr('Значение', 'Tumen')
# print(my_str.upper())
# print(my_str.name)
# print(help(Mystr))


# Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса,
# старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов, которые также являются свойствами экземпляра.

class Archive:
    """
    Класс, который хранит пару свойств число и строку. При создании нового экземпляра
    сохраняет число и строку прошлого созданного экземпляра в общий список. К которому можно обратиться
    со свех экземпляров
    """
    _instance = None

    def __new__(cls, number, string):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_number = []
            cls._instance.list_string = []

        cls._instance.list_number.append(number)
        cls._instance.list_string.append(string)
        return cls._instance

    def __init__(self, number, string):
        self.number = number
        self.string = string

    def __str__(self):
        return f'Экземпляр класса Achive с номером {self.number}'

    def __repr__(self):
        return f'{self.number} {self.string}'



# print(help(Archive))
# my_archive1 = Archive(15, 'Hello')
# print(my_archive1.list_number)
# print(my_archive1.list_string)
#
# my_archive2 = Archive(56, 'world')
# print(my_archive2.list_number)
# print(my_archive2.list_string)
#
# my_archive3 = Archive(60, 'people')
# print(my_archive3.list_number)
# print(my_archive3.list_string)



# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.


class Rectangle:
    def __init__(self, length, width=None):
        if not width:
            self.width = length
        else:
            self.width = width
        self.length = length

    def get_perimetr(self):
        return 2 * self.length + 2 * self.width

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        width = self.width
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
rect3 = rect1 - rect2
print(rect1.get_area(), rect2.get_area())
print(rect1 == rect2)
print(rect1 > rect2)
print(rect1 < rect2)
print(rect1 >= rect2)
print(rect1 <= rect2)
print(rect1 != rect2)
