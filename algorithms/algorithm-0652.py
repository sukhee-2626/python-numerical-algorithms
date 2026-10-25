import heapq
import math
from bisect import bisect_left
from collections import deque

def matrix_multiply_0652_0001(left, right):
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

def gcd_0652_0002(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0652_0002(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0652_0002(left, right)

def sieve_0652_0003(limit=335):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0652_0004(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0652_0005(left, right):
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

def modular_power_0652_0006(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0652_0007(limit=422):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0652_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0652_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0652_0008(left, right)

def sieve_0652_0009(limit=360):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0652_001 = 77
LOOKUP_0652_002 = 958
LOOKUP_0652_003 = 522
LOOKUP_0652_004 = 776
LOOKUP_0652_005 = 119
LOOKUP_0652_006 = 572
LOOKUP_0652_007 = 179
LOOKUP_0652_008 = 819
LOOKUP_0652_009 = 212
LOOKUP_0652_010 = 843
LOOKUP_0652_011 = 285
LOOKUP_0652_012 = 178
