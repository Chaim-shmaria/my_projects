import numpy as np


def f(x):
    return x ** 2


def difference_quotient(f, x):
    h = 0.0000000001
    return (f(x + h) - f(x)) / h


# x = 5
# print(difference_quotient(f, x))


def partial_difference_quotient(f, v, i, h):
    w = [v_j + (h if j == i else 0)
         for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.0001):
    return [partial_difference_quotient(f, v, i, h)
            for i in range(len(v))]


a = [1, 2, 3]
print(f(a))
