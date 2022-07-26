import pytest
from Homework_8.homework_8_class import Vehicle

@pytest.fixture
def vehicle_c():
    return Vehicle('Chevrolet Chevelle', 'SS 454', 1970, 76, 210, 20.3)

@pytest.fixture
def vehicle_b():
    return Vehicle('Plymouth Barracuda', '426 Hemi Cuda', 1970, 72, 204, 39.27)

@pytest.mark.parametrize('expected_result',
                         ['76 liters were filled in Chevrolet Chevelle SS 454. Tank Capacity is full'])
def test_refueling(capsys, vehicle_c, expected_result):
    vehicle_c.refueling()
    captured = capsys.readouterr()
    assert expected_result in captured.out

@pytest.mark.parametrize('expected_result',
                         ['72 liters were filled in Plymouth Barracuda 426 Hemi Cuda. Tank Capacity is full'])
def test_refueling(capsys, vehicle_b, expected_result):
    vehicle_b.refueling()
    captured = capsys.readouterr()
    assert expected_result in captured.out

@pytest.mark.parametrize('distance_to_destination, expected_result',
                         [(129, {'distance_traveled': 129.0,
                                 'fuel_left': 49.813,
                                 'travel_time': 46.07142857142858})])
def test_race(vehicle_c, distance_to_destination, expected_result):
    vehicle_c.refueling()
    assert vehicle_c.race(distance_to_destination) == expected_result

@pytest.mark.parametrize('distance_to_destination, expected_result',
                         [(123, {'distance_traveled': 123.0,
                                 'fuel_left': 23.697899999999997,
                                 'travel_time': 45.22058823529412})])
def test_race(vehicle_b, distance_to_destination, expected_result):
    vehicle_b.refueling()
    assert vehicle_b.race(distance_to_destination) == expected_result




