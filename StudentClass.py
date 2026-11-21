"""A student class demonstrating encapsulation through public methods."""


class Student:
    """Store a student number and allow the student's name to be updated."""

    def __init__(
        self,
        newStudentNumber: str,
        newStudentFirstName: str,
        newStudentLastName: str,
    ) -> None:
        self._student_number = newStudentNumber
        self._student_first_name = newStudentFirstName
        self._student_last_name = newStudentLastName

    def get_StudentNumber(self) -> str:
        return self._student_number

    def set_StudentNumber(self, value: str) -> None:
        """Report an attempted change and keep the original student number."""
        print("Error - Cannot Change Student Number")

    def get_StudentFirstName(self) -> str:
        return self._student_first_name

    def set_StudentFirstName(self, value: str) -> None:
        self._student_first_name = value

    def get_StudentLastName(self) -> str:
        return self._student_last_name

    def set_StudentLastName(self, value: str) -> None:
        self._student_last_name = value
