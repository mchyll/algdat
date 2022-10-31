import random
import math
import time


def insertionsort(arr, left, right):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


def quicksort(arr, left=0, right=-1):
    if right == -1:
        right = len(arr) - 1

    if right - left >= 34:
        delepos = splitt(arr, left, right)
        quicksort(arr, left, delepos - 1)
        quicksort(arr, delepos + 1, right)
    else:
        insertionsort(arr, left, right)
    return arr


def splitt(arr, left, right):
    m = finn_median(arr, left, right)
    dv = arr[m]
    arr[m], arr[right-1] = arr[right-1], arr[m]  # flytter median bort for øyeblikket
    iv = left
    ih = right
    while True:
        iv += 1
        while arr[iv] < dv:
            iv += 1
        ih -= 1
        while arr[ih] > dv:
            ih -= 1
        if iv >= ih:
            break
        arr[iv], arr[ih] = arr[ih], arr[iv]
    arr[iv], arr[right-1] = arr[right-1], arr[iv]  # flytter median tilbake
    return iv


def finn_median(arr, left, right):
    midt = (right - left) // 2
    liste = [arr[left], arr[midt], arr[right]]
    liste.sort()
    arr[left], arr[midt], arr[right] = liste[0], liste[1], liste[2]
    return liste[1]



#print(quicksort(arr0))
insertion, quick = 0, 0
x = 20

while quick >= insertion:
    x += 1
    arr0 = [random.randint(0, x) for x in range(0, x)]
    print(x)
    tid0 = time.time()
    quicksort(arr0)
    quick = time.time() - tid0
    tid2 = time.time()
    insertionsort(arr0)
    insertion = time.time() - tid2
    print("quick {:f}, insertion {:f}".format(quick, insertion))
    if quick <= insertion:
        break

print(x)
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
