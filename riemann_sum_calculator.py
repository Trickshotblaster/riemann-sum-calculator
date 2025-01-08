import numpy as np
import math
from math import cos, sin, tan, pi

def f(x):
    return 1 + cos(x/2)

def calc_area(l, w):
    return l * w

# todo: gradient descent
def get_min(func, x_min, x_max, precision = 1e-6):
    return min(func(x) for x in np.arange(x_min, x_max, precision))

def get_max(func, x_min, x_max, precision = 1e-6):
    return max(func(x) for x in np.arange(x_min, x_max, precision))

def calc_sum(f, x_1, x_2, N, mode="lower", endpoints="none"):
    assert x_2 > x_1, "x2 must be greater than x1"
    delta_x = (x_2 - x_1) / N
    total_area = 0.0
    if mode == "lower":
        for n in range(1, N+1):
            min_value_on_range = get_min(f, x_1 + (n-1)*delta_x, x_1 + n*delta_x)
            area = calc_area(delta_x, min_value_on_range)
            total_area += area
    elif mode == "upper":
        for n in range(1, N+1):
            max_value_on_range = get_max(f, x_1 + (n-1)*delta_x, x_1 + n*delta_x)
            area = calc_area(delta_x, max_value_on_range)
            total_area += area
    elif mode == "endpoints":
        if endpoints == "left":
            for n in range(1, N+1):
                value_for_range = f(x_1 + (n-1)*delta_x)
                area = calc_area(delta_x, value_for_range)
                total_area += area
        elif endpoints == "right":
            for n in range(1, N+1):
                value_for_range = f(x_1 + (n)*delta_x)
                area = calc_area(delta_x, value_for_range)
                total_area += area
        elif endpoints == "middle":
            for n in range(1, N+1):
                value_for_range = f(x_1 + ((n-1)*delta_x) + delta_x/2)
                area = calc_area(delta_x, value_for_range)
                total_area += area
    return total_area

print(calc_sum(
    f=f,
    x_1=-pi,
    x_2=pi,
    N=3,
    mode="upper",
    endpoints="none"
))