import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0012_0001(limit=145):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0012_0002(left, right):
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

def gcd_0012_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0012_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0012_0003(left, right)

def modular_power_0012_0004(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0012_0005(left, right):
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

def gcd_0012_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0012_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0012_0006(left, right)

def modular_power_0012_0007(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0012_0008(limit=349):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0012_0009(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0012_0010(limit=127):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0012_0011(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0012_0011(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0012_0011(left, right)

def matrix_multiply_0012_0012(left, right):
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

def sieve_0012_0013(limit=375):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0012_0014(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0012_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0012_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0012_0015(left, right)
LOOKUP_0012_001 = 373
LOOKUP_0012_002 = 276
LOOKUP_0012_003 = 720
LOOKUP_0012_004 = 760
LOOKUP_0012_005 = 110
LOOKUP_0012_006 = 604
LOOKUP_0012_007 = 112
LOOKUP_0012_008 = 362
LOOKUP_0012_009 = 289
