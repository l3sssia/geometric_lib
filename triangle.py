def checkValues(a, b, c):
    if (a < 0):
        raise ValueError("Given negative value for triangle side a: ", a)
    if (b < 0):
        raise ValueError("Given negative value for triangle side b: ", b)
    if (c < 0):
        raise ValueError("Given negative value for triangle side b: ", c)

def checkValues(a, h):
    if (a < 0):
        raise ValueError("Given negative value for triangle side a: ", a)
    if (h < 0):
        raise ValueError("Given negative value for triangle height: ", h)

def area(a, h):
    '''
    Возвращает площадь треугольника в зависимости от длины его стороны и высоты, опущенной к ней

        Параметры:
            a (int/float): длина стороны треугольника
            h (int/float): длина высоты, опущенная к стороне a

        Возвращаемое значение:
            area (int/float): площадь треугольника со стороной a и высотой h
    '''
    checkValues(a, h)
    return a * h / 2


def perimeter(a, b, c):
    '''
    Возвращает площадь треугольника в зависимости от длин его сторон

        Параметры:
            a (int/float): длина первой стороны треугольника
            b (int/float): длина второй стороны треугольника
            c (int/float): длина третьей стороны треугольника

        Возвращаемое значение:
            perimeter (int/float): периметр треугольника с сторонами a, b, c
    '''
    checkValues(a, b, c)
    return a + b + c
