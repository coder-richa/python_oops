from data_values_validator import is_non_empty_string, raise_exception_when_invalid
from person import Person


class Student(Person):

    def __init__(self, roll_no: str, course_name: str, name: str, gender: str,
                 address: str, contact_number: str, email: str) -> None:
        """
        Student class
        :param roll_no: Student Roll Number
        :param course_name: Student course name
        :param name: student name
        :param gender: student gender
        :param address: student address
        :param contact_number: student contact number
        :param email: student email address
        """
        self.roll_number = roll_no
        self.course_name = course_name
        Person.__init__(self, name=name, gender=gender, address=address,
                        contact_number=contact_number, email=email)

    @property
    def roll_number(self) -> str:
        return self._roll_no

    @roll_number.setter
    def roll_number(self, roll_no: str) -> None:
        raise_exception_when_invalid(validator=is_non_empty_string, value=roll_no,
                                     exception=ValueError, message="Invalid roll number")
        self._roll_no = roll_no

    @property
    def course_name(self) -> str:
        return self._course_name

    @course_name.setter
    def course_name(self, course_name: str) -> None:
        raise_exception_when_invalid(validator=is_non_empty_string, value=course_name,
                                     exception=ValueError, message="Invalid course name")
        self._course_name = course_name

    def __str__(self) -> str:
        return f'Roll Number: {self.roll_number}\n' \
               f'Course: {self.course_name}\n' \
               f'{Person.__str__(self)}'
