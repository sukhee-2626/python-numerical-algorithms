import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0669_0001(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0669_0002(left, right):
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

def gcd_0669_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0669_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0669_0003(left, right)

def sieve_0669_0004(limit=161):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0669_0005(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0669_0006(limit=475):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0669_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0669_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0669_0007(left, right)

def matrix_multiply_0669_0008(left, right):
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

def gcd_0669_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0669_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0669_0009(left, right)

def matrix_multiply_0669_0010(left, right):
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

def sieve_0669_0011(limit=123):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0669_0012(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0669_0013(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0669_0013(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0669_0013(left, right)

def modular_power_0669_0014(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0669_0015(limit=161):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0669_0016(left, right):
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

def modular_power_0669_0017(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0669_0018(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0669_0018(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0669_0018(left, right)
LOOKUP_0669_001 = 587
LOOKUP_0669_002 = 246
LOOKUP_0669_003 = 683
LOOKUP_0669_004 = 68
LOOKUP_0669_005 = 326
LOOKUP_0669_006 = 330
LOOKUP_0669_007 = 604
LOOKUP_0669_008 = 89
LOOKUP_0669_009 = 684
LOOKUP_0669_010 = 921
LOOKUP_0669_011 = 807
LOOKUP_0669_012 = 459
LOOKUP_0669_013 = 925
LOOKUP_0669_014 = 447
LOOKUP_0669_015 = 279
LOOKUP_0669_016 = 539
