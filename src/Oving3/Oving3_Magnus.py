import random


def insertionsort(arr, left=0, right=-1):
    if right < 0:
        right = len(arr)

    for i in range(left + 1, right):
        current = arr[i]
        j = i - 1
        while j >= left and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


def quicksort(arr, left=0, right=-1):
    if right < 0:
        right = len(arr)

    if right - left <= 10:
        insertionsort(arr, left, right)
        return

    pivot = find_and_sort_median(arr, left, right)
    pivot_value = arr[pivot]

    lower_pair = left
    higher_pair = right
    arr[pivot], arr[right - 1] = arr[right - 1], arr[pivot]  # Move the pivot out of the way

    while True:
        while True:
            lower_pair += 1
            if arr[lower_pair] > pivot_value: break  # Found an element to be moved to the right side

        while True:
            higher_pair -= 1
            if arr[higher_pair] < pivot_value: break  # Found an element to be moved to the left side

        if lower_pair >= higher_pair:
            break

        arr[lower_pair], arr[higher_pair] = arr[higher_pair], arr[lower_pair]

    pivot = lower_pair
    arr[pivot], arr[right - 1] = arr[right - 1], arr[pivot]

    quicksort(arr, left, pivot - 1)
    quicksort(arr, pivot + 1, right)


def find_and_sort_median(arr, left, right):
    middle = (left + right) // 2
    right -= 1

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


array = [x for x in range(100, 0, -1)]
#quicksort(array)
print(array)
print("Er tabellen sortert korrekt? {}\n".format(verify_sorted_array(array)))

array = [random.randint(-10, 100) for x in range(0, 100)]
quicksort(array)
print(array)
print("Er tabellen sortert korrekt? {}".format(verify_sorted_array(array)))


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
