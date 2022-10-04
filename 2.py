#Дорога

class  Road:
    def __init__(self, length, weidth) -> None:
        self.__length = length
        self.__weidth = weidth
        print(f'{self.__length} м * {self.__weidth} м * 25 кг * 5 см = {int(self.__length * self.__weidth * 25 * 5/1000)} т')

road = Road(20, 5000)
