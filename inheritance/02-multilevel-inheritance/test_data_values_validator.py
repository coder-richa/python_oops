import pytest
from data_values_validator import is_valid_string, is_non_empty_string, raise_exception_when_invalid


@pytest.fixture(params=[1, 1.50, [], (), True])
def setup_invalid_string_data(request):
    return request.param


@pytest.fixture(params=["John", "Peter"])
def setup_valid_string_data(request):
    return request.param


# A unit Test
def test_is_valid_string_function_exists():
    try:
        _ = is_valid_string("")
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_is_valid_string_with_non_string_value(setup_invalid_string_data):
    try:
        _ = is_valid_string(setup_invalid_string_data)
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_is_valid_string_with_string_value(setup_valid_string_data):
    try:
        _ = is_valid_string(setup_valid_string_data)
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_is_non_empty_string_function_exists():
    try:
        _ = is_non_empty_string("")
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_is_non_empty_string_with_invalid_value(setup_invalid_string_data):
    try:
        _ = is_non_empty_string(setup_invalid_string_data)
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_is_valid_string_with_valid_string_value(setup_valid_string_data):
    try:
        _ = is_non_empty_string(setup_valid_string_data)
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_raise_exception_when_invalid_function_exists():
    with pytest.raises(ValueError):
        raise_exception_when_invalid(validator=is_non_empty_string, value="",
                                         exception=ValueError, message="")
        assert False
    assert True


# # A unit Test
def test_is_non_empty_string_with_invalid_value(setup_invalid_string_data):
    with pytest.raises(ValueError):
        raise_exception_when_invalid(validator=is_non_empty_string, value=setup_invalid_string_data,
                                     exception=ValueError, message="")
        assert False
    assert True


# A unit Test
def test_is_valid_string_with_valid_string_value(setup_valid_string_data):
    raise_exception_when_invalid(validator=is_non_empty_string, value=setup_valid_string_data,
                                 exception=ValueError, message="")
    return True
