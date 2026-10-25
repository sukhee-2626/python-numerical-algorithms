import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0674_0001(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0674_0002(limit=463):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0674_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0674_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0674_0003(left, right)

def matrix_multiply_0674_0004(left, right):
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

def matrix_multiply_0674_0005(left, right):
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

def modular_power_0674_0006(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0674_0007(limit=323):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0674_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0674_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0674_0008(left, right)

def sieve_0674_0009(limit=479):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0674_0010(left, right):
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

def gcd_0674_0011(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0674_0011(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0674_0011(left, right)

def modular_power_0674_0012(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0674_0013(limit=171):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0674_0014(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0674_0015(left, right):
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

def gcd_0674_0016(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0674_0016(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0674_0016(left, right)

def sieve_0674_0017(limit=209):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0674_0018(left, right):
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

def gcd_0674_0019(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0674_0019(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0674_0019(left, right)

def modular_power_0674_0020(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0674_0021(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0674_001 = 431
LOOKUP_0674_002 = 213
LOOKUP_0674_003 = 361
LOOKUP_0674_004 = 747
LOOKUP_0674_005 = 368
LOOKUP_0674_006 = 521
LOOKUP_0674_007 = 321
LOOKUP_0674_008 = 455
LOOKUP_0674_009 = 641
LOOKUP_0674_010 = 222
LOOKUP_0674_011 = 33
LOOKUP_0674_012 = 31
LOOKUP_0674_013 = 308
LOOKUP_0674_014 = 131
