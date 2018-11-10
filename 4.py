""" Challenge

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.
For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3."""


def solution(a):
    """ Tarverses array and maps its values that aren't 0 or smaller or higher than array length 
        to their respective index in array (value 3 will be mapped to index 2), afterwards it traveres newly "sorted" array, 
        once it finds value that is not mapped correctly (for example 4 on position 2) it means that value that should be mapped at that index 
        wasn't in original array and should be returned, otherwise if it gets to the end of array it means that smallest value that is missing 
        equals to array length + 1 because, all members of array were mapped to their positions in array.

        Complexity O(n)"""

    arr_len = len(a)
    # Even though there is loop inside of loop this solution is still
    # O(n) because if value is processed by inner loop it will be skipped once outer loop gets to it
    # because its already in its place in array
    for i, v in enumerate(a):
        # if current value is 0 we don't care about since we are looking for
        # positive integers only and if current value is higher than array length
        # we don't care about it because max missing value can't be higher than array length
        if not 0 <= v < arr_len:
            continue
        # this part of code will keep assigning current value to its index in array until it gets to value
        # that is already at its index or higher than array length
        # example if we've got array [3, 4, 5, 1, 7]
        # we will acquire value at index 1, which is 3,
        # then we will got to third array member
        # store its value to temp variable and assign current value in its place
        # now we will use value which 3 replaced as our current value and repeat whole process again
        # since we replaced 5 with 3, new current value is 5
        # we go to 5th array member and replace its value with our 5 and store its old value in temp variable
        # and repeat whole process again until current value is smaller than 0 or higher than length of array,
        # because we don't need to (or can) map those values in their respective places in array
        while a[v - 1] != v:
            # put value at index where our current value should be
            # in temp variable
            temp = a[v - 1]
            # put our current value in its place in array
            a[v - 1] = v
            # make temp value new current value, and repeat whole process again
            # unless our new current value is not between zero and array length,
            # then we should just ignore them
            v = temp
            if v <= 0 or v > arr_len:
                break
    # iterates newly "sorted" array until it finds unmapped value,
    # if it finds unmapped value returns its index + 1
    for i, v in enumerate(a):
        if v != i + 1:
            return i + 1
    # if we got to this point this means all values up until array length are preset
    # and because of that lowest positive integer array length + 1
    return arr_len + 1


assert solution([3, 4, 5, 1, 7]) == 2
assert solution([3, 4, -1, 1, 7]) == 2
assert solution([1, 2, 0]) == 3
assert solution([1, 2, 3]) == 4
