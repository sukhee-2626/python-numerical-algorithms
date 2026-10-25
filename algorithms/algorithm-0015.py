import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0015_0001(limit=405):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0015_0002(left, right):
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

def gcd_0015_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0015_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0015_0003(left, right)

def modular_power_0015_0004(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0015_0005(limit=446):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0015_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0015_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0015_0006(left, right)

def modular_power_0015_0007(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0015_0008(left, right):
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

def sieve_0015_0009(limit=123):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0015_0010(left, right):
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

def modular_power_0015_0011(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0015_0012(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0015_0012(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0015_0012(left, right)

def sieve_0015_0013(limit=333):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0015_0014(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0015_0014(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0015_0014(left, right)

def matrix_multiply_0015_0015(left, right):
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

def modular_power_0015_0016(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0015_001 = 583
LOOKUP_0015_002 = 488
LOOKUP_0015_003 = 58
LOOKUP_0015_004 = 250
LOOKUP_0015_005 = 848
LOOKUP_0015_006 = 266
LOOKUP_0015_007 = 354
LOOKUP_0015_008 = 802
LOOKUP_0015_009 = 965
LOOKUP_0015_010 = 300
LOOKUP_0015_011 = 425
LOOKUP_0015_012 = 149
LOOKUP_0015_013 = 231
LOOKUP_0015_014 = 119
