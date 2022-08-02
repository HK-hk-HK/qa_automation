from Homework_12.Human.Staff.students_staff import StudentStaff


class Student(StudentStaff):
    def __init__(self, name: str, surname: str, birth_date, reward: int):
        super().__init__(name, surname, birth_date, reward, position='Student')

