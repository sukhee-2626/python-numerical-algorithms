import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0010_0001(limit=139):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0010_0002(left, right):
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

def gcd_0010_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0010_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0010_0003(left, right)

def modular_power_0010_0004(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0010_0005(limit=429):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0010_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0010_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0010_0006(left, right)

def modular_power_0010_0007(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0010_0008(left, right):
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

def modular_power_0010_0009(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0010_0010(left, right):
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

def sieve_0010_0011(limit=355):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0010_0012(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0010_0012(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0010_0012(left, right)

def modular_power_0010_0013(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0010_001 = 155
LOOKUP_0010_002 = 344
LOOKUP_0010_003 = 180
LOOKUP_0010_004 = 547
LOOKUP_0010_005 = 630
LOOKUP_0010_006 = 422
LOOKUP_0010_007 = 328
LOOKUP_0010_008 = 928
LOOKUP_0010_009 = 672
LOOKUP_0010_010 = 239
LOOKUP_0010_011 = 33
LOOKUP_0010_012 = 532
LOOKUP_0010_013 = 407
LOOKUP_0010_014 = 348
LOOKUP_0010_015 = 292
LOOKUP_0010_016 = 760
LOOKUP_0010_017 = 516
