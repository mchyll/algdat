import copy

arr = [5, 4, 3, 2, 1, 0]


def median3sort(arr, left, right):

    m = (left + right) // 2
    if arr[left] > arr[m]:
        arr[left], arr[m] = arr[m], arr[left]
    if arr[m] > arr[right]:
        arr[right], arr[m] = arr[m], arr[right]
        if arr[left] > arr[m]:
            arr[left], arr[m] = arr[m], arr[left]
    """for i in range(1, len(arr)):
    current = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > current:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = current
    """


def findMedian(arr, left, right):
    medianArr = [arr[left], arr[(left + right) // 2], arr[right]]
    median3sort(medianArr, left, right)
    arr[left], arr[(left + right) // 2], arr[right] = medianArr[0], medianArr[1], medianArr[2]


def split(arr, left, right):
    findMedian(arr, left, right)
    indexLeft = left
    indexRight = right - 1
    median = (left + right) // 2
    arr[median], arr[right] = arr[right], arr[(left + right) // 2]

    while a < b:

        if arr[a] > median:
            while True:
                if arr[indexRight] < median:
                    arr[indexLeft], arr[indexRight] = arr[indexRight], arr[indexLeft]
                    indexRight -= 1
                    break
                indexRight -= 1
        indexLeft += 1

    arr[indexLeft], arr[right] = arr[right], arr[indexLeft]

    return indexLeft

def split2(arr, left, right):
    indexleft = 0
    indexright = 0
    m = median3sort(arr, left, right)
    splitvalue = arr[m]
    arr[m], arr[right - 1] = arr[right - 1], arr[m]


def quicksort(arr, left, right):


    if (right - left > 2):
        splitIndex = split(arr, left, right)
        quicksort(arr, splitIndex + 1, right)
        quicksort(arr, left, splitIndex - 1)
    else: median3sort(arr, left, right)


print(arr)
split(arr, 0, 5)
print(arr)

