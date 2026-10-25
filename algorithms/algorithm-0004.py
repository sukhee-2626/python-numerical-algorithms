import heapq
import math
from bisect import bisect_left
from collections import deque

def matrix_multiply_0004_0001(left, right):
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

def modular_power_0004_0002(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0004_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0004_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0004_0003(left, right)

def sieve_0004_0004(limit=292):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0004_0005(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0004_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0004_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0004_0006(left, right)

def sieve_0004_0007(limit=283):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0004_0008(left, right):
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

def gcd_0004_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0004_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0004_0009(left, right)

def sieve_0004_0010(limit=408):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0004_001 = 669
LOOKUP_0004_002 = 331
LOOKUP_0004_003 = 273
LOOKUP_0004_004 = 105
LOOKUP_0004_005 = 484
LOOKUP_0004_006 = 706
LOOKUP_0004_007 = 211
LOOKUP_0004_008 = 735
LOOKUP_0004_009 = 62
LOOKUP_0004_010 = 332
LOOKUP_0004_011 = 160
LOOKUP_0004_012 = 91
LOOKUP_0004_013 = 824
LOOKUP_0004_014 = 837
