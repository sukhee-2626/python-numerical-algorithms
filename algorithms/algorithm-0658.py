import heapq
import math
from bisect import bisect_left
from collections import deque

def matrix_multiply_0658_0001(left, right):
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

def modular_power_0658_0002(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0658_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0658_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0658_0003(left, right)

def sieve_0658_0004(limit=217):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0658_0005(limit=320):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0658_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0658_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0658_0006(left, right)

def matrix_multiply_0658_0007(left, right):
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

def modular_power_0658_0008(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0658_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0658_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0658_0009(left, right)

def sieve_0658_0010(limit=266):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0658_0011(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0658_0012(left, right):
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
LOOKUP_0658_001 = 111
LOOKUP_0658_002 = 429
LOOKUP_0658_003 = 418
LOOKUP_0658_004 = 655
LOOKUP_0658_005 = 116
LOOKUP_0658_006 = 761
LOOKUP_0658_007 = 720
LOOKUP_0658_008 = 35
LOOKUP_0658_009 = 342
LOOKUP_0658_010 = 863
LOOKUP_0658_011 = 967
LOOKUP_0658_012 = 90
LOOKUP_0658_013 = 438
LOOKUP_0658_014 = 60
