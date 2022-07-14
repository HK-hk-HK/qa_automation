import pytest

from Homework_6.homework_6 import transform_age_ending, check_user_age

"""
NOTE: Within this homework functions, variables and prints are coded in the same file. 
In order to this test wasn't failed, all extra strings should be commented in the file with functions 
(particularly strings 52, 53 and 89 in the 'homework_6' file. Only functions code should be active!)
"""

# test positive scenarios, helper func: word ending depending on number
@pytest.mark.parametrize('age_number_string, expected_result', [('1', '1 рік'),
                                                                ('2', '2 роки'),
                                                                ('5', '5 років'),
                                                                ('11', '11 років'),
                                                                ('33', '33 роки'),
                                                                ('51', '51 рік'),
                                                                ('70', '70 років'),
                                                                ('98', '98 років'),])
def test_transform_age_ending_positive(age_number_string, expected_result):
    assert transform_age_ending(age_number_string) == expected_result

# test negative scenarios, helper func: input less than 1, more than 100
@pytest.mark.parametrize('age_wrong_number, expected_result', [('0', 'Вік користувача мае бути більше нуля'),
                                                               ('-10', 'Вік користувача мае бути більше нуля'),
                                                               ('100', 'Вік користувача мае бути меньше 100'),
                                                               ('20000', 'Вік користувача мае бути меньше 100')])
def test_transform_age_ending_negative_wrong_number(age_wrong_number, expected_result):
    assert transform_age_ending(age_wrong_number) == expected_result

# test negative scenarios, helper func: input text instead of number
@pytest.mark.parametrize('age_wrong_value, expected_result', [('test', 'Введіть ціле число будь ласка (від 1 до 99)'),
                                                              ('-10 test', 'Введіть ціле число будь ласка (від 1 до 99)'),
                                                              ('22 test', 'Введіть ціле число будь ласка (від 1 до 99)'),
                                                              (' ', 'Введіть ціле число будь ласка (від 1 до 99)')])
def test_transform_age_ending_negative_wrong_value(age_wrong_value, expected_result):
    assert transform_age_ending(age_wrong_value) == expected_result

# test positive scenarios, main func: word ending depending on number
@pytest.mark.parametrize('age_number_string, expected_result', [('1', 'Тобі ж 1 рік! Де твої батьки?'),
                                                                ('4', 'Тобі ж 4 роки! Де твої батьки?'),
                                                                ('5', 'Тобі ж 5 років! Де твої батьки?'),
                                                                ('7', 'Тобі лише 7 років, а це фільм для дорослих!'),
                                                                ('11', 'О! Вам 11 років! Який цікавий вік!'),
                                                                ('22', 'О! Вам 22 роки! Який цікавий вік!'),
                                                                ('65', 'Незважаючи на те, що вам 65 років, білетів всеодно нема!'),
                                                                ('66', 'О! Вам 66 років! Який цікавий вік!'),
                                                                ('73', 'Вам 73 роки? Покажіть пенсійне посвідчення'),])
def test_check_user_age_positive(age_number_string, expected_result):
    assert check_user_age(age_number_string) == expected_result

# test negative scenarios, main func: input less than 1, more than 100
@pytest.mark.parametrize('age_wrong_number, expected_result', [('0', 'Вік користувача мае бути більше нуля'),
                                                               ('-10', 'Вік користувача мае бути більше нуля'),
                                                               ('100', 'Вік користувача мае бути меньше 100'),
                                                               ('20000', 'Вік користувача мае бути меньше 100')])
def test_check_user_ageg_negative_wrong_number(age_wrong_number, expected_result):
    assert check_user_age(age_wrong_number) == expected_result

# test negative scenarios, main func: input text instead of number
@pytest.mark.parametrize('age_wrong_value, expected_result', [('test', 'Введіть ціле число будь ласка (від 1 до 99)'),
                                                              ('-10 test', 'Введіть ціле число будь ласка (від 1 до 99)'),
                                                              ('22 test', 'Введіть ціле число будь ласка (від 1 до 99)'),
                                                              (' ', 'Введіть ціле число будь ласка (від 1 до 99)')])
def test_check_user_age_negative_wrong_value(age_wrong_value, expected_result):
    assert check_user_age(age_wrong_value) == expected_result

