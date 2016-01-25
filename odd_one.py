# coding=utf-8
__name__ = "vutsuak"

"""Given a set of numbers where all elements occur even number of times except one number, find the odd occuring number”
This problem can be efficiently solved by just doing XOR of all numbers."""

import random as rand


def odd_one():
    arr = []
    for i in range(10):
        arr.append(rand.randrange(1, 101))
    crr = arr + arr
    crr.append(rand.randrange(1, 101))
    xored = 0
    for i in crr:
        xored ^= i
    print crr
    print xored


if __name__ == "vutsuak":
    odd_one()
