import math

from Homework_12.Group.group import Group
from Homework_12.Human.Staff.SubStaff.director import Director
from Homework_12.Human.Staff.SubStaff.head_teacher import HeadTeacher
from Homework_12.Human.Staff.SubStaff.other_staff import OtherStaff
from Homework_12.Human.Staff.SubStaff.teacher import Teacher


class School:
    # property
    education_cost = 4999

    # methods
    def __init__(self,
                 director: Director,
                 head_teacher: HeadTeacher,
                 teachers: [Teacher] = None,
                 other_staff: [OtherStaff] = None,
                 groups: [Group] = None):
        if teachers is None:
            teachers = []
        if other_staff is None:
            other_staff = []
        if groups is None:
            groups = []
        self.__director = director
        self.__head_teacher = head_teacher
        self.__teachers = teachers
        self.__other_staff = other_staff
        self.__groups = groups

    def __repr__(self) -> str:
        return f'{self.__director}, ' \
               f'{self.__head_teacher}, ' \
               f'{self.__teachers}, ' \
               f'{self.__other_staff}, ' \
               f'{self.__groups}'

    @property
    def director(self) -> Director:
        return self.__director

    @director.setter
    def director(self, new_director):
        self.__director = new_director

    @property
    def head_teacher(self) -> HeadTeacher:
        return self.__head_teacher

    @head_teacher.setter
    def head_teacher(self, new_head_teacher):
        self.__head_teacher = new_head_teacher

    def get_teachers(self) -> [Teacher]:
        return self.__teachers

    def add_teacher(self, teacher):
        self.__teachers.append(teacher)

    def remove_teacher(self, teacher):
        self.__teachers.remove(teacher)

    def get_other_staff(self) -> [OtherStaff]:
        return self.__other_staff

    def add_other_staff(self, other_staff):
        self.__other_staff.append(other_staff)

    def remove_other_staff(self, other_staff):
        self.__other_staff.remove(other_staff)

    def get_groups(self) -> [Group]:
        return self.__groups

    def add_group(self, group):
        self.__groups.append(group)

    def remove_group(self, group):
        """
        The method removes group from school, but doesn't remove actual group.
        The group's students are evenly distributed to other school groups otherwise the last group is completely
        removed from the school instance.

        :param group: the group to be removed
        :return: None
        """
        actual = self.actual_students_number()
        min_qt = self.min_students_quota()
        students_of_suspended_group = group.get_students()
        suspended_students_num = len(students_of_suspended_group)
        new_actual = actual - suspended_students_num
        groups_count = len(self.__groups)
        if new_actual < min_qt and groups_count >= 2:
            groups_count = len(self.__groups)
            current_group_i = 1
            for student in students_of_suspended_group:
                nth_group = current_group_i % groups_count
                self.__groups[nth_group - 1].add_student(student)
                current_group_i += 1
        self.__groups.remove(group)

    def calculate_budget(self) -> int:
        """
        Calculate school staff(director, head teacher, class teacher, teachers, other staff) reward(salary) sum

        :return: counted school budget in type int
        """
        budget = 0
        if len(self.__groups) != 0:
            for group in self.__groups:
                budget += group.classroom_teacher.reward
        if self.__director:
            budget += self.__director.reward
        if self.__head_teacher:
            budget += self.__head_teacher.reward
        if len(self.__teachers) != 0:
            for teacher in self.__teachers:
                budget += teacher.reward
        if len(self.__other_staff) != 0:
            for other_staff in self.__other_staff:
                budget += other_staff.reward
        return budget

    def actual_students_number(self) -> int:
        """
        Counts students added to the school instance

        :return: students number in type int that have been added to the school instance
        """
        students_number = 0
        for group in self.__groups:
            students_number += len(group.get_students())
        return students_number

    def min_students_quota(self) -> int:
        """
        Calculates min required students number to cower the school instance staff salaries
        depending on static method value '''education_cost''' and calculated school instance staff budget

        :return: min required students number in type int
        """
        return math.ceil(self.calculate_budget() / type(self).education_cost)

    def need_students(self) -> int:
        """
        Calculates required students number excluding already existing students in the school instance

        :return: required students number
        """
        return self.min_students_quota() - self.actual_students_number()


