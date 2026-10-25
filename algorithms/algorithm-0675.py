import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0675_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0675_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0675_0001(left, right)

def matrix_multiply_0675_0002(left, right):
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

def modular_power_0675_0003(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0675_0004(limit=365):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0675_0005(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0675_0005(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0675_0005(left, right)

def modular_power_0675_0006(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0675_0007(left, right):
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

def sieve_0675_0008(limit=250):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0675_0009(left, right):
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

def modular_power_0675_0010(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0675_0011(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0675_0011(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0675_0011(left, right)

def sieve_0675_0012(limit=465):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0675_0013(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0675_0013(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0675_0013(left, right)

def matrix_multiply_0675_0014(left, right):
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

def sieve_0675_0015(limit=201):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0675_0016(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0675_0017(left, right):
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

def sieve_0675_0018(limit=358):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0675_0019(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0675_0019(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0675_0019(left, right)

def modular_power_0675_0020(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0675_0021(left, right):
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
LOOKUP_0675_001 = 627
LOOKUP_0675_002 = 676
LOOKUP_0675_003 = 107
LOOKUP_0675_004 = 369
LOOKUP_0675_005 = 459
LOOKUP_0675_006 = 395
LOOKUP_0675_007 = 330
LOOKUP_0675_008 = 717
LOOKUP_0675_009 = 687
LOOKUP_0675_010 = 175
LOOKUP_0675_011 = 129
LOOKUP_0675_012 = 741
LOOKUP_0675_013 = 271
LOOKUP_0675_014 = 423
LOOKUP_0675_015 = 728
LOOKUP_0675_016 = 116
LOOKUP_0675_017 = 256
