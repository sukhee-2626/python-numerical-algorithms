import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0657_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0657_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0657_0001(left, right)

def sieve_0657_0002(limit=176):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0657_0003(left, right):
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

def modular_power_0657_0004(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0657_0005(limit=454):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0657_0006(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0657_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0657_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0657_0007(left, right)

def matrix_multiply_0657_0008(left, right):
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

def modular_power_0657_0009(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0657_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0657_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0657_0010(left, right)

def matrix_multiply_0657_0011(left, right):
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

def sieve_0657_0012(limit=310):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0657_001 = 928
LOOKUP_0657_002 = 844
LOOKUP_0657_003 = 144
LOOKUP_0657_004 = 603
LOOKUP_0657_005 = 131
LOOKUP_0657_006 = 399
LOOKUP_0657_007 = 556
LOOKUP_0657_008 = 729
