class Book:
    """ Базовый класс книги. """
    BOOK_TYPE = None

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author


    def __str__(self):
        return f'Книга "{self._name}". Автор {self._author}, тип книги: {self.BOOK_TYPE}.'

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    BOOK_TYPE = "Бумажная"

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = None
        self.init_pages(pages)

    def init_pages(self, pages):
        if pages <= 0:
            raise ValueError
        if not isinstance(pages, int):
            raise TypeError
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    BOOK_TYPE = "Аудио"

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = None
        self.init_duration(duration)

    def init_duration(self, duration):
        if duration <= 0:
            raise ValueError
        if not isinstance(duration, (int, float)):
            raise TypeError
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

if __name__ == "__main__":
    book1 = PaperBook("История Вани", "Ваня", 200)
    book2 = Book("История Дани", "Даня")
    book3 = AudioBook("История Вани", "Ваня", 1)
    print(book1)
    print(book2)
    print(book3)
