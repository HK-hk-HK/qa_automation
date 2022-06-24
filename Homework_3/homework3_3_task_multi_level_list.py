"""
Існує ліст з різними даними, наприклад
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть механізм, який сформує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1.
Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
"""
# Third task with multi-level list

import numpy as np

list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0,
         'Lorem Ipsum', 5.6, '6.8', -100, [42, '51', 4.4, '7.5', 'hello', True, [15, '12'], 'False'], 10]

def extract_digits(from_list):
    result_list = np.array([])
    for elem in from_list:
        if isinstance(elem, list):
            nested_list = extract_digits(elem)
            result_list = np.append(result_list, nested_list)
        try:
            if isinstance(elem, bool):
                continue
            float(elem)
            result_list = np.append(result_list, elem)
        except TypeError:
            continue
        except ValueError:
            continue
    return result_list

print(extract_digits(list1))