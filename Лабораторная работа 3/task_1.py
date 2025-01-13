class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        if not isinstance(pages, int):
            raise TypeError("pages must be an integer.")
        super().__init__(name, author)
        self.pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        if not isinstance(duration, float):
            raise TypeError("duration must be a float.")
        super().__init__(name, author)
        self.duration = duration