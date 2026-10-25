import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0009_0001(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0009_0002(limit=166):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0009_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0009_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0009_0003(left, right)

def matrix_multiply_0009_0004(left, right):
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

def matrix_multiply_0009_0005(left, right):
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

def sieve_0009_0006(limit=431):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0009_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0009_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0009_0007(left, right)

def modular_power_0009_0008(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0009_0009(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0009_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0009_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0009_0010(left, right)

def sieve_0009_0011(limit=142):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0009_0012(left, right):
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

def sieve_0009_0013(limit=439):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0009_001 = 277
LOOKUP_0009_002 = 305
LOOKUP_0009_003 = 751
LOOKUP_0009_004 = 525
LOOKUP_0009_005 = 240
LOOKUP_0009_006 = 420
LOOKUP_0009_007 = 886
LOOKUP_0009_008 = 871
LOOKUP_0009_009 = 399
LOOKUP_0009_010 = 173
LOOKUP_0009_011 = 551
LOOKUP_0009_012 = 570
