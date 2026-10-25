import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0013_0001(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0013_0002(left, right):
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

def sieve_0013_0003(limit=442):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0013_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0013_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0013_0004(left, right)

def matrix_multiply_0013_0005(left, right):
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

def sieve_0013_0006(limit=376):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0013_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0013_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0013_0007(left, right)

def modular_power_0013_0008(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0013_0009(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0013_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0013_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0013_0010(left, right)

def sieve_0013_0011(limit=336):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0013_0012(left, right):
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

def sieve_0013_0013(limit=351):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0013_0014(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0013_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0013_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0013_0015(left, right)
LOOKUP_0013_001 = 141
LOOKUP_0013_002 = 445
LOOKUP_0013_003 = 741
LOOKUP_0013_004 = 105
LOOKUP_0013_005 = 932
LOOKUP_0013_006 = 733
LOOKUP_0013_007 = 877
LOOKUP_0013_008 = 428
LOOKUP_0013_009 = 67
LOOKUP_0013_010 = 396
LOOKUP_0013_011 = 12
LOOKUP_0013_012 = 535
LOOKUP_0013_013 = 506
LOOKUP_0013_014 = 175
LOOKUP_0013_015 = 366
