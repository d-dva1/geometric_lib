import math


def area(r):
    '''
    Вычисляет площадь круга по радиусу.

    Пример:
        >> area(2);
        12.56637061
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Вычисляет периметр круга по радиусу.

    Пример:
        >> perimetr(4);
        25.13274123
    '''
    return 2 * math.pi * r

