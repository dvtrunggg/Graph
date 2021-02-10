from math 
import sqrt

class Point2D:
    def __init__(self, a, b):
        self.x = a
        self.y = b

def distance(a, b):
    return sqrt((a.x-b.x)**2+(a.y-b.y)**2)

def triangleCheck(a, b, c):
    if ((a.x == b.x and b.x == c.x) or (a.y == b.y and b.y == c.y)):
        return -1;
    else:
        return 1;

def triangleClass(a, b, c):
    da = sqrt(pow(distance(a, b), 2) + pow(distance(a, c), 2))
    db = sqrt(pow(distance(b, a), 2) + pow(distance(b, c), 2))
    dc = sqrt(pow(distance(c, a), 2) + pow(distance(c, b), 2))

    if distance(a, b) == distance(a, c):
        print('this is isosceles triangle')  # tam giac can

    if (distance(a, b) == distance(a, c)) and (distance(a, c) == distance(b, c)):
        print('this is equilateral triangle')   #tam guac deu

    if (da == distance(b, c)) or (db == distance(a, c)) or (dc == distance(a, b)):
        print('this is right triangle')     #tam giac vuong

def Perimeter(a, b, c):
    return distance(a, b) + distance(b, c) + distance(c, a)

def Area(a, b, c):
    return 0.5 * ((b.x - a.x)*(c.y - a.y) - (c.x - a.x) * (b.y - a.y))

def Position(a, b, c, d):
    ab = Point2D(b.x - a.x, b.y - a.y)
    cd = Point2D(d.x - c.x, d.y - c.y)
    if (ab.x * cd.x) + (ab.y * cd.y) == 0:
        print('2 đường thằng vuông góc')
    if (ab.x / cd.x) == (ab.y / cd.y):
        print('2 đường thẳng song song')

p1 = Point2D(2, 3)
p2 = Point2D(0, 2)
p3 = Point2D(4, -1)
p4 = Point2D(2, 9)

