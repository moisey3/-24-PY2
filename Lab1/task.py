# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest

class Plate:
    """
    Класс, представляющий тарелку.

    Характеризуется цветом в виде шестнадцатеричного
    числа отображающего цвет RGB, диаметром, и объемом.

    Предоставляет методы для инициализации цвета,проверки
    большая ли тарелка, и сравнения объема двух тарелок.
    """
    def __init__(self, color: str, diametr: Union[int, float], volume: Union[int, float]):
        """
        Инициализация объекта тарелки.

        :param color: Цвет тарелки в виде HEX из 6 символов
        :param diametr: Диаметр тарелки
        :param volume: Объем тарелки

        :raise TypeError: Не правильный тип значения диаметра или объема.
        :raise ValueError: Диаметр или объем не могут быть <= 0.

        Примеры:
        >>> plate1 = Plate("48dcd7", 200, 110)
        """
        self.color = None
        self.init_color(color)

        if not isinstance(diametr, (int, float)):
            raise TypeError("Не правильный тип значения диаметра")
        if diametr <= 0:
            raise ValueError("Диаметр не может быть <= 0")
        self.diametr = diametr

        if not isinstance(volume, (int, float)):
            raise TypeError
        if volume < 0:
            raise ValueError
        self.volume = volume

    def init_color(self, color: str) -> None:
        """
        Инициализация цвета тарелки.
        """
        # Проверка длины
        if len(color) != 6:
            raise ValueError("Ошибка: число должно содержать ровно 6 символов.")

        # Проверка на шестнадцатеричный формат
        try:
            int(color, 16)  # Пробуем преобразовать строку в 16-ричное число
        except ValueError:
            raise ValueError("Ошибка: введено некорректное шестнадцатеричное число")

        # Если проверки прошли успешно, устанавливаем значение
        self.color = color

    def is_large(self) -> bool:
        """Метод, который определяет, большая ли тарелка по объему"""
        ...

    def compare_size(self, other) -> str:
        """Метод для сравнения размера двух тарелок по объему"""
        ...


class Restaurant:
    """
    Класс, представляющий ресторан.

    Характеризуется названием, типом кухни и средним чеком.
    Предоставляет методы для принятия заказов,
    приготовления блюд и подачи еды.

    """

    def __init__(self, name: str, cuisine_type: str, average_bill: float):
        """
        Инициализация объекта ресторана.

        :param name: Название ресторана.
        :param cuisine_type: Тип кухни.
        :param average_bill: Средний чек (стоимость одного заказа).

        Примеры:
        >>> restaurant = Restaurant("La Pizzeria", "Итальянская", 1500)
        """
        if not name or not cuisine_type:
            raise ValueError("Название ресторана и тип кухни не могут быть пустыми.")
        if average_bill <= 0:
            raise ValueError("Средний чек не может быть меньше или равен нулю.")

        self.name = name
        self.cuisine_type = cuisine_type
        self.average_bill = average_bill

    def take_order(self, order: str) -> str:
        """
        Принять заказ от клиента. Сообщает, что заказ принят.

        :param order: Заказ клиента.

        Примеры:
        >>> restaurant = Restaurant("La Pizzeria", "Итальянская", 1500)
        >>> order1 = restaurant.take_order("Пицца Маргарита")
        """
        return f"Заказ принят: {order}"

    def cook_dish(self, dish: str) -> str:
        """
        Приготовить блюдо. Сообщает, что заказ готовится.

        :param dish: Название блюда.
        """
        ...

    def serve_food(self, dish: str):
        """
        Подать еду клиенту. Сообщает, что блюдо подано.

        :param dish: Название блюда.
        """
        ...


class Wallet:
    """
    Класс, представляющий кошелек.

    Характеризуется балансом, количеством карт и
    типом кошелька. Предоставляет методы для
    пополнения кошелька, снятия денег и добавления карт.
    """

    def __init__(self, balance: float, num_cards: int):
        """
        Инициализация объекта кошелька.

        :param balance: Баланс кошелька.
        :param num_cards: Количество карт в кошельке.

        :raise ValueError: Если balance < 0, Если num_cards > 5.

        Примеры:
        >>> wallet = Wallet(1000.0, 2)
        """
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        if num_cards > 5:
            raise ValueError("Количество карт не может превышать 5.")

        self.balance = balance
        self.num_cards = num_cards

    def add_money(self, amount: float) -> str:
        """
        Пополнение кошелька. Возвращает сообщение о пополнении баланса.

        :param amount: Сумма для пополнения

        :raise ValueError: Если amount < 0

        Примеры:
        >>> wallet = Wallet(1000.0, 2)
        >>> add_money1 = wallet.add_money(500)
        """
        if amount < 0:
            raise ValueError("Сумма пополнения не может быть отрицательной.")
        self.balance += amount
        return f"Баланс пополнен на {amount}. Текущий баланс: {self.balance}"

    def withdraw_money(self, amount: float) -> str:
        """
        Снятие денег с кошелька. Возвращает сообщение о снятии денег с баланса.

        :param amount: Сумма для снятия

        :raise ValueError: Если amount > balance (недостаточно средств на балансе).
        """
        if amount > self.balance:
            raise ValueError("Недостаточно средств на балансе.")
        self.balance -= amount
        return f"Снято {amount}. Текущий баланс: {self.balance}"

    def add_card(self) -> str:
        """
        Добавление карты в кошелек. Возвращает сообщение о добавленной карте.

        :raise ValueError: Если количество карт уже достигло максимума (5)
        """
        if self.num_cards >= 5:
            raise ValueError("Невозможно добавить карту. Максимальное количество карт — 5.")
        self.num_cards += 1
        return f"Добавлена карта. Количество карт в кошельке: {self.num_cards}"

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass

