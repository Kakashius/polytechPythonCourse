class Vehicle:
    """
    Базовый класс, представляющий транспортное средство.
    """
    def __init__(self, brand: str, model: str, year: int):
        """
        Инициализация экземпляра класса Vehicle.

        :param brand: Марка транспортного средства.
        :param model: Модель транспортного средства.
        :param year: Год выпуска транспортного средства.
        """
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = 0  # Защищённый атрибут для хранения пробега

    def __str__(self) -> str:
        """
        Строковое представление транспортного средства.

        :return: Строка, описывающая транспортное средство.
        """
        return f"{self.year} {self.brand} {self.model}"

    def __repr__(self) -> str:
        """
        Техническое строковое представление транспортного средства.

        :return: Строка с детальной информацией о транспортном средстве.
        """
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self.year})"

    def drive(self, distance: int) -> None:
        """
        Симуляция вождения транспортного средства.

        :param distance: Расстояние для поездки в километрах.
        """
        if distance > 0:
            self._mileage += distance
        else:
            raise ValueError("Расстояние должно быть положительным.")


class Car(Vehicle):
    """
    Класс, представляющий автомобиль, наследующийся от Vehicle.
    """
    def __init__(self, brand: str, model: str, year: int, seating_capacity: int):
        """
        Инициализация экземпляра класса Car.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        :param seating_capacity: Вместимость автомобиля.
        """
        super().__init__(brand, model, year)
        self.seating_capacity = seating_capacity

    def __str__(self) -> str:
        """
        Перегруженное строковое представление автомобиля.

        :return: Строка, описывающая автомобиль с указанием вместимости.
        """
        return f"{super().__str__()} с вместимостью {self.seating_capacity} мест"

    def park(self) -> str:
        """
        Симуляция парковки автомобиля.

        :return: Сообщение о том, что автомобиль припаркован.
        """
        return f"{self.brand} {self.model} припаркован."

    def drive(self, distance: int, passengers: int = 0) -> None:
        """
        Перегруженный метод drive с учётом пассажиров.

        :param distance: Расстояние для поездки в километрах.
        :param passengers: Количество пассажиров в автомобиле.

        Причина перегрузки: Чтобы учитывать влияние пассажиров на динамику вождения.
        """
        if passengers > self.seating_capacity:
            raise ValueError("Слишком много пассажиров для этого автомобиля.")
        print(f"Едем с {passengers} пассажирами...")
        super().drive(distance)


if __name__ == "__main__":
    # Write your solution here
    car = Car("Toyota", "Camry", 2022, 5)
    print(car)
    car.drive(100, passengers=4)
    print(repr(car))
    pass
