""" Challenge

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?"""


def solution1(a):
    """ First solution

    iterate array and get product of all elements in array(wp), 
    afterwards iterate array again and divide wp with current element.

    Complexity O(n)
    """

    wp = 1
    for i in a:
        wp *= i
    return [wp/i for i in a]


assert solution1([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert solution1([3, 2, 1]) == [2, 3, 6]


def solution2(a):
    """ Second solution, no division

    Not my solution :(.

    Complexity O(n)
    """
    
    length = len(a)
    r = [1] * length
    temp = 1
    i = 0
    while i < length:
        r[i] = temp
        temp *= a[i]
        i += 1

    temp = 1
    i = length - 1
    while i >= 0:
        r[i] *= temp
        temp *= a[i]
        i -= 1

    return r


assert solution2([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert solution2([3, 2, 1]) == [2, 3, 6]
