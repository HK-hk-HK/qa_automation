from abc import ABC, abstractmethod


class Staff(ABC):
    @property
    @abstractmethod
    def reward(self):
        pass

    @property
    @abstractmethod
    def position(self):
        pass

    @reward.setter
    @abstractmethod
    def reward(self, new_reward):
        pass

