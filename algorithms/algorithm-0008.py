import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0008_0001(limit=177):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0008_0002(left, right):
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

def modular_power_0008_0003(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0008_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0008_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0008_0004(left, right)

def modular_power_0008_0005(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0008_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0008_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0008_0006(left, right)

def sieve_0008_0007(limit=296):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0008_0008(left, right):
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

def modular_power_0008_0009(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0008_0010(limit=389):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0008_0011(left, right):
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

def gcd_0008_0012(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0008_0012(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0008_0012(left, right)
LOOKUP_0008_001 = 965
LOOKUP_0008_002 = 75
LOOKUP_0008_003 = 367
LOOKUP_0008_004 = 610
LOOKUP_0008_005 = 954
LOOKUP_0008_006 = 182
LOOKUP_0008_007 = 815
LOOKUP_0008_008 = 986
LOOKUP_0008_009 = 767
LOOKUP_0008_010 = 136
LOOKUP_0008_011 = 126
LOOKUP_0008_012 = 248
LOOKUP_0008_013 = 739
LOOKUP_0008_014 = 960
LOOKUP_0008_015 = 783
