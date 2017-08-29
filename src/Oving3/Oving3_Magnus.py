def insertionsort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


def quicksort(arr, left = 0, right = -1):
    if right == -1:
        right = len(arr)

    if len(arr) <= 10:
        insertionsort(arr)
        return

    l = arr[0]
    m = arr[len(arr) / 2]
    r = arr[len(arr) - 1]
    pivot = m

    if pivot > l and pivot > r:
        pivot = max(l, r)


arr = [5,4,3,2,1]
insertionsort(arr)
print(arr)

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
