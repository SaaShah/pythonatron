from math import log

def order_of_growth(t1, t2, N1, N2):
    return log(t2 / t1) / log(N2 / N1)

