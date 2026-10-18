"""A student class demonstrating encapsulation through public methods."""


class Student:
    def __init__(self, newStudentNumber, newStudentFirstName, newStudentLastName):
        self._StudentNumber = newStudentNumber
        self._StudentFirstName = newStudentFirstName
        self._StudentLastName = newStudentLastName

    def get_StudentNumber(self):
        return self._StudentNumber

    def set_StudentNumber(self, value):
        # The public interface does not allow changing the student number.
        print("Error - Cannot Change Student Number")

    def get_StudentFirstName(self):
        return self._StudentFirstName

    def set_StudentFirstName(self, value):
        self._StudentFirstName = value

    def get_StudentLastName(self):
        return self._StudentLastName

    def set_StudentLastName(self, value):
        self._StudentLastName = value
