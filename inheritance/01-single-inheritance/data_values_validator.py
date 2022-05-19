from typing import Any
from raise_exception import raise_exception


def is_valid_string(string: str) -> bool:
    """
    Checks whether parameter is a string
    :param string: the string value to be tested
    :return: True if argument is of type string
    """
    return isinstance(string, str)


def is_non_empty_string(string: str) -> bool:
    """
    validates if the given string is non-empty
    :param string:  the string value to be tested
    :return: True if non-empty string
    """
    return is_valid_string(string) and string.strip() != ""


def raise_exception_when_invalid(validator: callable, value: Any,\
                                 exception: Exception, message: str) -> None:
    """
    Raise exception in case the validator fails
    :param validator: Function object reference of the validator
    :param value: the value that should be passed to the validator
    :param exception: Exception Class reference to be raised
    :param message: Exception message to be displayed
    :return:
    """
    if not validator(value):
        raise_exception(exception, message)
