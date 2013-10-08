'''
Not entirely useful for a computer program :)
Simplifies doing large multiplications by hand
Typically, the quarter sqaure values are stored in a lookup table
a * b = ((a + b) ^ 2 / 4) - ((a - b) ^ 2 / 4)
'''

def qs(n):
    return n**2 * .25

def qs_mult(a, b):
    m = a + b
    n = a - b
    return qs(m) - qs(n) 

if __name__ == "__main__":
    a = 1024
    b = 8192
    print(a, "*", b, ":", a * b)
    print("qs_mult(", a, ", ", b, "): ", qs_mult(a, b))
