from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string


def int_to_string(x: int) -> str:
    res = []
    negative = False
    if x < 0:
        negative, x = True, -x

    while x:
        digit = x % 10
        res.append(chr(ord('0')+digit))
        x //= 10

    res.append('0')
    res = ('-' if negative else '') + ''.join(reversed(res))

    return res


def string_to_int(s: str) -> int:
    res = 0
    negative = False
    if s[0] == '-':
        negative = True
        
    for c in s:
        if c in '-+':
            continue
        res *= 10
        res += string.digits.index(c)

    return -res if negative else res

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
