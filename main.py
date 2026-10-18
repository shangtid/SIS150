"""Run a short demonstration of the Student class."""

from StudentClass import Student


def main():
    student = Student("1001", "Alex", "Smith")
    print("Student number:", student.get_StudentNumber())
    print("Original name:", student.get_StudentFirstName(), student.get_StudentLastName())

    student.set_StudentFirstName("Jordan")
    student.set_StudentLastName("Taylor")
    print("Updated name:", student.get_StudentFirstName(), student.get_StudentLastName())

    student.set_StudentNumber("2002")
    print("Student number after attempted change:", student.get_StudentNumber())


if __name__ == "__main__":
    main()
