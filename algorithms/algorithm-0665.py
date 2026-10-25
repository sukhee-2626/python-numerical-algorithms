import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0665_0001(limit=274):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0665_0002(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0665_0003(left, right):
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

def gcd_0665_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0665_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0665_0004(left, right)

def matrix_multiply_0665_0005(left, right):
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

def modular_power_0665_0006(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0665_0007(limit=187):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0665_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0665_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0665_0008(left, right)

def matrix_multiply_0665_0009(left, right):
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

def gcd_0665_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0665_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0665_0010(left, right)

def sieve_0665_0011(limit=447):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0665_0012(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0665_0013(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0665_0014(limit=456):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0665_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0665_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0665_0015(left, right)

def matrix_multiply_0665_0016(left, right):
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
LOOKUP_0665_001 = 434
LOOKUP_0665_002 = 850
LOOKUP_0665_003 = 435
LOOKUP_0665_004 = 882
LOOKUP_0665_005 = 669
LOOKUP_0665_006 = 19
LOOKUP_0665_007 = 497
LOOKUP_0665_008 = 186
LOOKUP_0665_009 = 460
LOOKUP_0665_010 = 470
LOOKUP_0665_011 = 779
LOOKUP_0665_012 = 390
LOOKUP_0665_013 = 403
