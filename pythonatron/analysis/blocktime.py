import os
import empirical

def time():
    user, sys, chuser, chsys, real = os.times()
    return user + sys

def run(entry, *args):
    start = time()
    entry(*args)
    end = time()
    return end - start

if __name__ == '__main__':

    def linear(n):
        total = 0
        for x in range(0, n):
            total += x

    def quadratic(n):
        total = 0
        for x in range(0, n):
            for y in range(0, n):
                total += x 
    n1 = 100000
    n2 = 1000000
    
    t1 = run(linear, n1)
    t2 = run(linear, n2)
    
    print 'Linear'
    print 'Time 1:', t1
    print 'Time 2:', t2
    print 'Order of growth:', empirical.order_of_growth(t1, t2, n1, n2)
    
    n1 = 1000
    n2 = 10000

    t1 = run(quadratic, n1)
    t2 = run(quadratic, n2)

    print '\nQuadratic'
    print 'Time 1:', t1
    print 'Time 2:', t2
    print 'Order of growth: ', empirical.order_of_growth(t1, t2, n1, n2)

