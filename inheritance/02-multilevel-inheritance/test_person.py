import pytest
from person import Person


# A unit Test
def test_person_class_exists():
    try:
        _ = Person(name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_non_string_value_name_in_constructor():
    with pytest.raises(ValueError):
        _ = Person(name=1, gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
        assert False
    assert True


# A unit Test
def test_non_string_value_gender_in_constructor():
    with pytest.raises(ValueError):
        _ = Person(name="John", gender=1, address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
        assert False
    assert True


# A unit Test
def test_non_string_value_address_in_constructor():
    with pytest.raises(ValueError):
        _ = Person(name="John", gender="Male", address=13,
                 contact_number="12345678", email="john@sample.com")
        assert False
    assert True


# A unit Test
def test_non_string_value_contact_number_in_constructor():
    with pytest.raises(ValueError):
        _ = Person(name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number=12345678, email="john@sample.com")
        assert False
    assert True


# A unit Test
def test_non_string_value_email_in_constructor():
    with pytest.raises(ValueError):
        _ = Person(name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email=1)
        assert False
    assert True


# A unit Test
def test_person_object_creation_with_correct_arguments_in_constructor():
    _ = Person(name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
    assert True


# A unit Test
def test_person_object_creation_with_correct_values():
    person = Person(name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
    assert person.name == "John" and person.gender == "Male" \
           and person.address == "13 Mall Road, QLD" and person.contact_number == "12345678"\
           and person.email == "john@sample.com"
