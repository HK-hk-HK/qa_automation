from Homework_11.Human.Staff.staff import Staff


class Director(Staff):
    def __init__(self, name: str, surname: str, birth_date, reward: int, position='Director'):
        super().__init__(name, surname, position, birth_date, reward)



