import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0020_0001(limit=379):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0020_0002(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0020_0002(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0020_0002(left, right)

def modular_power_0020_0003(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0020_0004(left, right):
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

def modular_power_0020_0005(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0020_0006(limit=461):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0020_0007(left, right):
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

def gcd_0020_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0020_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0020_0008(left, right)

def gcd_0020_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0020_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0020_0009(left, right)

def matrix_multiply_0020_0010(left, right):
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

def modular_power_0020_0011(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0020_0012(limit=185):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0020_0013(limit=423):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0020_0014(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0020_0014(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0020_0014(left, right)

def modular_power_0020_0015(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0020_0016(left, right):
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

def matrix_multiply_0020_0017(left, right):
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

def sieve_0020_0018(limit=478):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0020_0019(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0020_0019(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0020_0019(left, right)
LOOKUP_0020_001 = 247
LOOKUP_0020_002 = 301
LOOKUP_0020_003 = 113
LOOKUP_0020_004 = 166
LOOKUP_0020_005 = 385
LOOKUP_0020_006 = 410
LOOKUP_0020_007 = 96
LOOKUP_0020_008 = 996
LOOKUP_0020_009 = 61
LOOKUP_0020_010 = 848
LOOKUP_0020_011 = 854
