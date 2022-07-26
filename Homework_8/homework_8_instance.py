from homework_8_class import Vehicle
from homework_8_class import FuelLevelError
from homework_8_class import InvalidDistanceError

try:

    # audi q8 instance of 'Vehicle' class creation
    audi_q8 = Vehicle('Audi', 'Q8', 2019, 85, 250, 9.2)
    # mercedes instance of 'Vehicle' class creation
    mercedes_gle_450 = Vehicle('Mercedes', 'Gle 450', 2019, 85, 250, 12.6)

    # audi q8 info dict
    print(audi_q8.__dict__)
    # mercedes gle 450 info dict
    print(mercedes_gle_450.__dict__)

    # audi q8 is filled up to a full tank
    audi_q8.refueling()
    # mercedes gle 450 is filled up to a full tank
    mercedes_gle_450.refueling()

    # audi q8 odometer level before the first ride
    print(f'{audi_q8.producer} {audi_q8.model} odometer level before the first ride: ', audi_q8.mileage)
    # mercedes gle 450 odometer level first before ride
    print(f'{mercedes_gle_450.producer} {mercedes_gle_450.model} odometer level before the first ride: ',
          mercedes_gle_450.mileage)
    # comparing audi q8 and mercedes gle 450 release and odometer level
    print(f'{audi_q8.producer} {audi_q8.model} and {mercedes_gle_450.producer} {mercedes_gle_450.model} '
          f'have the same release year and the same odometer level: ', audi_q8.__eq__(mercedes_gle_450))

    # audi q8 first ride
    print(f'{audi_q8.producer} {audi_q8.model} first ride.', audi_q8.race(400))
    # audi q8 odometer level after the first ride
    print(f'{audi_q8.producer} {audi_q8.model} odometer level after the first ride: ', audi_q8.mileage)
    # audi q8 tank level after the first ride
    print(f'{audi_q8.producer} {audi_q8.model} tank level after the first ride: ', audi_q8.tank_level)

    # mercedes gle 450 first ride
    print(f'{mercedes_gle_450.producer} {mercedes_gle_450.model} first ride.', mercedes_gle_450.race(123))
    # mercedes gle 450 odometer level after the first ride
    print(f'{mercedes_gle_450.producer} {mercedes_gle_450.model} '
          f'odometer level after the first ride: ', mercedes_gle_450.mileage)
    # mercedes gle 450 tank level after the first ride
    print(f'{mercedes_gle_450.producer} {mercedes_gle_450.model} '
          f'tank level after the first ride: ', mercedes_gle_450.tank_level)

    # audi q8 met mercedes gle 450 and asked to lend fuel
    audi_q8.lend_fuel(mercedes_gle_450)
    # audi q8 tank level after mercedes gle 450 lent fuel to
    print(f'{audi_q8.producer} {audi_q8.model} tank level after {mercedes_gle_450.producer} {mercedes_gle_450.model} '
          f'lent fuel to: ', audi_q8.tank_level)
    print(f'{mercedes_gle_450.producer} {mercedes_gle_450.model} tank level after he '
          f'lent fuel to {audi_q8.producer} {audi_q8.model}: ', mercedes_gle_450.tank_level)

    # comparing audi q8 and mercedes gle 450 release and odometer level after the first ride
    print(f'{audi_q8.producer} {audi_q8.model} and {mercedes_gle_450.producer} {mercedes_gle_450.model} '
          f'have the same release year and the same odometer level: ', audi_q8.__eq__(mercedes_gle_450))

except FuelLevelError as error:
    print(f'Insufficient fuel level. Need more: {error} litres')
except InvalidDistanceError:
    print('Distance value can\'t be negative or equal to 0')
except TypeError:
    print(f'Input should be number, not string')


