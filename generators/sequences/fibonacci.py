'''
Fn = Fn-1 + Fn-2
F0 = 0
F1 = 1
'''
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        if i == 0: yield 0
        if i == 1: yield 1
        else:
            x, y = y, x + y
            yield y

'''
Fn = Fn-1 + Fn-2 + Fn-3
F0 = 1
F1 = 1
F2 = 1
'''
def tribonacci(n):
    x, y, z = 1, 1, 1 
    for i in range(n):
        if i is 0 or i is 1 or i is 2 : yield 1
        else:
            x, y, z = y, z, x + y + z
            yield z

if __name__ == '__main__':
    for n in fibonacci(10):
        print(n)

    for n in tribonacci(10):
        print(n)



