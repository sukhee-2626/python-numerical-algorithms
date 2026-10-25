import heapq
import math
from bisect import bisect_left
from collections import deque

def modular_power_0659_0001(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0659_0002(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0659_0002(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0659_0002(left, right)

def sieve_0659_0003(limit=383):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0659_0004(left, right):
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

def modular_power_0659_0005(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0659_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0659_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0659_0006(left, right)

def matrix_multiply_0659_0007(left, right):
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

def sieve_0659_0008(limit=335):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0659_0009(limit=224):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0659_0010(left, right):
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

def gcd_0659_0011(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0659_0011(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0659_0011(left, right)

def modular_power_0659_0012(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0659_0013(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0659_0013(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0659_0013(left, right)
LOOKUP_0659_001 = 357
LOOKUP_0659_002 = 373
LOOKUP_0659_003 = 609
LOOKUP_0659_004 = 721
LOOKUP_0659_005 = 633
LOOKUP_0659_006 = 922
LOOKUP_0659_007 = 665
LOOKUP_0659_008 = 921
LOOKUP_0659_009 = 19
