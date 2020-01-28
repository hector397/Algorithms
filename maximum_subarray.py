from typing import *
import timeit

"""
Finds the maximum subarray in an array using brute force
"""
def brute_force_maximum_subarray(array: List, low: int, high: int) -> Tuple:
    if len(array) == 0:
        return low, high, 0
    else:
        left = low
        right = high
        maxSum = array[0]

        for i in range(high):
            sum = 0

            for j in range(i, high):
                sum += array[j]

                if sum > maxSum:
                    maxSum = sum
                    left = i
                    right = j

        return left, right, maxSum


"""
Finds maximum subarray in an array using recursivity
"""
def recursive_maximum_subarray(array: List, low: int, high: int) -> Tuple:
    if len(array) == 0:
        return low, high, 0
    elif high == low:
        return low, high, array[low]
    else:
        mid = (low + high) // 2

        left_low, left_high, left_sum = recursive_maximum_subarray(array, low, mid)
        right_low, right_high, right_sum = recursive_maximum_subarray(array, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


"""
Find maximum subarray crossing the midpoint
"""
def find_max_crossing_subarray(array: List, low: int, mid: int, high: int) -> Tuple:
    left_sum = -50000
    sum = 0

    for i in range(mid, low - 1, -1):
        sum += array[i]

        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -50000
    sum = 0

    for j in range(mid + 1, high + 1):
        sum += array[j]

        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum + right_sum