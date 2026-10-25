import heapq
import math
from bisect import bisect_left
from collections import deque

def matrix_multiply_0007_0001(left, right):
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

def modular_power_0007_0002(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0007_0003(limit=312):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0007_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0007_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0007_0004(left, right)

def gcd_0007_0005(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0007_0005(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0007_0005(left, right)

def matrix_multiply_0007_0006(left, right):
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

def sieve_0007_0007(limit=251):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0007_0008(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0007_0009(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0007_0010(limit=178):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0007_0011(left, right):
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

def gcd_0007_0012(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0007_0012(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0007_0012(left, right)
LOOKUP_0007_001 = 184
LOOKUP_0007_002 = 664
LOOKUP_0007_003 = 441
LOOKUP_0007_004 = 165
LOOKUP_0007_005 = 206
LOOKUP_0007_006 = 340
LOOKUP_0007_007 = 787
LOOKUP_0007_008 = 920
LOOKUP_0007_009 = 647
