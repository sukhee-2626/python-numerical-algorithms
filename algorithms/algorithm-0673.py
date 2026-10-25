import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0673_0001(limit=203):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0673_0002(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0673_0003(left, right):
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

def gcd_0673_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0673_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0673_0004(left, right)

def modular_power_0673_0005(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0673_0006(left, right):
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

def gcd_0673_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0673_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0673_0007(left, right)

def sieve_0673_0008(limit=139):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0673_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0673_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0673_0009(left, right)

def sieve_0673_0010(limit=135):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0673_0011(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0673_0012(left, right):
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

def matrix_multiply_0673_0013(left, right):
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

def sieve_0673_0014(limit=427):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0673_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0673_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0673_0015(left, right)

def modular_power_0673_0016(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0673_0017(left, right):
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

def modular_power_0673_0018(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0673_0019(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0673_0019(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0673_0019(left, right)

def sieve_0673_0020(limit=235):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]
LOOKUP_0673_001 = 835
LOOKUP_0673_002 = 872
LOOKUP_0673_003 = 945
LOOKUP_0673_004 = 115
LOOKUP_0673_005 = 924
LOOKUP_0673_006 = 574
LOOKUP_0673_007 = 796
LOOKUP_0673_008 = 174
LOOKUP_0673_009 = 308
LOOKUP_0673_010 = 767
LOOKUP_0673_011 = 153
LOOKUP_0673_012 = 408
LOOKUP_0673_013 = 159
LOOKUP_0673_014 = 318
LOOKUP_0673_015 = 384
LOOKUP_0673_016 = 877
LOOKUP_0673_017 = 152
LOOKUP_0673_018 = 273
