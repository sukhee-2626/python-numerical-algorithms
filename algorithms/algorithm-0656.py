import heapq
import math
from bisect import bisect_left
from collections import deque

def matrix_multiply_0656_0001(left, right):
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

def sieve_0656_0002(limit=201):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0656_0003(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0656_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0656_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0656_0004(left, right)

def modular_power_0656_0005(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0656_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0656_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0656_0006(left, right)

def sieve_0656_0007(limit=296):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0656_0008(left, right):
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

def gcd_0656_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0656_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0656_0009(left, right)

def matrix_multiply_0656_0010(left, right):
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

def modular_power_0656_0011(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0656_001 = 854
LOOKUP_0656_002 = 815
LOOKUP_0656_003 = 199
LOOKUP_0656_004 = 626
LOOKUP_0656_005 = 356
LOOKUP_0656_006 = 480
LOOKUP_0656_007 = 382
LOOKUP_0656_008 = 934
LOOKUP_0656_009 = 31
LOOKUP_0656_010 = 928
LOOKUP_0656_011 = 401
