from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError('Числа должны быть класса int')
        if not capacity_volume > 0:
            raise ValueError('Не может быть отрицательным')
        self.capacity_volume = capacity_volume


    def init_occupied_volume(self, occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError('Числа должны быть класса int')
        if occupied_volume < 0:
            raise ValueError('Не может быть отрицательным')
        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass = Glass(200, 100)  #  инициализировать экземпляр класса Glass
    print(glass.capacity_volume)  #  распечатать атрибут capacity_volume
    print(glass.occupied_volume)  #  распечатать атрибут occupied_volume
