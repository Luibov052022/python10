import time
# Светофор

class TrafficLight:
    
    def running(self):
        self.__color = 1
        while self.__color < 4:
            if self.__color == 1:
                print('Красный режим')
                time.sleep(7)
            elif self.__color == 2:
                print('Желтый режим')
                time.sleep(2)
            elif self.__color == 3:
                print('Зеленый режим')
                time.sleep(10) 
            self.__color += 1           

light = TrafficLight()
light.running()
light.running()
light.running()