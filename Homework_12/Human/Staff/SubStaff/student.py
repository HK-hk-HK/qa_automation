from Homework_12.Human.Staff.students_staff import StudentStaff
from faker import Faker
from datetime import date
from Homework_12.exceptions import InvalidRewardValueError


class Student(StudentStaff):
    def __init__(self, name: str, surname: str, birth_date, reward: int):
        super().__init__(name, surname, birth_date, reward, position='Student')

fake = Faker()

if __name__ == '__main__':
    student1 = Student(fake.unique.first_name(), fake.unique.last_name(), date(2001, 12, 15), 1)
    # print(student1.__dict__)
    print(student1)
    print(student1.age)
    print(student1.reward)
