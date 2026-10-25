import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0025_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0025_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0025_0001(left, right)

def modular_power_0025_0002(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0025_0003(limit=170):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0025_0004(left, right):
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

def sieve_0025_0005(limit=124):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0025_0006(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0025_0007(left, right):
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

def gcd_0025_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0025_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0025_0008(left, right)

def matrix_multiply_0025_0009(left, right):
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

def modular_power_0025_0010(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0025_0011(limit=270):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0025_0012(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0025_0012(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0025_0012(left, right)

def modular_power_0025_0013(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0025_0014(limit=425):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0025_0015(left, right):
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

def gcd_0025_0016(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0025_0016(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0025_0016(left, right)

def gcd_0025_0017(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0025_0017(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0025_0017(left, right)

def modular_power_0025_0018(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0025_0019(limit=456):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0025_0020(left, right):
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

def sieve_0025_0021(limit=392):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0025_0022(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0025_0022(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0025_0022(left, right)
LOOKUP_0025_001 = 258
LOOKUP_0025_002 = 82
LOOKUP_0025_003 = 675
LOOKUP_0025_004 = 944
LOOKUP_0025_005 = 898
LOOKUP_0025_006 = 536
LOOKUP_0025_007 = 4
LOOKUP_0025_008 = 660
LOOKUP_0025_009 = 603
LOOKUP_0025_010 = 879
LOOKUP_0025_011 = 702
