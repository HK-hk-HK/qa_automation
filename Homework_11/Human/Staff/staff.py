from Homework_11.Human.human import Human


class InvalidRewardValueError(Exception):
    def __init__(self, error):
        self.error = error

class Staff(Human):
    def __init__(self, name: str, surname: str, position: str, birth_date, reward: int):
        super().__init__(name, surname, position, birth_date)
        self.__reward = reward

    def __repr__(self) -> str:
        return f'{self.position}: {self.name} {self.surname}'

    @property
    def reward(self) -> int:
        return self.__reward

    @reward.setter
    def reward(self, new_reward):
        if new_reward > 0 and isinstance(new_reward, int):
            self.__reward = new_reward
        else:
            raise InvalidRewardValueError(new_reward)



