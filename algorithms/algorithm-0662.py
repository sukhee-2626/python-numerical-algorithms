import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0662_0001(limit=418):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0662_0002(left, right):
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

def modular_power_0662_0003(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0662_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0662_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0662_0004(left, right)

def modular_power_0662_0005(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0662_0006(limit=436):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0662_0007(left, right):
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

def gcd_0662_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0662_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0662_0008(left, right)

def gcd_0662_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0662_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0662_0009(left, right)

def modular_power_0662_0010(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0662_0011(left, right):
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

def sieve_0662_0012(limit=479):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0662_0013(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0662_0014(left, right):
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
LOOKUP_0662_001 = 925
LOOKUP_0662_002 = 718
LOOKUP_0662_003 = 237
LOOKUP_0662_004 = 799
LOOKUP_0662_005 = 93
LOOKUP_0662_006 = 439
LOOKUP_0662_007 = 718
LOOKUP_0662_008 = 315
LOOKUP_0662_009 = 305
LOOKUP_0662_010 = 878
LOOKUP_0662_011 = 421
LOOKUP_0662_012 = 144
LOOKUP_0662_013 = 965
LOOKUP_0662_014 = 32
LOOKUP_0662_015 = 488
