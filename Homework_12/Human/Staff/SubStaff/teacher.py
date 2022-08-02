from Homework_12.Human.Staff.school_staff import SchoolStaff


class Teacher(SchoolStaff):
    def __init__(self, name: str, surname: str, birth_date, reward: int, position='Teacher'):
        super().__init__(name, surname, birth_date, reward, position)
