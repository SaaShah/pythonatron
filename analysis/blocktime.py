import os

def etime():
    user, sys, chuser, chsys, real = os.times()
    print user, sys, chuser, chsys, real
    return user + sys

def run(entry):
    start = etime()
    entry()
    end = etime()
    return end - start


def init():
    total = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            total += 2
            total /= .01

time = run(init)
print time
