from raise_exception import raise_exception
import pytest


# A unit Test
def test_raise_exception_function_exists():
    try:
        raise_exception(class_name=ValueError,message="")
        assert True
    except AssertionError:
        assert False
    except ValueError:
        assert True


# A unit Test
def test_raise_exception_function():
    with pytest.raises(ValueError):
        raise_exception(class_name=ValueError,message="")
        assert False
    assert True
