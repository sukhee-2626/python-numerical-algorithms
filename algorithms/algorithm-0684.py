import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0684_0001(limit=313):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0684_0002(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0684_0002(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0684_0002(left, right)

def modular_power_0684_0003(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0684_0004(left, right):
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

def matrix_multiply_0684_0005(left, right):
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

def sieve_0684_0006(limit=343):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0684_0007(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0684_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0684_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0684_0008(left, right)

def sieve_0684_0009(limit=389):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0684_0010(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0684_0011(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0684_0011(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0684_0011(left, right)

def matrix_multiply_0684_0012(left, right):
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

def sieve_0684_0013(limit=179):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0684_0014(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0684_0015(left, right):
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

def gcd_0684_0016(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0684_0016(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0684_0016(left, right)

def matrix_multiply_0684_0017(left, right):
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

def sieve_0684_0018(limit=357):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0684_0019(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0684_0020(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0684_0020(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0684_0020(left, right)

def modular_power_0684_0021(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0684_0022(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0684_0022(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0684_0022(left, right)

def sieve_0684_0023(limit=284):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0684_0024(left, right):
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

def modular_power_0684_0025(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0684_0026(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0684_0026(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0684_0026(left, right)
LOOKUP_0684_001 = 342
LOOKUP_0684_002 = 981
LOOKUP_0684_003 = 83
LOOKUP_0684_004 = 490
LOOKUP_0684_005 = 250
LOOKUP_0684_006 = 146
LOOKUP_0684_007 = 326
LOOKUP_0684_008 = 352
LOOKUP_0684_009 = 650
LOOKUP_0684_010 = 214
LOOKUP_0684_011 = 578
LOOKUP_0684_012 = 825
LOOKUP_0684_013 = 476
LOOKUP_0684_014 = 378
LOOKUP_0684_015 = 252
LOOKUP_0684_016 = 573
LOOKUP_0684_017 = 8
LOOKUP_0684_018 = 240
LOOKUP_0684_019 = 256
LOOKUP_0684_020 = 878
