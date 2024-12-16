# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Vehicle():
    def __init__(self, max_speed: float, fuel_capacity: float):
        """
        Создание и подготовка к работе объекта "Транспортное средство"

        :param max_speed: Максимальная скорость транспортного средства (в км/ч)
        :param fuel_capacity: Емкость топливного бака (в литрах)

        Примеры:
        >>> car = Vehicle(180, 50)  # вызовет ошибку, так как Vehicle абстрактный класс
        Traceback (most recent call last):
        ...
        TypeError: Can't instantiate abstract class Vehicle with abstract methods drive, refuel
        """
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        if fuel_capacity <= 0:
            raise ValueError("Емкость топливного бака должна быть положительным числом")

        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity

    def drive(self, distance: float) -> float:
        """
        Проехать определенное расстояние.

        :param distance: Расстояние в километрах
        :return: Реально пройденное расстояние
        """
        pass

    def refuel(self, amount: float) -> None:
        """
        Заправить транспортное средство.

        :param amount: Количество топлива для заправки
        """
        pass


class Tree():
    def __init__(self, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        Примеры:
        >>> oak = Tree(10, 50)  # вызовет ошибку, так как Tree абстрактный класс
        Traceback (most recent call last):
        ...
        TypeError: Can't instantiate abstract class Tree with abstract methods grow, photosynthesize
        """
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным")

        self.height = height
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличить рост дерева за указанное количество лет.

        :param years: Количество лет
        """
        pass

    def photosynthesize(self, sunlight_hours: float) -> None:
        """
        Выполнить фотосинтез в течение указанного времени.

        :param sunlight_hours: Количество часов солнечного света
        """
        pass


class Chair():
    def __init__(self, material: str, legs: int):
        """
        Создание и подготовка к работе объекта "Стул"

        :param material: Материал, из которого сделан стул
        :param legs: Количество ножек стула

        Примеры:
        >>> chair = Chair("wood", 4)  # вызовет ошибку, так как Chair абстрактный класс
        Traceback (most recent call last):
        ...
        TypeError: Can't instantiate abstract class Chair with abstract methods sit, move
        """
        if legs <= 0:
            raise ValueError("Количество ножек должно быть положительным числом")
        if not material:
            raise ValueError("Материал должен быть указан")

        self.material = material
        self.legs = legs

    def sit(self, weight: float) -> bool:
        """
        Проверить, выдерживает ли стул заданный вес.

        :param weight: Вес в килограммах
        :return: True, если вес допустим, иначе False
        """
        pass

    def move(self, distance: float) -> None:
        """
        Переместить стул на заданное расстояние.

        :param distance: Расстояние в метрах
        """
        pass


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
