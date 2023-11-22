import numpy as np
import matplotlib.pyplot as plt


def sum_of_squares(V):
    """Computes the sum of squared elements in v"""
    return np.dot(V, V)


def _f(x):
    return x ** 2


def difference_quotient(f, x):
    h = 0.0000000001
    return (f(x + h) - f(x)) / h


# x = 5
# print(difference_quotient(_f, x))


def partial_difference_quotient(f, v, i):
    h = 0.0000000001
    w = [v_j + (h if j == i else 0) for j, v_j in enumerate(v)]
    return (f(w) - f(v)) / h


def estimate_gradient(f, v, h=0.0001):
    return [partial_difference_quotient(f, v, i)
            for i in range(len(v))]

# _v = [1, 2, 3]
# print(estimate_gradient(sum_of_squares, _v))

# show graph:
# xs = range(-10, 11)
# actuals = [sum_of_squares(x) for x in xs]
# estimates = [difference_quotient(sum_of_squares,x) for x in xs]
# plt.title("gradiant")
# plt.plot(xs, actuals, 'rx', label='Actual')  # red x
# plt.plot(xs, estimates, 'b+', label='Estimate') # blue +
# plt.legend(loc=9)
# plt.show()
