import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0002_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0002_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0002_0001(left, right)

def modular_power_0002_0002(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0002_0003(left, right):
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

def sieve_0002_0004(limit=172):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0002_0005(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0002_0005(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0002_0005(left, right)

def sieve_0002_0006(limit=378):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0002_0007(left, right):
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

def modular_power_0002_0008(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0002_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0002_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0002_0009(left, right)
LOOKUP_0002_001 = 276
LOOKUP_0002_002 = 123
LOOKUP_0002_003 = 782
LOOKUP_0002_004 = 219
LOOKUP_0002_005 = 575
LOOKUP_0002_006 = 506
LOOKUP_0002_007 = 245
LOOKUP_0002_008 = 165
LOOKUP_0002_009 = 159
LOOKUP_0002_010 = 285
LOOKUP_0002_011 = 452
