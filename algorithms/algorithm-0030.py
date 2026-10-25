import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0030_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0030_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0030_0001(left, right)

def modular_power_0030_0002(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0030_0003(limit=182):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0030_0004(left, right):
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

def sieve_0030_0005(limit=137):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0030_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0030_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0030_0006(left, right)

def matrix_multiply_0030_0007(left, right):
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

def modular_power_0030_0008(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0030_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0030_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0030_0009(left, right)

def sieve_0030_0010(limit=214):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0030_0011(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0030_0012(left, right):
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

def matrix_multiply_0030_0013(left, right):
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

def sieve_0030_0014(limit=223):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0030_0015(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0030_0016(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0030_0016(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0030_0016(left, right)

def modular_power_0030_0017(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0030_0018(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0030_0018(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0030_0018(left, right)

def matrix_multiply_0030_0019(left, right):
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

def sieve_0030_0020(limit=423):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0030_0021(limit=373):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0030_0022(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0030_0022(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0030_0022(left, right)

def modular_power_0030_0023(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0030_0024(left, right):
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
LOOKUP_0030_001 = 149
LOOKUP_0030_002 = 576
LOOKUP_0030_003 = 165
LOOKUP_0030_004 = 127
LOOKUP_0030_005 = 942
LOOKUP_0030_006 = 277
LOOKUP_0030_007 = 779
LOOKUP_0030_008 = 742
LOOKUP_0030_009 = 846
LOOKUP_0030_010 = 462
LOOKUP_0030_011 = 654
LOOKUP_0030_012 = 544
LOOKUP_0030_013 = 284
LOOKUP_0030_014 = 404
LOOKUP_0030_015 = 619
LOOKUP_0030_016 = 553
LOOKUP_0030_017 = 210
LOOKUP_0030_018 = 449
