import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0663_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0663_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0663_0001(left, right)

def sieve_0663_0002(limit=453):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0663_0003(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0663_0004(left, right):
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

def matrix_multiply_0663_0005(left, right):
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

def sieve_0663_0006(limit=244):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0663_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0663_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0663_0007(left, right)

def modular_power_0663_0008(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0663_0009(left, right):
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

def modular_power_0663_0010(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0663_0011(limit=460):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0663_0012(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0663_0012(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0663_0012(left, right)

def sieve_0663_0013(limit=417):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0663_0014(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0663_0014(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0663_0014(left, right)

def modular_power_0663_0015(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0663_001 = 523
LOOKUP_0663_002 = 526
LOOKUP_0663_003 = 134
LOOKUP_0663_004 = 407
LOOKUP_0663_005 = 652
LOOKUP_0663_006 = 826
LOOKUP_0663_007 = 987
LOOKUP_0663_008 = 731
LOOKUP_0663_009 = 129
LOOKUP_0663_010 = 636
LOOKUP_0663_011 = 464
LOOKUP_0663_012 = 442
LOOKUP_0663_013 = 443
LOOKUP_0663_014 = 124
