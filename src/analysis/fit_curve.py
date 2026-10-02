import numpy as np
from scipy.stats import linregress


def fit_linear_curve(x, y):
    """
    线性拟合
    y = ax+b
    """

    result = linregress(x, y)

    slope = result.slope
    intercept = result.intercept
    r_squared = result.rvalue**2

    return slope, intercept, r_squared