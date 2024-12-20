class IncorrectVinNumber(Exception):
    def __init__(self, message:str):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message:str):
        self.message = message

class Car:
    def __init__(self, model:str, vin:int, numbers:str):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin)->bool:
        '''проверяет на корректность vin номер'''

        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin<1000000 or vin >= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers)->bool:
        '''проверяет на корректность номера автомобиля'''
        string_int='0123456789'
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        for i in range(1,4):
            if numbers[i] not in string_int:
                raise TypeError('В номере отсутствуют 3 целых числа')

        return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
except TypeError as exc:
    print(exc.args[0])
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'тo01тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
