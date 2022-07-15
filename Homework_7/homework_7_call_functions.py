from homework_7_functions import transform_age_ending
from homework_7_functions import check_user_age

"""
Візьміть свою HW 6 ("Касир в кінотеатрі"), винесіть всі допоміжні функціі в окремий файл. 
В основному файлі виконайте імпорт цих функцій.
"""

# Variable that created to be passed as an argument for 'transform_age_ending()' and 'check_user_age()' functions
user_age = input('Введіть вік користувача: ')

# Prints ukrainian word 'рік' in relevant form
print(transform_age_ending(user_age))

# Prints the relevant cashier respond that depends on the inputted user age
print(check_user_age(user_age))