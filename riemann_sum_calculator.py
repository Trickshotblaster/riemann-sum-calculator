"""
Riemann Sum Calculator
Estimates the area under a curver using Riemann Sums numerically
Requirements: numpy (pip install numpy), although could be modified do be done without

Use:
Replace f(x) with any one-variable function, making sure to return the value
Then, use calc_sum to find the Riemann sum for the function on the interval
with N subdivisions
Be careful when changing precision, it can help but is terribly implemented and
a 10x in precision will result in 10x memory footprint (just buy 128TB ram bro)
Have fun!
"""

import numpy as np
import math
from math import cos, sin, tan, pi

def f(x):
    """Replace this with your function, remember x^2 is written as x**2 in python"""
    return 1 + cos(x/2)

def calc_area(l, w):
    """Most useful function ever created"""
    return l * w

# todo: gradient descent maybe
def get_min(func, x_min, x_max, precision=1e-6):
    """Call f(x) on a bunch of x between x_min and x_max
    spaced apart by precision, return min"""
    return min(func(x) for x in np.arange(x_min, x_max, precision))

def get_max(func, x_min, x_max, precision=1e-6):
    """Call f(x) on a bunch of x between x_min and x_max,
    spaced apart by precision, return max"""
    return max(func(x) for x in np.arange(x_min, x_max, precision))

def calc_sum(f, x_1, x_2, N, mode="lower", endpoints="none", precision=1e-6):
    """Calculate Riemann sum for f, using x_1 as start of interval,
    x_2 for end of interval, N as num subdivisions,
    mode chosen between upper, lower, and endpoints,
    which endpoints to use if using endpoints (left/right/middle),
    and precision for finding min/max if upper/lower mode chosen"""

    # make sure the inteval is right
    assert x_2 > x_1, "x2 must be greater than x1"
    # find the x-size of rectangles and intialize area
    delta_x = (x_2 - x_1) / N
    total_area = 0.0
    # check for mode
    if mode == "lower":
        for n in range(1, N+1):
            # for each subdivision n, get the min value of f (the height of our rectangle)
            # then calculate the area using delta_x as a base and add to total area
            min_value_on_range = get_min(f, x_1 + (n-1)*delta_x, x_1 + n*delta_x, precision=precision)
            area = calc_area(delta_x, min_value_on_range)
            total_area += area
    elif mode == "upper":
        for n in range(1, N+1):
            # again, for each subdivsion N, get the max value of f as the height, delta_x width
            # and calc area
            max_value_on_range = get_max(f, x_1 + (n-1)*delta_x, x_1 + n*delta_x, precision=precision)
            area = calc_area(delta_x, max_value_on_range)
            total_area += area
    elif mode == "endpoints":
        if endpoints == "left":
            for n in range(1, N+1):
                # just get f(x_(n-1)) for height
                value_for_range = f(x_1 + (n-1)*delta_x)
                area = calc_area(delta_x, value_for_range)
                total_area += area
        elif endpoints == "right":
            for n in range(1, N+1):
                # f(x_n) for height
                value_for_range = f(x_1 + (n)*delta_x)
                area = calc_area(delta_x, value_for_range)
                total_area += area
        elif endpoints == "middle":
            for n in range(1, N+1):
                # calculate the middle by adding delta_x/2
                value_for_range = f(x_1 + ((n-1)*delta_x) + delta_x/2)
                area = calc_area(delta_x, value_for_range)
                total_area += area
    return total_area

def main():
    print(calc_sum(
        f=f,
        x_1=-5,
        x_2=5,
        N=3,
        mode="lower",
        endpoints="none",
        precision=1e-6
    ))

if __name__ == "__main__":
    main()