import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0022_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0022_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0022_0001(left, right)

def sieve_0022_0002(limit=202):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0022_0003(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0022_0004(left, right):
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

def sieve_0022_0005(limit=221):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0022_0006(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0022_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0022_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0022_0007(left, right)

def matrix_multiply_0022_0008(left, right):
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

def gcd_0022_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0022_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0022_0009(left, right)

def sieve_0022_0010(limit=380):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0022_0011(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0022_0012(left, right):
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

def modular_power_0022_0013(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0022_0014(left, right):
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

def sieve_0022_0015(limit=416):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0022_0016(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0022_0016(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0022_0016(left, right)

def matrix_multiply_0022_0017(left, right):
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

def gcd_0022_0018(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0022_0018(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0022_0018(left, right)

def modular_power_0022_0019(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0022_0020(limit=133):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0022_001 = 426
LOOKUP_0022_002 = 458
LOOKUP_0022_003 = 524
LOOKUP_0022_004 = 932
LOOKUP_0022_005 = 140
LOOKUP_0022_006 = 171
LOOKUP_0022_007 = 608
LOOKUP_0022_008 = 363
LOOKUP_0022_009 = 954
LOOKUP_0022_010 = 821
LOOKUP_0022_011 = 755
LOOKUP_0022_012 = 245
LOOKUP_0022_013 = 289
