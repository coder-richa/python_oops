import pytest
from student import Student


# A unit Test
def test_student_class_exists():
    try:
        _ = Student(roll_no="123", course_name="Python", name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
        assert True
    except AssertionError:
        assert False


# A unit Test
def test_non_string_value_roll_no_in_constructor():
    with pytest.raises(ValueError):
        _ = Student(roll_no=1, course_name="Python", name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
        assert False
    assert True


# A unit Test
def test_non_string_value_course_name_in_constructor():
    with pytest.raises(ValueError):
        _ = Student(roll_no="123", course_name=1, name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
        assert False
    assert True


# A unit Test
def test_student_object_creation_with_correct_arguments_in_constructor():
    _ = Student(roll_no="123", course_name="Python", name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
    assert True


# A unit Test
def test_student_object_creation_with_correct_values():
    student = Student(roll_no="123", course_name="Python", name="John", gender="Male", address="13 Mall Road, QLD",
                 contact_number="12345678", email="john@sample.com")
    assert student.name == "John" and student.gender == "Male" \
           and student.address == "13 Mall Road, QLD" and student.contact_number == "12345678"\
           and student.email == "john@sample.com" and student.roll_number == "123" \
           and student.course_name == "Python"
