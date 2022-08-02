from datetime import date


class Human:
    # methods
    def __init__(self, name: str, surname: str, birth_date: date):
        self.name = name
        self.surname = surname
        self.__birth_date = birth_date

    @property
    def age(self) -> int:
        """
        Counts class object's age

        :return: counted age in type int
        """
        return (date.today() - self.birth_date).days // 365

    @property
    def birth_date(self) -> date:
        """
        Displays birth date

        :return: Birth date in type date (yyyy-mm-dd)
        """
        return self.__birth_date

