import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0660_0001(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0660_0002(limit=317):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0660_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0660_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0660_0003(left, right)

def matrix_multiply_0660_0004(left, right):
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

def gcd_0660_0005(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0660_0005(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0660_0005(left, right)

def modular_power_0660_0006(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0660_0007(limit=255):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0660_0008(left, right):
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

def modular_power_0660_0009(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0660_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0660_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0660_0010(left, right)

def sieve_0660_0011(limit=149):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0660_0012(left, right):
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

def sieve_0660_0013(limit=438):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0660_001 = 205
LOOKUP_0660_002 = 927
LOOKUP_0660_003 = 702
LOOKUP_0660_004 = 769
LOOKUP_0660_005 = 805
LOOKUP_0660_006 = 175
LOOKUP_0660_007 = 285
LOOKUP_0660_008 = 88
LOOKUP_0660_009 = 917
LOOKUP_0660_010 = 223
LOOKUP_0660_011 = 667
LOOKUP_0660_012 = 448
LOOKUP_0660_013 = 612
LOOKUP_0660_014 = 801
LOOKUP_0660_015 = 506
LOOKUP_0660_016 = 854
LOOKUP_0660_017 = 443
