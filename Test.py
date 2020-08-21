arr = [5, 3, 4, 1, 2]
import time


def select():
    global arr
    for i in range(len(arr) - 1, -1, -1):
        imin = 0
        print(arr)
        for j in range(1, i + 1):
            if arr[imin] < arr[j]:
                imin = j
        arr[i], arr[imin] = arr[imin], arr[i]
        print(arr)


def bubble_sort():
    count = 0
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
        count += 1
    return count


def insertion_sort():
    for i in range(1, len(arr)):
        curr_el = arr[i]
        pos = i
        while curr_el < arr[pos - 1] and pos > 0:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
            print(arr)
        arr[pos] = curr_el
    print(arr)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    print("Pivot:" + str(pivot))
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
    print(arr)

print("Sorted:")
# print(select())
# print(bubble_sort())
# print(insertion_sort())
print(arr)
quickSort(arr, 0, len(arr) - 1)
