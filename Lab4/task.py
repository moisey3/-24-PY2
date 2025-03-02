class MusicalInstrument:
    """
    Базовый класс для музыкальных инструментов.

    :param name: Название инструмента
    :param material: Материал изготовления
    :param sound_range: Диапазон звучания

    :raise TypeError: Если переданы аргументы неверного типа
    :raise ValueError: Если переданы пустые строки
    """

    def __init__(self, name: str, material: str, sound_range: str) -> None:
        if not isinstance(name, str) or not isinstance(material, str) or not isinstance(sound_range, str):
            raise TypeError("Название, материал и диапазон звука должны быть строками.")
        if not name or not material or not sound_range:
            raise ValueError("Название, материал и диапазон звука не могут быть пустыми.")

        self.name = name
        self.material = material
        self.sound_range = sound_range
        self._volume = 5  # Приватный атрибут, чтобы громкость можно было изменять только через методы

    @property
    def volume(self) -> int:
        """Возвращает текущую громкость инструмента."""
        return self._volume

    def play_scale(self) -> str:
        """Играет гамму на инструменте."""
        return f"{self.name} играет гамму."

    def increase_volume(self, amount: int) -> str:
        """
        Увеличивает громкость инструмента.

        :param amount: Величина увеличения громкости
        :raise ValueError: Если значение не положительное
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Уровень увеличения должен быть положительным числом.")
        self._volume = min(10, self._volume + amount)
        return f"{self.name}: громкость увеличена до {self._volume}."

    def decrease_volume(self, amount: int) -> str:
        """
        Уменьшает громкость инструмента.

        :param amount: Величина уменьшения громкости
        :raise ValueError: Если значение не положительное
        """
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Уровень уменьшения должен быть положительным числом.")
        self._volume = max(1, self._volume - amount)
        return f"{self.name}: громкость уменьшена до {self._volume}."

    def __str__(self) -> str:
        return f"{self.name} ({self.material}, {self.sound_range}, Громкость: {self._volume})"

    def __repr__(self) -> str:
        return f"MusicalInstrument(name={self.name!r}, material={self.material!r}, sound_range={self.sound_range!r})"


class StringInstrument(MusicalInstrument):
    """
    Класс для струнных инструментов.

    :param number_of_strings: Количество струн
    :raise ValueError: Если количество струн не положительное
    """

    def __init__(self, name: str, material: str, sound_range: str, number_of_strings: int) -> None:
        super().__init__(name, material, sound_range)
        if not isinstance(number_of_strings, int) or number_of_strings <= 0:
            raise ValueError("Количество струн должно быть положительным целым числом.")
        self._number_of_strings = number_of_strings  # Приватный атрибут, чтобы избежать некорректного изменения

    def play_scale(self) -> str:
        """Играет гамму перебором струн."""
        return f"{self.name} играет гамму перебором струн."

    def __repr__(self) -> str:
        return f"StringInstrument(name={self.name!r}, material={self.material!r}, sound_range={self.sound_range!r}, number_of_strings={self._number_of_strings})"


class WindInstrument(MusicalInstrument):
    """
    Класс для духовых инструментов.

    :param reed_type: Тип трости
    :raise ValueError: Если тип трости не указан
    """

    def __init__(self, name: str, material: str, sound_range: str, reed_type: str) -> None:
        super().__init__(name, material, sound_range)
        if not isinstance(reed_type, str) or not reed_type:
            raise ValueError("Тип трости должен быть непустой строкой.")
        self._reed_type = reed_type  # Приватный атрибут, чтобы ограничить изменение типа трости

    def replace_reed(self) -> str:
        """Заменяет трость на новую."""
        return f"{self.name}: Трость заменена на новую."

    def play_scale(self) -> str:
        """Играет гамму, регулируя подачу воздуха."""
        return f"{self.name} играет гамму, регулируя подачу воздуха."

    def __repr__(self) -> str:
        return f"WindInstrument(name={self.name!r}, material={self.material!r}, sound_range={self.sound_range!r}, reed_type={self._reed_type!r})"


if __name__ == "__main__":
    guitar = StringInstrument("Гитара", "Дерево", "E2-E6", 6)
    clarinet = WindInstrument("Кларнет", "Дерево", "D3-Bb6", "Одинарная трость")

    print(guitar)
    print(clarinet)

    print(guitar.play_scale())
    print(clarinet.play_scale())

    print(guitar.increase_volume(3))
    print(clarinet.decrease_volume(2))

    print(clarinet.replace_reed())
