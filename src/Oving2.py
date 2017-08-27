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


print("Bruker power1")
sumTime = 0
num = 0
for i in range(20):
    start = time.time()
    result = power1(1.0000001, 900)
    stop = time.time()
    elapsed = (stop - start) * 1000000
    if elapsed > 0:
        sumTime += elapsed
        num += 1
    print("  Svar: {}, tid={} µs".format(result, elapsed))

if num > 0:
    print("Gjennomsnitt tidsbruk: {} µs\n".format(sumTime / num))


print("Bruker power2")
sumTime = 0
num = 0
for i in range(20):
    start = time.time()
    result = power2(1.0000001, 900)
    stop = time.time()
    elapsed = (stop - start) * 1000000
    if elapsed > 0:
        sumTime += elapsed
        num += 1
    print("  Svar: {}, tid={} µs".format(result, elapsed))

if num > 0:
    print("Gjennomsnitt tidsbruk: {} µs".format(sumTime / num))


print("Bruker innebygd power")
sumTime = 0
num = 0
for i in range(20):
    start = time.time()
    result = 1.0000001 ** 900
    stop = time.time()
    elapsed = (stop - start) * 1000000
    if elapsed > 0:
        sumTime += elapsed
        num += 1
    print("  Svar: {}, tid={} µs".format(result, elapsed))

if num > 0:
    print("Gjennomsnitt tidsbruk: {} µs".format(sumTime / num))
