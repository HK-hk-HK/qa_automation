from Homework_12.Human.Staff.school_staff import SchoolStaff


class OtherStaff(SchoolStaff):
    def __init__(self, name: str, surname: str, birth_date, reward: int, position='Other Staff'):
        super().__init__(name, surname, birth_date, reward, position)

