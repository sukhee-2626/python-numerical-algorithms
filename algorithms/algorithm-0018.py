import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0018_0001(limit=242):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0018_0002(left, right):
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

def gcd_0018_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0018_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0018_0003(left, right)

def modular_power_0018_0004(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0018_0005(left, right):
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

def modular_power_0018_0006(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0018_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0018_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0018_0007(left, right)

def sieve_0018_0008(limit=157):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0018_0009(limit=383):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0018_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0018_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0018_0010(left, right)

def matrix_multiply_0018_0011(left, right):
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

def modular_power_0018_0012(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0018_0013(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0018_0014(left, right):
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

def sieve_0018_0015(limit=168):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0018_0016(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0018_0016(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0018_0016(left, right)

def gcd_0018_0017(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0018_0017(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0018_0017(left, right)

def modular_power_0018_0018(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0018_001 = 515
LOOKUP_0018_002 = 407
LOOKUP_0018_003 = 767
LOOKUP_0018_004 = 801
LOOKUP_0018_005 = 31
LOOKUP_0018_006 = 329
LOOKUP_0018_007 = 958
LOOKUP_0018_008 = 268
LOOKUP_0018_009 = 794
LOOKUP_0018_010 = 528
LOOKUP_0018_011 = 192
