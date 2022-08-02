from datetime import date

"""
Завдання №1

Розробити клас Людина. Людина має:
Ім'я, Прізвище, Вік (атрибут але ж змінний), Стать

Люди можуть:
Їсти, Спати, Говорити, Ходити, Стояти, Лежати

Також ми хочемо контролювати популяцію людства. Змінювати популяцію можемо в __init__.
Треба сказати, що доступ до статичних полів класу з __init__ не можуть іти через НазваКласу.статичий_атрибут,
позаяк ми не може бачити імені класу. Але натомість ми можемо сказати self.__class__.static_attribute.
"""

class Human:
    # properties
    humans_population = 0

    # methods
    def __init__(self, name: str, surname: str, gender: str, birth_date):
        """
        Initiates class object after declaration

        This method allows to describe class object of "Human" class and set unique values for each one

        :param name: given human's name in type str
        :param surname: given human's surname in type str
        :param gender: human's gender in type str (preferred values: 'm', 'male', 'man', 'f', 'female', 'w', 'woman')
        :param birth_date: with imported 'datetime' module input should be in the following format:
         '''birth_date = date.today(yyyy, m, d)''' - if 1-9 month/day of birth
         '''birth_date = date.today(yyyy, mm, dd)''' - if 10-12 month and 10-31 day of birth
        """
        self.name = name
        self.surname = surname
        self.gender = gender
        self.__birth_date = birth_date
        self.__class__.humans_population += 1

    @property
    def counts_age(self) -> int:
        """
        Counts class object's age

        :return: counted age in type int
        """
        return (date.today() - self.birth_date).days // 365

    @property
    def birth_date(self) -> date:
        """
        Displays actual class object's age

        :return: actual age in type int
        """
        return self.__birth_date

    def __repr__(self) -> str:
        """
        Doesn't take any arguments and generates main description about declared class object

        :return: greeting in type str of declared class object depending on inputted value for 'gender' parameter
        """
        if self.gender in ('m', 'male', 'man'):
            return f"Hey, meet {self.name} {self.surname}! " \
               f"He is {self.counts_age} years old and I'm going to tell about him a little bit"
        elif self.gender in ('f', 'female', 'w', 'woman'):
            return f"Hey, meet {self.name} {self.surname}! " \
               f"She is {self.counts_age} years old and I'm going to tell about her a little bit"
        else:
            return f"{self.name} {self.surname}, {self.counts_age} years old. That's it"

    def eat(self, dish: str):
        """
        Takes 1 argument in type str that mean's class object's favourite dish

        :param dish: class object's favourite dish in type str
        :return: None
        """
        print(f"{self.name}'s favourite dish is {dish}")

    def sleep(self, sleeping_hours: float):
        """
        Takes 1 argument in type float that mean's class object's sleeping hours needed for energy recovery

        :param sleeping_hours: class object's sleeping hours needed for energy recovery
        :return: None
        """
        print(f"{self.name} usually sleeps {sleeping_hours} hours")

    def talk(self):
        """
        Doesn't take any arguments and describes how talkative is class object

        :return: None
        """
        if self.gender in ('m', 'male', 'man'):
            print(f"{self.name} sometimes talking to himself")
        elif self.gender in ('f', 'female', 'w', 'woman'):
            print(f"{self.name} sometimes talking to herself")
        else:
            print(f"{self.name} doesn't really like to talk")

    def walk(self):
        """
        Doesn't take any arguments and describes that class object likes walking

        :return: None
        """
        print(f"{self.name} prefers walking instead of taking the subway or taxi")

    def stand(self):
        """
        Doesn't take any arguments and describes case of class object standing

        :return: None
        """
        print(f"{self.name} has a high desk at home so {self.name} can work standing up.")

    def lie(self):
        """
        Doesn't take any arguments and describes case of class object lying down

        :return: None
        """
        print(f"{self.name} used to read books lying down")

    def __del__(self) -> str:
        """
        The function doesn't take any arguments. It deletes class object if recall this function and mention existing class object
        (e.g. '''del misha''')

        :return: special note in type str about deleting of class object
        """
        return f"Delete {self.name} {self.surname}"




