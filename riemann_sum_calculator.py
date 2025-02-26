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
from math import cos, sin, tan, pi, e, exp
from math import log as ln

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
    elif mode == "trapezoid":
        for n in range(1, N+1):
            a = f(x_1 + (n-1)*delta_x) 
            b = f(x_1 + n*delta_x)
            area = ((a+b)/2) * delta_x
            total_area += area
    elif mode == "simpson":
        assert N % 2 == 0, "n must be even"
        for n in range(0, N+1): 
            f_x_i = f(x_1 + n * delta_x)
            if n == 0 or n == N:
                area = (delta_x/3) * f_x_i
                total_area += area
            elif (n-1) % 2 == 0:
                area = (4 * delta_x / 3) * f_x_i
                total_area += area
            else:
                area = (2 * delta_x / 3) * f_x_i
                total_area += area

    return total_area

def main():
    f = lambda x: 13 * cos(x**2)
    n = 4
    lower_bound = 0
    upper_bound = 1

    real = calc_sum(
        f=f,
        x_1=lower_bound,
        x_2=upper_bound,
        N=10000,
        mode="endpoints",
        endpoints="middle"
    )

    print("trapezoidal")
    T_n = calc_sum(
        f=f,
        x_1=lower_bound,
        x_2=upper_bound,
        N=n,
        mode="trapezoid",
    )
    E_T = real - T_n
    print(T_n)
    print("Error:", E_T)
    
    print("midpoint")
    M_n = calc_sum(
        f=f,
        x_1=lower_bound,
        x_2=upper_bound,
        N=n,
        mode="endpoints",
        endpoints="middle",
    )
    E_M = real - M_n
    print(M_n)
    print("Error:", E_M)

    print("simpson")
    S_n = calc_sum(
        f=f,
        x_1=lower_bound,
        x_2=upper_bound,
        N=n,
        mode="simpson",
    )
    E_S = real - S_n
    print(S_n)
    print("Error:", E_S)


if __name__ == "__main__":
    main()