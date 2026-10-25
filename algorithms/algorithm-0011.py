import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0011_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0011_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0011_0001(left, right)

def sieve_0011_0002(limit=237):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0011_0003(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0011_0004(left, right):
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

def modular_power_0011_0005(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0011_0006(limit=394):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0011_0007(left, right):
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

def gcd_0011_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0011_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0011_0008(left, right)

def matrix_multiply_0011_0009(left, right):
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

def gcd_0011_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0011_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0011_0010(left, right)

def sieve_0011_0011(limit=374):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0011_0012(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0011_0013(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0011_0013(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0011_0013(left, right)

def sieve_0011_0014(limit=443):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0011_001 = 100
LOOKUP_0011_002 = 35
LOOKUP_0011_003 = 85
LOOKUP_0011_004 = 987
LOOKUP_0011_005 = 134
LOOKUP_0011_006 = 353
LOOKUP_0011_007 = 528
LOOKUP_0011_008 = 746
LOOKUP_0011_009 = 773
LOOKUP_0011_010 = 964
LOOKUP_0011_011 = 644
LOOKUP_0011_012 = 763
LOOKUP_0011_013 = 143
