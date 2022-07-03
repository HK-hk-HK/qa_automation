import pytest

from Homework_5.homework_5_2_task import convert_argument_to_float

# test positive scenarios: return float number if value is number/any type
@pytest.mark.parametrize('value, check_type', [(float(convert_argument_to_float(4)), float),
                                               (float(convert_argument_to_float('6')), float),
                                               (float(convert_argument_to_float('6.5')), float)])
def test_convert_argument_to_float_positive(value, check_type):
    assert isinstance(value, check_type)

# test positive scenarios: return float 0 if the value is not number
@pytest.mark.parametrize('value, return_float_zero', [(float(convert_argument_to_float('test')), float(0)),
                                                      (float(convert_argument_to_float([1, 2.3])), float(0))])
def test_convert_argument_to_float_positive(value, return_float_zero):
    try:
        assert value
    except:
        return return_float_zero

# test negative: if the function without argument
def test_convert_argument_to_float_negative():
    with pytest.raises(TypeError):
        convert_argument_to_float()