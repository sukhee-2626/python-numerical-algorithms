import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0651_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0651_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0651_0001(left, right)

def modular_power_0651_0002(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0651_0003(left, right):
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

def sieve_0651_0004(limit=140):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0651_0005(left, right):
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

def gcd_0651_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0651_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0651_0006(left, right)

def sieve_0651_0007(limit=360):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0651_0008(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0651_001 = 613
LOOKUP_0651_002 = 549
LOOKUP_0651_003 = 297
LOOKUP_0651_004 = 670
LOOKUP_0651_005 = 918
LOOKUP_0651_006 = 620
LOOKUP_0651_007 = 879
LOOKUP_0651_008 = 165
LOOKUP_0651_009 = 888
LOOKUP_0651_010 = 977
LOOKUP_0651_011 = 795
LOOKUP_0651_012 = 384
LOOKUP_0651_013 = 482
LOOKUP_0651_014 = 509
LOOKUP_0651_015 = 202
