#
# Pylint tutorial
#

class car:
    def __init__(self,color):
        self.color = color

my_car = car('blue')

def crash (car1, car2):
    car.color = 'burnt'


crash(car('red'),my_car)