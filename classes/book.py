import numbers


class Book:
    """
    The Book class holds the book_id, book name and other relevant attributes and methods
    associated with its objects.
    """

    def __init__(self, book_id: str = "123", book_title: str = "Learn Python", book_author: str = "John Smith", book_price: float = 10.5):
        """

        :param book_id: The unique identifier number of the book
        :param book_title: The title of the book
        :param book_author: The author name of the book
        :param book_price:  The price of the book
        """
        # Assigning values to non-public attributes with the help of setters
        self.id = book_id
        self.title = book_title
        self.author = book_author
        self.price = book_price

    # Getter
    @property
    def id(self) -> str:
        """
        :return: id of the book
        """
        # non-public attribute to avoid un-authorized access
        return self._book_id

    # Setter
    @id.setter
    def id(self, book_id: str) -> None:
        """
        :param book_id: id of the book
        :return: None
        """
        # Check parameter value and data type
        if not isinstance(book_id,str) or book_id == "":
            raise ValueError("Invalid Book ID")
        # non-public attribute to avoid un-authorized access
        self._book_id = book_id

    # Getter
    @property
    def title(self) -> str:
        """
        :return: title of the book
        """
        # non-public attribute to avoid un-authorized access
        return self._book_title

    # Setter
    @title.setter
    def title(self, book_title: str) -> None:
        """
        :param book_title: title of the book
        :return: None
        """
        # Check parameter value and data type
        if not isinstance(book_title, str) or book_title == "":
            raise ValueError("Invalid Book title")
        # non-public attribute to avoid un-authorized access
        self._book_title = book_title

    # Getter
    @property
    def author(self) -> str:
        """
        :return: author name of the book
        """
        # non-public attribute to avoid un-authorized access
        return self._book_author

    # Setter
    @author.setter
    def author(self, book_author: str) -> None:
        """
        :param book_author: author name of the book
        :return: None
        """
        # Check parameter value and data type
        if not isinstance(book_author, str) or book_author == "":
            raise ValueError("Invalid Book author")
        # non-public attribute to avoid un-authorized access
        self._book_author = book_author

    # Getter
    @property
    def price(self) -> float:
        """
        :return: price of the book
        """
        # non-public attribute to avoid un-authorized access
        return self._book_price

    # Setter
    @price.setter
    def price(self, book_price: float) -> None:
        """
        :param book_price: price of the book
        :return: None
        """
        # Check parameter value and data type
        if not isinstance(book_price, numbers.Complex) or book_price == "":
            raise ValueError("Invalid Book price")
        # non-public attribute to avoid un-authorized access
        self._book_price = book_price

    # Write object as string value
    def __str__(self):
        return f'ID:  {self._book_id}\n' \
               f'Title: {self.title}\n' \
               f'Author: {self.author}\n' \
               f'Price: {self.price}'