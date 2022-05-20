def raise_exception(class_name: Exception, message: str = "Something went wrong") -> None:
    """
    Raises exception with given exception class and message
    :param class_name: Name reference of the exception class
    :param message: error message of the exception
    :return:
    """
    raise class_name(message)
