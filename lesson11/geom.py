from math import pi

p1 = ('p', 0, 0)

def printpoint(p):
    print('point:%s,%s'%(p[1],p[2]))

def pointarea(p):return 0

printpoint(p1)
print(pointarea(p1))

sq1 = ('s', 2)

def printsq(sq):
    print('sqrt:%s'%sq[1])

def sqarea(sq):
    return sq[1]**2

printsq(sq1)
print(sqarea(sq1))

cir1 = ('c', 1)

def printsq(cir):
    print('circle:%s'%cir[1])

def cirarea(cir):
    return cir[1]**2*pi

printsq(cir1)
print(cirarea(cir1))

def geomarea(geom):
    if geom[0] == 'p':return pointarea(geom)
    if geom[0] == 's':return sqarea(geom)
    if geom[0] == 'c':return cirarea(geom)
    
lst = [p1, sq1, cir1]
s = sum([geomarea(i) for i in lst])
print(s)
