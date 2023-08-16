# Solution I found that works much better than mine.  Need to study
# probability and linear algebra before I can understand it.

import numpy as np


def get_active_and_terminals(m):
    a, t = [], []
    for n, r in enumerate(m):
        (a if sum(r) else t).append(n)
    return (a, t)


def get_list(b):
    b = b.round().astype(int).A1
    gcd = np.gcd.reduce(b)
    b = np.append(b, b.sum())
    return (b/gcd).astype(int)


def solution(m):
    a, t = get_active_and_terminals(m)
    if 0 in t:
        return [1] + [0]*len(t[1:]) + [1]
    m = np.matrix(m, dtype=float)[a, :]
    d = np.prod(m.sum(1))
    p = m/m.sum(1)
    q, r = p[:, a], p[:, t]
    i = np.identity(len(q))
    n = (i - q)**(-1)
    b = n[0]*r*d/np.linalg.det(n)
    return list(get_list(b))
