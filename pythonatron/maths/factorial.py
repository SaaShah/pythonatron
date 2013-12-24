def factorial(n):
    x = 1
    for i in range(1, abs(n)+1):
        x *= i
    return x if n > 0 else -x

if __name__ == "__main__":
    for i in range(-10, 10):
        print(i, factorial(i))
