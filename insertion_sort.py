from typing import *


def insertion_sort(array: List) -> None:
    """
    Sort an array in increasing order

    Parameters:
         array: List of integers
    """

    for j in range(2, len(array)):
        key = array[j]

        i = j - 1

        while i > 0 and array[i] < key:
            array[i + 1] = array[i]
            i -= 1

        array[i + 1] = key
