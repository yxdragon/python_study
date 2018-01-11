from math import pi

class Geom():
    def __init__(self):pass
    def printself(self):print('this is a geom')
    def area(self):return -1;

class Point(Geom):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def printself(self):
        print('point:%s,%s'%(self.x, self.y))

    def area(self):return 0;

class Circle(Geom):
    def __init__(self, r):
        self.r = r

    def printself(self):
        print('circle:%s'%self.r)

    def area(self):
        return self.r**2*pi

geom = Geom()
geom.printself()
print(geom.area())

p = Point(0, 0)
p.printself()
print(p.area())

c = Circle(1)
c.printself()
print(c.area())

lst = [Point(0,0), Circle(1), Circle(2)]
print(sum([i.area() for i in lst]))
