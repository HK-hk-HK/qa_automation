"""
Напишіть функцію, що приймає один аргумант.
Функція має вивести на екран тип цього аргумента (для визначення типу використайте type)
"""

def print_type(type_argument):
    return type(type_argument)

some_integer = print_type(type_argument=876)
some_string = print_type(type_argument='test')
some_float = print_type(type_argument=5.7)
some_list = print_type(type_argument=[])

print(f'Type of some_integer is: {some_integer}')
print(f'Type of some_string is: {some_string}')
print(f'Type of some_float is: {some_float}')
print(f'Type of some_list is: {some_list}')


