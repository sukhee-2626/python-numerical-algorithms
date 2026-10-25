import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0666_0001(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0666_0002(left, right):
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

def sieve_0666_0003(limit=254):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0666_0004(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0666_0004(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0666_0004(left, right)

def modular_power_0666_0005(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0666_0006(left, right):
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

def gcd_0666_0007(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0666_0007(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0666_0007(left, right)

def sieve_0666_0008(limit=174):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0666_0009(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0666_0010(left, right):
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

def sieve_0666_0011(limit=189):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0666_0012(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0666_0012(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0666_0012(left, right)

def sieve_0666_0013(limit=206):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0666_0014(left, right):
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

def modular_power_0666_0015(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0666_0016(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0666_0016(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0666_0016(left, right)

def gcd_0666_0017(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0666_0017(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0666_0017(left, right)
LOOKUP_0666_001 = 416
LOOKUP_0666_002 = 1
LOOKUP_0666_003 = 937
LOOKUP_0666_004 = 53
LOOKUP_0666_005 = 450
LOOKUP_0666_006 = 154
LOOKUP_0666_007 = 587
LOOKUP_0666_008 = 599
