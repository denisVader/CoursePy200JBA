from typing import Union
import doctest

class Airplane:
    """"
     Класс описывает модель самолета
    """
    def __init__(self, seat: int, passenger: int):
        """
        Инициализация экземпляра класс
        :param seat: сколько мест в самолете
        :param passenger: поссажиры
        Примеры:
        #>>> airplane = Airplane(500, 0)  # инициализация экземпляра класса
        """
        self.seat = None
        self.init_seat(seat)
        self.passenger = None
        self.init_passenger(passenger)
        self.free_seat = 0
    def init_seat(self,seat:int):
        if not isinstance(seat, int):
            raise TypeError('Должен быть классом  int')
        if seat < 0:
            raise ValueError('Не может быть отрицательным')
        self.seat = seat


    def init_passenger(self, passenger: int):
        if not isinstance(passenger, int):
            raise TypeError('Должен быть классом  int')
        if passenger < 0:
            raise ValueError('Не может быть отрицательным')
        self.passenger = passenger

    def increment_passenger(self, passenger: int):
        """
        Метод увеличивает занятое место
        :param occupied_seat: Количество занятых мест
        """
        if not isinstance(passenger, int):
            raise TypeError('Должен быть классом  int')
        if passenger < 0:
            raise ValueError('Не может быть отрицательным')
        self.free_seat += passenger




if __name__ == "__main__":
    airplane = Airplane(550, 400)    #  работоспособность экземпляров класса проверить с помощью doctest
    airplane.increment_passenger(2)
    print(airplane.seat)
    print(airplane.passenger)
    print(airplane.free_seat)


class PhoneBook:
    """
    Класс описывает модель записной книжки
    """
    def __init__(self, name: str, phone: int):
        self.name = None
        self.init_name(name)
        self.phone = None
        self.init_phone(phone)


    def init_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Должен быть строковым')
        self.name = name

    def init_phone(self, phone: int):
        if not isinstance(phone, int):
            raise TypeError('Должен быть int')
        self.phone = phone

    def append(self, name, phone):
        #with open('file.txt', 'a') as file_object:
        #file_object.write(name,phone)
            pass


if __name__ == "__main__":
    pass

class Cube:
    """
    Класс описывает куб
    """
    def __init__(self, length: Union[float, int], width: Union[float, int], height: Union[float, int]):
        """Создаем атрибуты"""
        self.length = None
        self.init_length(length)
        self.width = None
        self.init_width(width)
        self.height = None
        self.init_height(height)

    def init_length(self, length: Union[float, int]):
        if not isinstance(length, (float, int)):
            raise TypeError('Должен быть тип int')
        if length < 0:
            raise ValueError('Не может быть отрицательным')
        self.length = length

    def init_width(self, width: Union[float, int]):
        if not isinstance(width, (float,int)):
            raise TypeError('Должен быть тип int')
        if width < 0:
            raise ValueError('Не может быть отрицательным')
        self.width = width

    def init_height(self, height: Union[float, int]):
        if not isinstance(height, (float, int)):
            raise TypeError('Должен быть тип int')
        if height < 0:
            raise ValueError('Не может быть отрицательным')
        self.height = height

    def calculate_volume(self, length, width, height):
        """
        Метод вычисляет объем, исходя из трех велечин
        """
        volume = length * width * height
        return volume

if __name__ == "__main__":
    cube = Cube(1, 2, 3)
    print(cube.height)
    print(cube.length)
    print(cube.width)
    print(cube.calculate_volume(1.2, 2, 3))
    #help(cube)
    doctest.testmod()

