from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume < 0:
            raise ValueError('Не может быть отрицательным')
        if occupied_volume > capacity_volume:
            raise ValueError('Объем стакана меньше ')
        self.capacity_volume = capacity_volume     #Атрибут # инициализировать объект "Стакан"
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError('Не может быть отрицательным')
        self.occupied_valume = occupied_volume

        print(isinstance(capacity_volume, (int, float)))
        print(isinstance(occupied_volume, (int, float)))



if __name__ == "__main__":
    glass1 = Glass(200, 150)    #Экземпдяр класса

    glass2 = Glass(200, 50)    #Второй экземпляр класс



    # incorrect_capacity_volume_type = ...
    # incorrect_occupied_volume_value = ...     # попробовать инициализировать не корректные объекты
