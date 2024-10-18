#!/usr/bin/python3
'''
Modeule that provide the minOperations method.
'''


def minOperations(n: int) -> int:
    '''
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    '''
    operation = 0
    storage = 0
    chars = 1

    while chars < n:
        if storage == 0:
            storage = chars
            chars += storage
            operation = 2
        elif (n - chars) % chars == 0:
            storage = chars
            chars += storage
            operation += 2
        else:
            chars += storage
            operation += 1

    return operation
