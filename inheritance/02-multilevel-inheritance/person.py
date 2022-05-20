from data_values_validator import is_non_empty_string, raise_exception_when_invalid


class Person:

    def __init__(self, name: str, gender: str, address: str,
                 contact_number: str, email: str):
        """
        Constructor of Person class
        :param name: holds name of the person
        :param gender: holds gender of the person
        :param address: holds address of the person
        :param contact_number: holds contact number of the person
        :param email: holds email of the person
        """
        self.name = name
        self.gender = gender
        self.address = address
        self.contact_number = contact_number
        self.email = email

    @property
    def name(self) -> str:
        """
        :return: name of the person
        """
        return self._name

    @name.setter
    def name(self, person_name: str):
        raise_exception_when_invalid(validator=is_non_empty_string,value=person_name,
                                     exception=ValueError, message="Invalid name")
        self._name = person_name

    @property
    def gender(self) -> str:
        """
        :return: gender of the person
        """
        return self._gender

    @gender.setter
    def gender(self, person_gender: str):
        raise_exception_when_invalid(validator=is_non_empty_string, value=person_gender,
                                     exception=ValueError, message="Invalid gender")
        self._gender = person_gender

    @property
    def address(self) -> str:
        """
         address of the person
        :return:
        """
        return self._address

    @address.setter
    def address(self, person_address: str):
        raise_exception_when_invalid(validator=is_non_empty_string, value=person_address,
                                     exception=ValueError, message="Invalid address")
        self._address = person_address

    @property
    def contact_number(self) -> str:
        """
        :return: contact number of the person
        """
        return self._contact_number

    @contact_number.setter
    def contact_number(self, person_contact_number: str):
        raise_exception_when_invalid(validator=is_non_empty_string, value=person_contact_number,
                                     exception=ValueError, message="Invalid contact number")
        self._contact_number = person_contact_number

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, person_email: str):
        raise_exception_when_invalid(validator=is_non_empty_string, value=person_email,
                                     exception=ValueError, message="Invalid email")
        self._email = person_email

    def __str__(self):
        return f'Name:  {self.name}\n' \
               f'Gender: {self.gender}\n' \
               f'Address: {self.address}\n' \
               f'Contact Number: {self.contact_number}\n' \
               f'Email: {self.email}'
