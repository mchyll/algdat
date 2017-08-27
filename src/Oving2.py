import time


def power1(x, n):
    if n <= 0:
        return 1
    return x * power1(x, n - 1)


def power2(x, n):
    if n <= 0:
        return 1

    if n % 2 != 0:  # Hvis n er odde
        return x * power2(x * x, (n - 1) / 2)

    # Hvis n er partall
    return power2(x * x, n / 2)


for i in range(50):
    start = time.time()
    result = power1(1.0000001, 900)
    stop = time.time()
    print("Svar: {}, tStart={}, tStop={}, tid={} µs".format(result, start, stop, (stop - start) * 1000000))
