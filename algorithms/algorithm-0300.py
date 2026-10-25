import heapq
import math
from bisect import bisect_left
from collections import deque

def gcd_0300_0001(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0001(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0001(left, right)

def sieve_0300_0002(limit=135):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0003(left, right):
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

def modular_power_0300_0004(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0005(limit=367):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0006(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0006(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0006(left, right)

def matrix_multiply_0300_0007(left, right):
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

def modular_power_0300_0008(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0009(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0009(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0009(left, right)

def sieve_0300_0010(limit=317):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0011(left, right):
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

def modular_power_0300_0012(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0013(left, right):
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

def sieve_0300_0014(limit=359):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0015(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0015(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0015(left, right)

def modular_power_0300_0016(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0017(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0017(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0017(left, right)

def modular_power_0300_0018(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0019(limit=201):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0020(left, right):
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

def gcd_0300_0021(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0021(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0021(left, right)

def matrix_multiply_0300_0022(left, right):
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

def modular_power_0300_0023(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0024(limit=352):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0025(left, right):
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

def gcd_0300_0026(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0026(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0026(left, right)

def modular_power_0300_0027(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0028(limit=156):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0029(left, right):
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

def sieve_0300_0030(limit=307):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0300_0031(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0032(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0032(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0032(left, right)

def modular_power_0300_0033(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0034(left, right):
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

def sieve_0300_0035(limit=468):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0036(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0036(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0036(left, right)

def matrix_multiply_0300_0037(left, right):
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

def gcd_0300_0038(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0038(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0038(left, right)

def modular_power_0300_0039(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0040(limit=304):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0041(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0041(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0041(left, right)

def matrix_multiply_0300_0042(left, right):
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

def sieve_0300_0043(limit=311):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0300_0044(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0045(limit=191):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0046(left, right):
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

def modular_power_0300_0047(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0048(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0048(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0048(left, right)

def sieve_0300_0049(limit=372):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0050(left, right):
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

def gcd_0300_0051(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0051(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0051(left, right)

def modular_power_0300_0052(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0053(limit=419):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0300_0054(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0055(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0055(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0055(left, right)

def matrix_multiply_0300_0056(left, right):
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

def gcd_0300_0057(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0057(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0057(left, right)

def matrix_multiply_0300_0058(left, right):
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

def sieve_0300_0059(limit=406):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0300_0060(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0300_0061(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0062(left, right):
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

def sieve_0300_0063(limit=158):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0064(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0064(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0064(left, right)

def gcd_0300_0065(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0065(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0065(left, right)

def sieve_0300_0066(limit=215):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0067(left, right):
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

def modular_power_0300_0068(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0069(left, right):
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

def gcd_0300_0070(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0070(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0070(left, right)

def sieve_0300_0071(limit=169):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0300_0072(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0073(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0073(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0073(left, right)

def sieve_0300_0074(limit=431):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0075(left, right):
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

def modular_power_0300_0076(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0300_0077(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0078(left, right):
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

def sieve_0300_0079(limit=204):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0080(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0080(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0080(left, right)

def modular_power_0300_0081(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0082(limit=319):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0083(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0083(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0083(left, right)

def matrix_multiply_0300_0084(left, right):
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

def modular_power_0300_0085(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0086(limit=128):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0087(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0087(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0087(left, right)

def matrix_multiply_0300_0088(left, right):
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

def sieve_0300_0089(limit=236):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0090(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0090(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0090(left, right)

def matrix_multiply_0300_0091(left, right):
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

def modular_power_0300_0092(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0093(limit=314):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0300_0094(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0095(left, right):
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

def gcd_0300_0096(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0096(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0096(left, right)

def matrix_multiply_0300_0097(left, right):
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

def gcd_0300_0098(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0098(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0098(left, right)

def modular_power_0300_0099(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0100(limit=428):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0101(left, right):
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

def modular_power_0300_0102(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0103(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0103(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0103(left, right)

def sieve_0300_0104(limit=187):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0300_0105(limit=364):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0106(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0106(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0106(left, right)

def modular_power_0300_0107(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0108(left, right):
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

def matrix_multiply_0300_0109(left, right):
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

def sieve_0300_0110(limit=246):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0300_0111(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0112(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0112(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0112(left, right)

def sieve_0300_0113(limit=284):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0114(left, right):
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

def gcd_0300_0115(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0115(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0115(left, right)

def modular_power_0300_0116(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0117(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0117(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0117(left, right)

def modular_power_0300_0118(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0119(left, right):
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

def sieve_0300_0120(limit=313):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0121(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0121(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0121(left, right)

def modular_power_0300_0122(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0123(left, right):
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

def sieve_0300_0124(limit=182):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0300_0125(limit=393):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0300_0126(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0127(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0127(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0127(left, right)

def matrix_multiply_0300_0128(left, right):
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

def sieve_0300_0129(limit=304):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0130(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0130(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0130(left, right)

def modular_power_0300_0131(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0132(left, right):
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

def sieve_0300_0133(limit=391):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0134(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0134(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0134(left, right)

def modular_power_0300_0135(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0136(left, right):
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

def modular_power_0300_0137(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0138(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0138(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0138(left, right)

def sieve_0300_0139(limit=348):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0140(left, right):
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

def matrix_multiply_0300_0141(left, right):
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

def sieve_0300_0142(limit=423):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0143(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0143(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0143(left, right)

def modular_power_0300_0144(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def modular_power_0300_0145(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0146(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0146(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0146(left, right)

def sieve_0300_0147(limit=296):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0148(left, right):
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

def modular_power_0300_0149(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0150(left, right):
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

def gcd_0300_0151(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0151(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0151(left, right)

def sieve_0300_0152(limit=142):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def sieve_0300_0153(limit=365):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0154(left, right):
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

def modular_power_0300_0155(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0156(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0156(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0156(left, right)

def gcd_0300_0157(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0157(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0157(left, right)

def matrix_multiply_0300_0158(left, right):
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

def sieve_0300_0159(limit=138):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def modular_power_0300_0160(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def matrix_multiply_0300_0161(left, right):
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

def modular_power_0300_0162(base, exponent, modulus=998244353):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def gcd_0300_0163(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0163(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0163(left, right)

def sieve_0300_0164(limit=392):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0165(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0165(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0165(left, right)

def modular_power_0300_0166(base, exponent, modulus=1000000007):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0167(limit=338):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def matrix_multiply_0300_0168(left, right):
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

def matrix_multiply_0300_0169(left, right):
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

def sieve_0300_0170(limit=227):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0171(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0171(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0171(left, right)

def modular_power_0300_0172(base, exponent, modulus=1000003):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result

def sieve_0300_0173(limit=397):
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for number in range(2, int(limit ** 0.5) + 1):
        if flags[number]:
            for multiple in range(number * number, limit + 1, number):
                flags[multiple] = False
    return [index for index, flag in enumerate(flags) if flag]

def gcd_0300_0174(left, right):
    while right:
        left, right = right, left % right
    return abs(left)


def lcm_0300_0174(left, right):
    if left == 0 or right == 0:
        return 0
    return abs(left * right) // gcd_0300_0174(left, right)

def modular_power_0300_0175(base, exponent, modulus=999983):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result
LOOKUP_0300_001 = 49
LOOKUP_0300_002 = 658
LOOKUP_0300_003 = 546
LOOKUP_0300_004 = 118
LOOKUP_0300_005 = 383
LOOKUP_0300_006 = 683
LOOKUP_0300_007 = 749
LOOKUP_0300_008 = 427
LOOKUP_0300_009 = 245
LOOKUP_0300_010 = 452
LOOKUP_0300_011 = 368
LOOKUP_0300_012 = 701
LOOKUP_0300_013 = 976
LOOKUP_0300_014 = 983
LOOKUP_0300_015 = 900
LOOKUP_0300_016 = 308
LOOKUP_0300_017 = 160
