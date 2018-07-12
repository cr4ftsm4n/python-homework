from math import ceil, sqrt
from itertools import zip_longest
import sys


def encode(msg):
    msg = _cleanse(msg)
    square_size = int(ceil(sqrt(len(msg))))
    square = _chunks_of(msg, square_size)
    return ' '.join([''.join(col)
                     for col in zip_longest(*square, fillvalue=' ')])


def _cleanse(s):
    return ''.join([c for c in s if c.isalnum()]).lower()


def _chunks_of(s, n):
    if len(s) <= n:
        return [s]
    return [s[:n]] + _chunks_of(s[n:], n)
