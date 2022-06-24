"""
Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
Слово та номер отримайте за допомогою input() або скористайтеся константою.
Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".
"""
# 1 task with two inputs

word1 = input('Input some word: ')
num = int(input(f'Input number from 1 to {len(word1)} : '))

if word1 == '':
    print('"Word field" can\'be empty')
else:
    if num <= 0:
        print('The number should be more than zero')
    else:
        try:
            print(f'The {num} symbol in "{word1}" is "{word1[num - 1]}"')
        except IndexError:
            print(f'Index Error: Max number for "Input number" filed is {len(word1)}')
        except ValueError:
            print('Value Error: Integer more than zero should be inputted in the "Number Field"')

