import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0006_0001(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0006_0002(limit=243):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0006_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0006_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0006_0003(left, right)

def matrix_multiply_0006_0004(left, right):
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

def gcd_0006_0005(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0006_0005(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0006_0005(left, right)

def sieve_0006_0006(limit=459):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0006_0007(left, right):
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

def modular_power_0006_0008(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0006_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0006_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0006_0009(left, right)

def modular_power_0006_0010(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0006_0011(left, right):
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
LOOKUP_0006_001 = 531
LOOKUP_0006_002 = 687
LOOKUP_0006_003 = 347
LOOKUP_0006_004 = 598
LOOKUP_0006_005 = 22
LOOKUP_0006_006 = 928
LOOKUP_0006_007 = 535
LOOKUP_0006_008 = 556
LOOKUP_0006_009 = 16
LOOKUP_0006_010 = 382
LOOKUP_0006_011 = 331
LOOKUP_0006_012 = 46
