import pytest

from Homework_5.homework_5_3_task import print_result_depending_on_args

@pytest.mark.parametrize('first_value, second_value, expected_result', [('test', 'test', 'test test'),
                                                                        (5, 2, 3),
                                                                        ('test', 5.7, {'test': 5.7}),
                                                                        (5, 'test', (5, 'test')),
                                                                        (5.3, 1.3, 4.0)])
def test_print_result_depending_on_args_positive(first_value, second_value, expected_result):
    assert print_result_depending_on_args(first_value, second_value) == expected_result



