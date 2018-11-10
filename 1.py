""" Challenge

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass? """


def solution1(l, k):
    """ First solution

    iterate array and for each element iterate array again,
    but start second iteration from elements index + 1,
    because all elements with index lower than current elements index were already checked
    and element with current index is being currently checked. 

    Complexity O(n^2)
    """

    i = 0
    length = len(l)
    while i < length:
        j = i + 1
        v = l[i]
        while j < length:
            if v + l[j] == k:
                return True
            j = j + 1
        i += 1

    return False


assert solution1([10, 15, 3, 7], 17)
assert solution1([10, 15, 3, 7], 13)
assert not solution1([10, 15, 3, 7], 21)


def solution2(l, k):
    """ Second solution

    iterate array and and check whether k - current value exists in dictionary 
    if it exists return true, because pair of current value that adds up to k 
    was already found, otherwise add current value to dictionary.

    Complexity O(n)
    """

    d = {}
    for v in l:
        if k - v in d:
            return True
        d[v] = 1
    return False


assert solution2([10, 15, 3, 7], 17)
assert solution2([10, 15, 3, 7], 13)
assert not solution2([10, 15, 3, 7], 21)
assert not solution2([10, 15, 3, 7], 20)
