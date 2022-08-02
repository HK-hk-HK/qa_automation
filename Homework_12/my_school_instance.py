from datetime import date
from faker import Faker

from Homework_12.Group.group import Group
from Homework_12.Human.Staff.SubStaff.director import Director
from Homework_12.Human.Staff.SubStaff.head_teacher import HeadTeacher
from Homework_12.Human.Staff.SubStaff.other_staff import OtherStaff
from Homework_12.Human.Staff.SubStaff.student import Student
from Homework_12.Human.Staff.SubStaff.teacher import Teacher
from Homework_12.School.school import School

fake = Faker()

if __name__ == '__main__':
    student1 = Student(fake.unique.first_name(), fake.unique.last_name(), date(2001, 12, 15), 1)
    student2 = Student(fake.unique.first_name(), fake.unique.last_name(), date(2004, 2, 5), 1)
    student3 = Student(fake.unique.first_name(), fake.unique.last_name(), date(2006, 3, 6), 1)
    student4 = Student(fake.unique.first_name(), fake.unique.last_name(), date(2009, 10, 1), 5)
    student5 = Student(fake.unique.first_name(), fake.unique.last_name(), date(2008, 11, 2), 4)
    student6 = Student(fake.unique.first_name(), fake.unique.last_name(), date(2010, 12, 3), 3)

    class_teacher1 = Teacher(fake.unique.first_name(), fake.unique.last_name(), date(1989, 1, 1), 20000, 'class teacher1')
    class_teacher2 = Teacher(fake.unique.first_name(), fake.unique.last_name(), date(1982, 11, 12), 20000, 'class teacher2')
    class_teacher3 = Teacher(fake.unique.first_name(), fake.unique.last_name(), date(1983, 1, 13), 20000, 'class teacher2')

    group1 = Group(class_teacher1)
    group2 = Group(class_teacher2)
    group3 = Group(class_teacher3)

    print(group1)
    group1.add_student(student1)
    group1.add_student(student4)
    print(group1)
    print(group2)
    group2.add_student(student2)
    group2.add_student(student5)
    print(group2)
    print(group3)
    group3.add_student(student3)
    group3.add_student(student6)
    print(group3)

    director1 = Director(fake.unique.first_name(), fake.unique.last_name(), date(1975, 11, 14), 50000)
    director2 = Director(fake.unique.first_name(), fake.unique.last_name(), date(1988, 7, 9), 45000)

    print(director1.__dict__)
    print(director2)

    head_teacher1 = HeadTeacher(fake.unique.first_name(), fake.unique.last_name(), date(1980, 5, 23), 30000)
    head_teacher2 = HeadTeacher(fake.unique.first_name(), fake.unique.last_name(), date(1981, 6, 24), 25000)

    print(head_teacher1)
    print(head_teacher2)

    teacher1 = Teacher(fake.unique.first_name(), fake.unique.last_name(), date(1995, 9, 12), 25000, 'Math teacher')
    teacher2 = Teacher(fake.unique.first_name(), fake.unique.last_name(), date(1990, 7, 22), 25000, 'Chemistry teacher')
    teacher3 = Teacher(fake.unique.first_name(), fake.unique.last_name(), date(1991, 3, 5), 25000, 'Music Teacher')
    teacher4 = Teacher(fake.unique.first_name(), fake.unique.last_name(), date(1992, 5, 9), 1000, 'To remove teacher')

    print(teacher1, teacher2, teacher3, teacher4)

    other_staff1 = OtherStaff(fake.unique.first_name(), fake.unique.last_name(), date(1969, 10, 12), 10000, 'Supply manager')
    other_staff2 = OtherStaff(fake.unique.first_name(), fake.unique.last_name(), date(1968, 6, 6), 7000, 'Janitor1')
    other_staff3 = OtherStaff(fake.unique.first_name(), fake.unique.last_name(), date(1992, 5, 9), 1000, 'To remove other staff')

    print(other_staff1, other_staff2, other_staff3)

    school1 = School(director1, head_teacher1)
    print(school1.__dict__)

    school1.add_teacher(teacher1)
    school1.add_teacher(teacher2)
    school1.add_teacher(teacher3)
    school1.add_teacher(teacher4)
    print(school1.get_teachers())

    school1.remove_teacher(teacher4)
    print(school1.get_teachers())

    school1.add_other_staff(other_staff1)
    school1.add_other_staff(other_staff2)
    school1.add_other_staff(other_staff3)
    school1.add_other_staff(other_staff=OtherStaff(fake.unique.first_name(), fake.unique.last_name(), date(1978, 7, 7), 7000, 'Janitor2'))
    print(school1.get_other_staff())

    school1.remove_other_staff(other_staff3)
    print(school1.get_other_staff())

    print(school1.director)
    school1.director = director2
    print(school1.director)

    print(school1.head_teacher)
    school1.head_teacher = head_teacher2
    print(school1.head_teacher)

    print(school1.calculate_budget())

    print(school1.min_students_quota())

    print(school1.get_groups())
    school1.add_group(group1)
    school1.add_group(group2)
    school1.add_group(group3)
    print(school1.get_groups())
    print(len(school1.get_groups()))

    school1.remove_group(group1)
    print(len(school1.get_groups()))
    print(group2.get_students())

    print(school1.get_groups())

    print(school1.need_students())

    print(school1.get_teachers())

    print(school1.__dict__)
    print(teacher1.__dict__)


