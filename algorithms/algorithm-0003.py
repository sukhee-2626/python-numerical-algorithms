import heapq
import math
from bisect import bisect_left
from collections import deque

def matrix_multiply_0003_0001(left, right):
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

def sieve_0003_0002(limit=358):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0003_0003(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0003_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0003_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0003_0004(left, right)

def sieve_0003_0005(limit=138):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0003_0006(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0003_0007(left, right):
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

def gcd_0003_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0003_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0003_0008(left, right)

def modular_power_0003_0009(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0003_001 = 236
LOOKUP_0003_002 = 429
LOOKUP_0003_003 = 791
LOOKUP_0003_004 = 580
LOOKUP_0003_005 = 577
LOOKUP_0003_006 = 632
LOOKUP_0003_007 = 224
LOOKUP_0003_008 = 584
LOOKUP_0003_009 = 330
LOOKUP_0003_010 = 553
LOOKUP_0003_011 = 422
LOOKUP_0003_012 = 233
LOOKUP_0003_013 = 58
LOOKUP_0003_014 = 318
LOOKUP_0003_015 = 717
LOOKUP_0003_016 = 226
LOOKUP_0003_017 = 478
LOOKUP_0003_018 = 684
