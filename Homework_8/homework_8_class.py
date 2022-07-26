class FuelLevelError(Exception):
    def __init__(self, error):
        self.error = error

class InvalidDistanceError(Exception):
    pass

class Vehicle:
    # properties
    __tank_level: float = 0
    __odometer_value: int = 0

    # methods
    def __init__(self,
                 producer: str,
                 model: str,
                 year: int,
                 tank_capacity: float,
                 max_speed: int,
                 fuel_consumption: float,):
        """
        Initiates class object after declaration

        This method allows to describe class object of "Vehicle" class and set unique values for each one
        :param producer: vehicle's brand in type sting
        :param model: vehicle's model in type string
        :param year: vehicle's release year in type int
        :param tank_capacity: vehicle's tank capacity in type float
        :param max_speed: vehicle's max speed in type int
        :param fuel_consumption: vehicle's fuel consumption is the inverse of fuel economy in type float.
                                 It is the amount of fuel consumed in driving a given distance.
                                 It is measured in liters per 100 kilometers
        """
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption

    @property
    def tank_level(self):
        """
        This method is declared as property in order to get info of private property '''--tank_level'''

        :return: value of private property '''--tank_level'''
        """
        return self.__tank_level

    @property
    def mileage(self) -> int:
        """
        This method is declared as property in order to get info of private property '''__odometer_value'''

        :return: value of private property '''__odometer_value'''
        """
        return int(self.__odometer_value)

    def __repr__(self) -> str:
        """
        Doesn't take any arguments and generates main description about declared class object

        :return: info in type str about of declared class Vehicle that includes:
                 Vehicle's producer name, model and release year
        """
        return f'{self.producer} {self.model} released at {self.year} has ' \
               f'{self.__odometer_value} odometer value'

    def refueling(self):
        """
        Doesn't take any arguments fills the tank to full by equating the capacity of Vehicle's tank.
        Prints the note how many liters was filled depending on the amount of fuel in the tank of particular instance

        :return: None
        """
        fuel_to_full = self.tank_capacity - self.__tank_level
        self.__tank_level = fuel_to_full + self.__tank_level
        print(f'{fuel_to_full} liters were filled in {self.producer} {self.model}. Tank Capacity is full')

    def race(self, distance_to_destination: float) -> dict:
        """
        Takes one argument in type float (int) and counts traveled distance,
        fuel that left after the trip and spent time traveled

        :param distance_to_destination: number in type float or int that means the distance
                                        that instance is going to overcome
        :return: type dict that contains counted traveled distance, fuel that left after the trip
                 and spent time traveled
        """
        if distance_to_destination <= 0:
            raise InvalidDistanceError()
        else:
            fuel_per_km = (self.fuel_consumption/100)
            spent_fuel = self.tank_capacity - self.__tank_level
            distance_traveled = spent_fuel/fuel_per_km + distance_to_destination
            used_fuel = fuel_per_km * distance_to_destination
            fuel_left = self.__tank_level - used_fuel
            average_speed = self.max_speed*80/100
            travel_time = distance_to_destination/average_speed*60
            self.__burn_fuel(used_fuel)
            self.__increase_odometer_level(distance_to_destination)
            vehicle_dict = {
                'distance_traveled': distance_traveled,
                'fuel_left': fuel_left,
                'travel_time': travel_time
            }
            return vehicle_dict

    def __burn_fuel(self, fuel_needed: float):
        """
        Private function that takes one argument in type float (int) helps to define if a Vehicle
        has enough fuel for the distance mentioned in the '''race()''' method or calculate tank level
        after '''race()''' with relevant parameter value

        :param fuel_needed: argument in type float (int) that means the amount of fuel needed for the trip
        :return: None
        """
        if self.__tank_level < fuel_needed:
            insufficient_fuel = fuel_needed - self.__tank_level
            raise FuelLevelError(insufficient_fuel)
        else:
            self.__tank_level = self.__tank_level - fuel_needed

    def __increase_odometer_level(self, distance):
        """
        Private method that takes one argument and helps '''race()''' method to count the distance
        to be increased for odometer level

        :param distance: distance to be passed
        :return: None
        """
        self.__odometer_value = self.__odometer_value + distance

    def lend_fuel(self, other):
        """
        Takes other instance of the same class as a parameter and depending on the other tank level counts
        if other instance is allowed to lend fuel to self instance

        :param other: other Vehicle class object
        :return: None
        """
        fuel_to_full = self.tank_capacity - self.__tank_level
        if other.__tank_level <= fuel_to_full:
            print('No worries, I\'ll figure it out somehow')
        else:
            other.__tank_level = other.__tank_level - fuel_to_full
            self.__tank_level = self.__tank_level + fuel_to_full
            print(f'{self.producer} {self.model} says to {other.producer} {other.model}: '
                  f'"Thanks, buddy, you rescued me. You shared in {fuel_to_full} liters of fuel with me"')
            print(f'{other.producer} {other.model} says to {self.producer} {self.model}: '
                  f'"No problem, bro. You left me with {other.__tank_level} litres of fuel"')

    def __eq__(self, other) -> bool:
        """
        Helps to define equality of '''year''' and '''__odometer_value''' comparing Vehicle self and other instances

        :param other: other Vehicle class object
        :return: boolean depending on compared self and other instances '''year''' and '''__odometer_value'''
        """
        if self.year == other.year and self.__odometer_value == other.__odometer_value:
            return True
        return False



