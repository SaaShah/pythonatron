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
    def test(n):
        total = 0
        for x in range(0, n):
            for y in range(0, n):
                total += 2
    n1 = 1000
    n2 = 10000
    t1 = run(test, (n1))
    t2 = run(test, (n2))

    print 'Time 1:', t1
    print 'Time 2:', t2
    print 'Order of growth: ', empirical.order_of_growth(t1, t2, n1, n2)

