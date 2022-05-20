from raise_exception import raise_exception
from student import Student
from sports import Sports


class Player(Student):

    def __init__(self, sports: Sports, roll_no: str, course_name: str, name: str, gender: str,
                 address: str, contact_number: str, email: str) -> None:
        """
        Player class
        :param sports: Student Sports choice
        :param roll_no: Student Roll Number
        :param course_name: Student course name
        :param name: student name
        :param gender: student gender
        :param address: student address
        :param contact_number: student contact number
        :param email: student email address
        """
        self.sports = sports
        Student.__init__(self, roll_no=roll_no, course_name=course_name, name=name,
                        gender=gender, address=address,
                        contact_number=contact_number, email=email)

    @property
    def sports(self) -> Sports:
        """
        :return: sports
        """
        return self._sports

    @sports.setter
    def sports(self, sport: Sports) -> None:
        """
        :param sport: sports played by the student
        :return: None
        """
        if not isinstance(sport, Sports):
            raise_exception(class_name=ValueError, message="Invalid Sport")
        self._sports = sport

    def __str__(self) -> str:
        return f'Sport: {self.sports.value}\n' \
               f'{Student.__str__(self)}'
