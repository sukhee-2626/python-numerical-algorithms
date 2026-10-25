import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0664_0001(limit=142):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0664_0002(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0664_0003(left, right):
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

def gcd_0664_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0664_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0664_0004(left, right)

def matrix_multiply_0664_0005(left, right):
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

def modular_power_0664_0006(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0664_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0664_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0664_0007(left, right)

def sieve_0664_0008(limit=321):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0664_0009(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0664_0010(left, right):
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

def gcd_0664_0011(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0664_0011(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0664_0011(left, right)

def sieve_0664_0012(limit=196):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0664_0013(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0664_0014(left, right):
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

def gcd_0664_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0664_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0664_0015(left, right)
LOOKUP_0664_001 = 990
LOOKUP_0664_002 = 608
LOOKUP_0664_003 = 31
LOOKUP_0664_004 = 207
LOOKUP_0664_005 = 946
LOOKUP_0664_006 = 400
LOOKUP_0664_007 = 921
LOOKUP_0664_008 = 512
LOOKUP_0664_009 = 214
LOOKUP_0664_010 = 387
LOOKUP_0664_011 = 853
LOOKUP_0664_012 = 918
LOOKUP_0664_013 = 464
LOOKUP_0664_014 = 214
LOOKUP_0664_015 = 306
LOOKUP_0664_016 = 713
