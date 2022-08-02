
from Homework_12.Human.Staff.staff import Staff
from Homework_12.Human.human import Human
from Homework_12.exceptions import InvalidRewardValueError


class SchoolStaff(Staff, Human):
    def __init__(self, name: str, surname: str, birth_date, reward: int, position: str):
        super().__init__(name, surname, birth_date)
        self.__reward = reward
        self.__position = position

    def __repr__(self) -> str:
        return f'{self.__position}: {self.name} {self.surname}'

    @property
    def reward(self) -> int:
        return self.__reward

    @property
    def position(self) -> str:
        return self.__position

    @reward.setter
    def reward(self, new_reward):
        if new_reward in range(1, 100000 + 1) and isinstance(new_reward, int):
            self.__reward = new_reward
        else:
            raise InvalidRewardValueError(new_reward)



