import sys

seq = sys.argv[1]

import math

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

def sort(a,b):
    if a > b:
        return a, b
    return b, a

def getMaximumMatches(seq):
    a_count = 0
    u_count = 0
    g_count = 0
    c_count = 0
    for i, c in enumerate(seq):
        if c =='A':
            a_count = a_count + 1
        elif c =='U':
            u_count = u_count + 1
        elif c =='G':
            g_count = g_count + 1
        else:
            c_count = c_count + 1
    return nCr(*sort(a_count, u_count)) * nCr(*sort(g_count, c_count))

print(getMaximumMatches(seq))
