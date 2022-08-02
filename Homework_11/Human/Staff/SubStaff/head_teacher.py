from Homework_11.Human.Staff.staff import Staff


class HeadTeacher(Staff):
    def __init__(self, name: str, surname: str, birth_date, reward: int, position='Head teacher'):
        super().__init__(name, surname, position, birth_date, reward)
