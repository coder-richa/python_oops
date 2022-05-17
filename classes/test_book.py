import pytest
from book import Book


# A unit Test
def test_book_class_exists():
    """
    Test whether book class is available
    """
    try:
        book = Book()
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_non_string_value_book_id_in_constructor():
    """
    Test whether book class accepts non-string value of id in book creation
    """
    with pytest.raises(ValueError):
        _ = Book(book_id=1)
        assert False
    assert True


# A unit Test
def test_non_string_value_book_title_in_constructor():
    """
    Test whether book class accepts non-string value of title in book creation
    """
    with pytest.raises(ValueError):
        _ = Book(book_id="Book-1", book_title=123)
        assert False
    assert True


# A unit Test
def test_non_string_value_book_author_in_constructor():
    """
    Test whether book class accepts non-string value of author in book creation
    """
    with pytest.raises(ValueError):
        _ = Book(book_id="Book-1", book_title="Title", book_author=123)
        assert False
    assert True


# A unit Test
def test_non_float_value_book_price_in_constructor():
    """
    Test whether book class accepts non-floating point value of price in book creation
    """
    with pytest.raises(ValueError):
        _ = Book(book_id="Book-1", book_title="Title", book_author="James Bond", book_price="price")
        assert False
    assert True


# A unit Test
def test_object_creation_with_correct_arguments_in_constructor():
    """
    Test whether book class accepts correct parameters in book creation
    """
    _ = Book(book_id="Book-1", book_title="Title", book_author="James Bond", book_price=10)
    assert True


# A unit Test
def test_object_creation_with_correct_values():
    """
    Test whether object has correct values assigned to all attributes
    """
    book = Book(book_id="Book-1", book_title="Title", book_author="James Bond", book_price=10)
    assert book.id == "Book-1" and book.title == "Title" \
           and book.author == "James Bond" and book.price == 10

# A unit Test
def test_object_string_format():
    """
    Test whether object has correct values assigned to all attributes
    """
    book = Book(book_id="Book-1", book_title="Title", book_author="James Bond", book_price=10)
    s = "ID:  Book-1\n" \
        "Title: Title\n" \
        "Author: James Bond\n" \
        "Price: 10"
    assert str(book) == s



