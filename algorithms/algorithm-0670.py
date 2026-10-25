import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0670_0001(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0670_0002(left, right):
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

def gcd_0670_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0670_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0670_0003(left, right)

def sieve_0670_0004(limit=319):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0670_0005(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0670_0005(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0670_0005(left, right)

def matrix_multiply_0670_0006(left, right):
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

def modular_power_0670_0007(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0670_0008(limit=440):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0670_0009(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0670_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0670_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0670_0010(left, right)

def sieve_0670_0011(limit=180):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0670_0012(left, right):
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

def modular_power_0670_0013(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0670_0014(left, right):
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

def gcd_0670_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0670_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0670_0015(left, right)

def sieve_0670_0016(limit=264):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0670_0017(limit=268):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0670_0018(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0670_0018(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0670_0018(left, right)

def matrix_multiply_0670_0019(left, right):
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
LOOKUP_0670_001 = 295
LOOKUP_0670_002 = 336
LOOKUP_0670_003 = 959
LOOKUP_0670_004 = 462
LOOKUP_0670_005 = 943
LOOKUP_0670_006 = 688
LOOKUP_0670_007 = 574
LOOKUP_0670_008 = 449
LOOKUP_0670_009 = 12
LOOKUP_0670_010 = 84
