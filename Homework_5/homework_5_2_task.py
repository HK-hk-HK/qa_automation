"""
Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float.
Якщо перетворити не вдається функція має повернути 0 (флоатовий нуль).
"""


def convert_argument_to_float(my_arg):
    try:
        return float(my_arg)
    except:
        return float(0)


converted_value = convert_argument_to_float(4)
print(converted_value)

converted_value = convert_argument_to_float('6')
print(converted_value)

converted_value = convert_argument_to_float('5.5')
print(converted_value)

converted_value = convert_argument_to_float('test')
print(converted_value)
