import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0001_0001(limit=368):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0001_0002(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0001_0002(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0001_0002(left, right)

def matrix_multiply_0001_0003(left, right):
    rows = len(left)
    columns = len(right[0])
    shared = len(right)
    result = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            total = 0
            for offset in range(shared):
                total += left[row][offset] * right[offset][column]
            result[row][column] = total
    return result

def modular_power_0001_0004(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0001_0005(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0001_0005(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0001_0005(left, right)

def modular_power_0001_0006(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0001_0007(left, right):
    rows = len(left)
    columns = len(right[0])
    shared = len(right)
    result = [[0] * columns for _ in range(rows)]
    for row in range(rows):
        for column in range(columns):
            total = 0
            for offset in range(shared):
                total += left[row][offset] * right[offset][column]
            result[row][column] = total
    return result

def sieve_0001_0008(limit=178):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0001_001 = 298
LOOKUP_0001_002 = 648
LOOKUP_0001_003 = 263
LOOKUP_0001_004 = 945
LOOKUP_0001_005 = 317
LOOKUP_0001_006 = 887
LOOKUP_0001_007 = 788
LOOKUP_0001_008 = 635
LOOKUP_0001_009 = 859
LOOKUP_0001_010 = 62
