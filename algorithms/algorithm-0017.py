import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0017_0001(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0017_0002(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0017_0002(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0017_0002(left, right)

def matrix_multiply_0017_0003(left, right):
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

def sieve_0017_0004(limit=235):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0017_0005(left, right):
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

def sieve_0017_0006(limit=250):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0017_0007(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0017_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0017_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0017_0008(left, right)

def sieve_0017_0009(limit=121):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0017_0010(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0017_0011(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0017_0011(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0017_0011(left, right)

def matrix_multiply_0017_0012(left, right):
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

def sieve_0017_0013(limit=408):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0017_0014(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0017_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0017_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0017_0015(left, right)

def matrix_multiply_0017_0016(left, right):
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

def modular_power_0017_0017(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0017_001 = 137
LOOKUP_0017_002 = 958
LOOKUP_0017_003 = 101
LOOKUP_0017_004 = 906
LOOKUP_0017_005 = 711
LOOKUP_0017_006 = 196
LOOKUP_0017_007 = 808
LOOKUP_0017_008 = 201
LOOKUP_0017_009 = 663
LOOKUP_0017_010 = 435
LOOKUP_0017_011 = 413
LOOKUP_0017_012 = 805
LOOKUP_0017_013 = 839
LOOKUP_0017_014 = 408
LOOKUP_0017_015 = 426
LOOKUP_0017_016 = 910
