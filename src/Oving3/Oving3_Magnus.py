import random


def insertionsort(arr, left=0, right=-1):
    if right < 0:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        current = arr[i]
        j = i - 1
        while j >= left and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


def quicksort(arr, left=0, right=-1):
    if right < 0:
        right = len(arr) - 1

    if right - left <= 10:
        insertionsort(arr, left, right)
        return

    pivot = find_and_sort_median(arr, left, right)
    pivot_value = arr[pivot]

    arr[pivot], arr[right - 1] = arr[right - 1], arr[pivot]  # Move the pivot out of the way
    lower_mark = left
    higher_mark = right - 1

    while True:
        print("\n\nLower: ")
        while True:
            lower_mark += 1
            print(lower_mark, end=' ')
            if arr[lower_mark] > pivot_value or lower_mark >= higher_mark:
                break  # Found an element to be moved to the right side

        print("\nHigher: ")
        while True:
            higher_mark -= 1
            print(higher_mark, end=' ')
            if arr[higher_mark] < pivot_value or lower_mark >= higher_mark:
                break  # Found an element to be moved to the left side

        if lower_mark >= higher_mark:
            break

        arr[lower_mark], arr[higher_mark] = arr[higher_mark], arr[lower_mark]

    pivot = lower_mark
    arr[pivot], arr[right - 1] = arr[right - 1], arr[pivot]

    quicksort(arr, left, pivot - 1)
    quicksort(arr, pivot + 1, right)


def find_and_sort_median(arr, left, right):
    middle = (left + right) // 2

    if arr[left] > arr[middle]:
        arr[left], arr[middle] = arr[middle], arr[left]

    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]

    if arr[middle] > arr[right]:
        arr[middle], arr[right] = arr[right], arr[middle]

    return middle


def verify_sorted_array(arr):
    prev = arr[0]

    for i in range(1, len(arr)):
        if prev > arr[i]:
            return False
        prev = arr[i]

    return True



"""
Kode fra boka
"""

def qsort(t, v, h):
    if h - v > 2:
        delepos = splitt(t, v, h)
        qsort(t, v, delepos - 1)
        qsort(t, delepos + 1, h)
    else:
        median3sort(t, v, h)


def median3sort(t, v, h):
    m = (v + h) // 2
    if t[v] > t[m]:
        t[v], t[m] = t[m], t[v]
    if t[m] > t[h]:
        t[m], t[h] = t[h], t[m]
        if t[v] > t[m]:
            t[v], t[m] = t[m], t[v]
    return m


def splitt(t, v, h):
    m = median3sort(t, v, h)
    dv = t[m]
    iv, ih = v, h - 1

    t[m], t[h - 1] = t[h - 1], t[m]
    while True:
        while True:
            iv += 1
            if t[iv] > dv: break

        while True:
            ih -= 1
            if t[ih] < dv: break

        if iv >= ih: break

    t[iv], t[h - 1] = t[h - 1], t[iv]
    return iv


"""
array = [x for x in range(100, 0, -1)]
quicksort(array)
print(array)
print("Er tabellen sortert korrekt? {}\n".format(verify_sorted_array(array)))
"""

array = [random.randint(-50, 100) for x in range(0, 1000)]
array2 = list(array)
print("Opprinnelig array: ", end='')
print(array)

"""
qsort(array, 0, len(array) - 1)
print(array)
print("Er tabellen sortert korrekt? {}".format(verify_sorted_array(array)))
"""

quicksort(array2)
print("\n\nSortert array: ", end='')
print(array2)
print("Er tabellen sortert korrekt? {}".format(verify_sorted_array(array2)))


"""
    if l > m:
        temp = arr[0]
        l = arr[0] = m
        m = arr[len(arr) / 2] = temp

    if m > r:
        temp = arr[len(arr) / 2]
        m = arr[len(arr) / 2] = r
        r = arr[len(arr) - 1] = temp

Når sorteringen (og tidtaking) er ferdig, bruk en løkke som sjekker at tabellen er korrekt
sortert. Altså at tabell[i+1] >= tabell[i] for alle i-verdier mellom 0 og
tabell.length-2. Dermed finner dere ut om sorteringsalgoritmen deres virker som
den skal. Det er fort gjort å gjøre feil. Man kan sortere veldig raskt, hvis resultatet ikke
trenger å være riktig. :-(

Se på vanlige feil med tidtaking når vi er ferdig.
"""
