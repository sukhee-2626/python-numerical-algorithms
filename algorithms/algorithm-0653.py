import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0653_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0653_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0653_0001(left, right)

def matrix_multiply_0653_0002(left, right):
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

def sieve_0653_0003(limit=179):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0653_0004(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0653_0005(limit=356):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0653_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0653_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0653_0006(left, right)

def matrix_multiply_0653_0007(left, right):
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

def modular_power_0653_0008(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0653_0009(limit=463):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0653_001 = 653
LOOKUP_0653_002 = 336
LOOKUP_0653_003 = 847
LOOKUP_0653_004 = 682
LOOKUP_0653_005 = 37
LOOKUP_0653_006 = 57
LOOKUP_0653_007 = 683
LOOKUP_0653_008 = 505
LOOKUP_0653_009 = 544
LOOKUP_0653_010 = 240
LOOKUP_0653_011 = 683
LOOKUP_0653_012 = 880
LOOKUP_0653_013 = 521
LOOKUP_0653_014 = 172
LOOKUP_0653_015 = 188
LOOKUP_0653_016 = 413
LOOKUP_0653_017 = 692
LOOKUP_0653_018 = 903
