'''
Utility for rotating point around shortest path along a radius
Provides a method for simply offsetting the start value, as well
as an iterator for obtaining the point over a given number of steps
'''

from math import pi
def offset(a, b):
    while b - a > pi:
        a += pi * 2
    while b - a < -pi:
        a -= pi * 2
    return a

def short_rotation(a, b, steps):
    a = offset(a, b)
    n = 0
    d = b - a
    inc = 1 / steps
    while n <= 1.0:
        yield a + d * n
        n += inc 

if __name__ == '__main__':
    a = 2 * pi - pi / 4
    b = pi / 4
    for r in short_rotation(a, b, 10.0):
        print r
