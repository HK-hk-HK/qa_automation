"""
Вести з консолі строку зі слів (або скористайтеся константою).
Напишіть код, який визначить кількість слів, в цих даних.
"""
import re

text = 'Now is the clouds that am rudely stamp\'d , and some hath smooth\'d his summer by this wrinkled for monuments ;'
symbols = '[,.:;*/&$#@!?\']'

text = re.sub(symbols, '', text)
print('Кількість слів в константi дорiвнює: ', len(text.split()))
print(text)