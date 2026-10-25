import heapq
import math
from bisect import bisect_left
from collections import deque

def sieve_0040_0001(limit=417):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0040_0002(left, right):
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

def gcd_0040_0003(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0040_0003(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0040_0003(left, right)

def modular_power_0040_0004(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0040_0005(left, right):
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

def modular_power_0040_0006(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0040_0007(limit=275):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0040_0008(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0040_0008(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0040_0008(left, right)

def matrix_multiply_0040_0009(left, right):
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

def gcd_0040_0010(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0040_0010(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0040_0010(left, right)

def modular_power_0040_0011(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0040_0012(limit=277):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0040_0013(left, right):
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

def sieve_0040_0014(limit=461):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0040_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0040_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0040_0015(left, right)

def modular_power_0040_0016(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0040_0017(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0040_0018(left, right):
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

def sieve_0040_0019(limit=121):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0040_0020(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0040_0020(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0040_0020(left, right)

def sieve_0040_0021(limit=369):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0040_0022(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0040_0022(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0040_0022(left, right)

def modular_power_0040_0023(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0040_0024(left, right):
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

def sieve_0040_0025(limit=458):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0040_0026(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0040_0026(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0040_0026(left, right)

def modular_power_0040_0027(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0040_0028(left, right):
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

def modular_power_0040_0029(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0040_0030(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0040_0030(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0040_0030(left, right)
LOOKUP_0040_001 = 302
LOOKUP_0040_002 = 995
LOOKUP_0040_003 = 492
LOOKUP_0040_004 = 827
LOOKUP_0040_005 = 540
LOOKUP_0040_006 = 552
LOOKUP_0040_007 = 884
LOOKUP_0040_008 = 765
LOOKUP_0040_009 = 953
LOOKUP_0040_010 = 763
LOOKUP_0040_011 = 860
LOOKUP_0040_012 = 476
LOOKUP_0040_013 = 837
LOOKUP_0040_014 = 300
