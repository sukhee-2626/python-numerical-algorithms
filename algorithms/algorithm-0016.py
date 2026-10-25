import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0016_0001(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0016_0002(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0016_0002(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0016_0002(left, right)

def sieve_0016_0003(limit=358):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0016_0004(left, right):
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

def matrix_multiply_0016_0005(left, right):
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

def modular_power_0016_0006(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0016_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0016_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0016_0007(left, right)

def sieve_0016_0008(limit=286):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0016_0009(limit=219):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0016_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0016_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0016_0010(left, right)

def modular_power_0016_0011(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0016_0012(left, right):
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

def gcd_0016_0013(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0016_0013(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0016_0013(left, right)

def modular_power_0016_0014(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0016_0015(limit=427):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0016_0016(left, right):
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

def gcd_0016_0017(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0016_0017(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0016_0017(left, right)
LOOKUP_0016_001 = 695
LOOKUP_0016_002 = 601
LOOKUP_0016_003 = 710
LOOKUP_0016_004 = 334
LOOKUP_0016_005 = 771
LOOKUP_0016_006 = 622
LOOKUP_0016_007 = 167
LOOKUP_0016_008 = 958
LOOKUP_0016_009 = 777
