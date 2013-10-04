def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        if i == 0: yield 0
        if i == 1: yield 1
        else:
            x, y = y, x + y
            yield y

def tribonacci(n):
    x, y, z = 1, 1, 1 
    for i in range(n):
        if i is 0 or i is 1 or i is 2 : yield 1
        else:
            x, y, z = y, z, x + y + z
            yield z

if __name__ == '__main__':
    for x in fibonacci(20):
        print(x)

    for x in tribonacci(20):
        print(x)



