def insertionsort(arr, left=0, right=-1):
    """
    Sorterer en del av eller en hel array med insertion sort.
    :param arr:
    :param left: venstre grense for delen av arr som skal sorteres, inklusivt
    :param right: høyre grense for delen av arr som skal sorteres, inklusivt
    :return:
    """
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
    """
    Sorterer en del av eller en hel array med quicksort.
    :param arr:
    :param left: venstre grense for delen av arr som skal sorteres, inklusivt
    :param right: høyre grense for delen av arr som skal sorteres, inklusivt
    :return:
    """
    if right < 0:
        right = len(arr) - 1

    if right - left <= 200:  # Sorter en delarray med insertionsort hvis den er liten nok
        insertionsort(arr, left, right)
        return

    # Finn delingselementet
    pivot = find_and_sort_median(arr, left, right)
    pivot_value = arr[pivot]

    # Flytt delingselementet helt til høyre, ut av veien
    arr[pivot], arr[right - 1] = arr[right - 1], arr[pivot]

    lower_mark = left
    higher_mark = right - 1

    while True:
        while True:
            lower_mark += 1
            # Let etter elementer som har høyere verdi enn delingsverdien
            if arr[lower_mark] > pivot_value or lower_mark >= higher_mark:
                break  # Fant et element som må flyttes til høyre side

        while True:
            higher_mark -= 1
            # Let etter elementer som har lavere verdi enn delingsverdien
            if arr[higher_mark] < pivot_value or lower_mark >= higher_mark:
                break  # Fant et element som må flyttes til venstre side

        # Når venstre og høyre peker krysser hverandre står alle elementer på riktig side i forhold til delingsverdien
        if lower_mark >= higher_mark:
            break

        arr[lower_mark], arr[higher_mark] = arr[higher_mark], arr[lower_mark]

    pivot = lower_mark  # Posisjonen til delingselementet skal være der venstre og høyre peker krysset hverandre
    arr[pivot], arr[right - 1] = arr[right - 1], arr[pivot]  # Flytt delingselementet tilbake til riktig plass

    # Sorter venstre og høyre deltabell rekursivt hver for seg
    quicksort(arr, left, pivot - 1)
    quicksort(arr, pivot + 1, right)


def find_and_sort_median(arr, left, right):
    """
    Finner medianen av første, mellomste og siste element, sorterer de i forhold til hverandre,
    og returnerer index til medianen.
    :param arr:
    :param left:
    :param right:
    :return:
    """
    middle = (left + right) // 2

    if arr[left] > arr[middle]:
        arr[left], arr[middle] = arr[middle], arr[left]

    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]

    if arr[middle] > arr[right]:
        arr[middle], arr[right] = arr[right], arr[middle]

    return middle
