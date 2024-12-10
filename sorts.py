import sys
from utils import Number
from math import ceil

sys.setrecursionlimit(10**6)


def bubble_sort(arr: list[Number]) -> list[Number]:
    size: int = len(arr)
    end: int = size - 1

    for i in range(end):
        swapped: bool = False
        for j in range(0, end - i):
            a, b = arr[j], arr[j + 1]
            if a > b:
                arr[j], arr[j + 1] = b, a
                swapped = True

        if not swapped:
            break

    return arr


def selection_sort(arr: list[Number]) -> list[Number]:
    size: int = len(arr)
    end: int = size - 1

    for i in range(end + 1):
        min_el_pointer: int = i

        for j in range(i + 1, end + 1):
            if arr[min_el_pointer] > arr[j]:
                min_el_pointer = j

        arr[i], arr[min_el_pointer] = arr[min_el_pointer], arr[i]

    return arr


# def quick_sort(arr: list[Number]) -> list[Number]:
#     if len(arr) < 2:
#         return arr

#     pivot = min([max([arr[0], arr[-1]]), arr[ceil(len(arr) / 2)]])

#     return [
#         *quick_sort([x for x in arr if x < pivot]),
#         *list(filter(lambda x: x == pivot, arr)),
#         *quick_sort([x for x in arr if x > pivot]),
#     ]


# 0.020589 seconds
def quick_sort(arr: list[Number]) -> list[Number]:
    if len(arr) < 2:
        return arr

    pivot = min([max([arr[0], arr[-1]]), arr[ceil(len(arr) / 2)]])
    less, equal, greater = ([], [], [])

    for x in arr:
        (less if x < pivot else greater if x > pivot else equal).append(x)

    return quick_sort(less) + equal + quick_sort(greater)
