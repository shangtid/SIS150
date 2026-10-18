# Student Encapsulation Lab

A Python course example demonstrating a constructor, nonpublic attributes,
accessor methods (getters), and mutator methods (setters).

## Run

Requires Python 3. No additional packages are needed.

```sh
python main.py
```

## Expected output

```text
Student number: 1001
Original name: Alex Smith
Updated name: Jordan Taylor
Error - Cannot Change Student Number
Student number after attempted change: 1001
```

## How it works

- `__init__` sets the student's number, first name, and last name.
- Getter methods retrieve those values.
- Name setters allow updates to the first and last name.
- The student-number setter displays an error and leaves the number unchanged.

A leading underscore indicates that an attribute is nonpublic by convention
in Python. It does not enforce privacy or prevent direct modification.
The student number is protected through this class's public methods.

`StudentClass.py` contains the class; `main.py` demonstrates its behavior.
This version corrects syntax and inconsistent capitalization in the supplied
course example and adds a runnable demonstration.
