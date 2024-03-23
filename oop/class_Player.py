from datetime import datetime as dt


class Player:

    __LEVEL, __HEALTH = 1, 100
    __slots__ = ['__level', '__health', '__born']  # allowed properties

    def __init__(self):
        self.__level = Player.__LEVEL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property
    def level(self):  # getter
        return self.__level, f'{dt.now() - self.__born}'

    @level.setter
    def level(self, number_of_level):  # setter
        self.__level += Player.__typeTest(number_of_level)
        if self.__level >= 100:
            self.__level = 100

    @classmethod
    def set_cls_field(cls, number_of_level=1, health=100):
        cls.__LEVEL = Player.__typeTest(number_of_level)
        cls.__HEALTH = Player.__typeTest(health)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):  # checks if the type of 'value' is equal to type of par2
            return value
        else:
            raise TypeError("Must be integer")
