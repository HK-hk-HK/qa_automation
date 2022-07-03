import pytest

from Homework_5.homework_5_1_task import print_type

# test positive scenarios
@pytest.mark.parametrize('value, value_type', [('test', str),
                                               (5, int),
                                               (5.5, float),
                                               ([], list)])
def test_type_positive(value, value_type):
    assert type(value) is value_type


# test negative: if the function without argument
def test_type_negative():
    with pytest.raises(TypeError):
        print_type()

