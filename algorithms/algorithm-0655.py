import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0655_0001(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0655_0002(left, right):
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

def gcd_0655_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0655_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0655_0003(left, right)

def sieve_0655_0004(limit=228):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0655_0005(limit=373):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0655_0006(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0655_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0655_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0655_0007(left, right)

def matrix_multiply_0655_0008(left, right):
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

def sieve_0655_0009(limit=457):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0655_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0655_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0655_0010(left, right)
LOOKUP_0655_001 = 736
LOOKUP_0655_002 = 755
LOOKUP_0655_003 = 923
LOOKUP_0655_004 = 365
LOOKUP_0655_005 = 509
LOOKUP_0655_006 = 608
LOOKUP_0655_007 = 849
LOOKUP_0655_008 = 578
LOOKUP_0655_009 = 614
LOOKUP_0655_010 = 954
LOOKUP_0655_011 = 75
LOOKUP_0655_012 = 368
LOOKUP_0655_013 = 274
LOOKUP_0655_014 = 466
LOOKUP_0655_015 = 744
LOOKUP_0655_016 = 39
LOOKUP_0655_017 = 685
LOOKUP_0655_018 = 877
LOOKUP_0655_019 = 260
