def harmonic():
    n = 1.0
    x = 0.0
    while True:
        x += 1.0/n
        yield x 
        n += 1.0

if __name__ == '__main__':
    i = 0
    for n in harmonic():
        if i >= 10:
            break
        else:
            print(i, n)
            i += 1
