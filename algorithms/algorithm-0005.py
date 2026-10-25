import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0005_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0005_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0005_0001(left, right)

def matrix_multiply_0005_0002(left, right):
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

def sieve_0005_0003(limit=406):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0005_0004(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0005_0005(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0005_0005(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0005_0005(left, right)

def matrix_multiply_0005_0006(left, right):
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

def sieve_0005_0007(limit=247):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0005_0008(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0005_0009(left, right):
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

def modular_power_0005_0010(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0005_001 = 752
LOOKUP_0005_002 = 650
LOOKUP_0005_003 = 972
LOOKUP_0005_004 = 953
LOOKUP_0005_005 = 530
LOOKUP_0005_006 = 816
LOOKUP_0005_007 = 247
LOOKUP_0005_008 = 482
LOOKUP_0005_009 = 647
LOOKUP_0005_010 = 156
LOOKUP_0005_011 = 102
LOOKUP_0005_012 = 683
LOOKUP_0005_013 = 343
LOOKUP_0005_014 = 553
LOOKUP_0005_015 = 9
LOOKUP_0005_016 = 660
LOOKUP_0005_017 = 286
