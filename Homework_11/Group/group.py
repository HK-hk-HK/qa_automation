from Homework_11.Human.Staff.SubStaff.student import Student
from Homework_11.Human.Staff.SubStaff.teacher import Teacher


class Group:
    def __init__(self, classroom_teacher: Teacher, students: [Student] = None):
        if students is None:
            students = []
        self.__classroom_teacher = classroom_teacher
        self.__students = students

    def __repr__(self) -> str:
        return f'{self.__classroom_teacher}, {self.__students}'

    @property
    def classroom_teacher(self) -> Teacher:
        return self.__classroom_teacher

    @classroom_teacher.setter
    def classroom_teacher(self, new_class_teacher):
        self.__classroom_teacher = new_class_teacher

    def get_students(self) -> [Student]:
        return self.__students

    def add_student(self, student):
        self.__students.append(student)

    def remove_student(self, student):
        self.__students.remove(student)


