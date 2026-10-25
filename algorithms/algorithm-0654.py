import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0654_0001(limit=128):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0654_0002(left, right):
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

def gcd_0654_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0654_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0654_0003(left, right)

def modular_power_0654_0004(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0654_0005(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0654_0005(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0654_0005(left, right)

def matrix_multiply_0654_0006(left, right):
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

def modular_power_0654_0007(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0654_0008(limit=429):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0654_0009(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0654_0010(limit=426):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0654_001 = 378
LOOKUP_0654_002 = 962
LOOKUP_0654_003 = 951
LOOKUP_0654_004 = 936
LOOKUP_0654_005 = 501
LOOKUP_0654_006 = 443
LOOKUP_0654_007 = 274
LOOKUP_0654_008 = 688
LOOKUP_0654_009 = 577
LOOKUP_0654_010 = 410
LOOKUP_0654_011 = 366
LOOKUP_0654_012 = 204
LOOKUP_0654_013 = 788
LOOKUP_0654_014 = 733
