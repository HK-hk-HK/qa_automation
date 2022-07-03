"""
Напишіть функцію, що приймає два аргументи.
Функція повинна:
- якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
- якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
- якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
- у будь-якому іншому випадку повернути кортеж з цих аргументів
"""

def print_result_depending_on_args(arg_one, arg_two):
    try:
        if type(arg_one) is str and type(arg_two) is str:
            return f'{arg_one} {arg_two}'
        elif type(arg_one) is str:
            return {arg_one: arg_two}
        elif type(arg_one) is int or float and type(arg_two) is int or float:
            return arg_one - arg_two
    except TypeError:
        return arg_one, arg_two


function_test = print_result_depending_on_args('unioned', 'args')
print(type(function_test))
print('Arguments result: ', function_test)

function_test = print_result_depending_on_args('unioned', 5.7)
print(type(function_test))
print('Arguments result: ', function_test)

function_test = print_result_depending_on_args(5, 1.3)
print(type(function_test))
print('Arguments result: ', function_test)

function_test = print_result_depending_on_args(5, 'args')
print(type(function_test))
print('Arguments result: ', function_test)

function_test = print_result_depending_on_args(2, 6)
print(type(function_test))
print('Arguments result: ', function_test)
