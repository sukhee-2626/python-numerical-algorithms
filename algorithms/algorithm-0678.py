import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0678_0001(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0678_0002(left, right):
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

def sieve_0678_0003(limit=273):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0678_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0678_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0678_0004(left, right)

def matrix_multiply_0678_0005(left, right):
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

def modular_power_0678_0006(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0678_0007(limit=287):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0678_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0678_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0678_0008(left, right)

def modular_power_0678_0009(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0678_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0678_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0678_0010(left, right)

def sieve_0678_0011(limit=346):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0678_0012(left, right):
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

def sieve_0678_0013(limit=450):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0678_0014(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0678_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0678_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0678_0015(left, right)

def matrix_multiply_0678_0016(left, right):
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

def modular_power_0678_0017(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0678_0018(left, right):
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

def sieve_0678_0019(limit=135):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0678_0020(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0678_0020(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0678_0020(left, right)

def gcd_0678_0021(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0678_0021(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0678_0021(left, right)

def modular_power_0678_0022(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0678_0023(limit=417):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0678_001 = 806
LOOKUP_0678_002 = 382
LOOKUP_0678_003 = 160
LOOKUP_0678_004 = 402
LOOKUP_0678_005 = 785
LOOKUP_0678_006 = 348
LOOKUP_0678_007 = 57
LOOKUP_0678_008 = 614
LOOKUP_0678_009 = 667
LOOKUP_0678_010 = 453
LOOKUP_0678_011 = 778
LOOKUP_0678_012 = 878
LOOKUP_0678_013 = 19
LOOKUP_0678_014 = 120
LOOKUP_0678_015 = 374
LOOKUP_0678_016 = 172
LOOKUP_0678_017 = 205
LOOKUP_0678_018 = 131
