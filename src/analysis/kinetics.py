import numpy as np
from scipy.stats import linregress


def calculate_initial_rate(time, absorbance, n_points=5):
    """
    计算反应初始速率

    参数
    ----------
    time : array-like
        时间，例如 [0, 10, 20, 30, 40]

    absorbance : array-like
        对应时间的吸光度，例如 Abs652

    n_points : int
        用前多少个数据点进行线性拟合

    返回
    ----------
    slope : float
        初始反应速率，单位为 Abs/s

    r2 : float
        线性拟合 R²

    intercept : float
        截距
    """

    time = np.asarray(time)
    absorbance = np.asarray(absorbance)

    # 取反应初始阶段的数据
    time_initial = time[:n_points]
    absorbance_initial = absorbance[:n_points]

    # 线性拟合
    result = linregress(
        time_initial,
        absorbance_initial
    )

    slope = result.slope
    intercept = result.intercept
    r2 = result.rvalue ** 2

    return slope, r2, intercept
if __name__ == "__main__":

    # 模拟数据
    data = {
        10: {
            1: [0.100, 0.119, 0.135, 0.155, 0.172],
            2: [0.102, 0.119, 0.138, 0.156, 0.175],
            3: [0.098, 0.117, 0.135, 0.151, 0.171],
        },

        50: {
            1: [0.100, 0.141, 0.184, 0.225, 0.270],
            2: [0.102, 0.145, 0.185, 0.229, 0.269],
            3: [0.098, 0.139, 0.183, 0.226, 0.266],
        },

        100: {
            1: [0.100, 0.166, 0.229, 0.297, 0.361],
            2: [0.102, 0.166, 0.233, 0.297, 0.364],
            3: [0.098, 0.165, 0.228, 0.293, 0.359],
        }
    }

    time = [0, 10, 20, 30, 40]

    print("==============================")
    print("Kinetics analysis")
    print("==============================")

    for concentration in data:

        for replicate in data[concentration]:

            absorbance = data[concentration][replicate]

            slope, r2, intercept = calculate_initial_rate(
                time,
                absorbance
            )

            print(
                f"Concentration = {concentration} μg/mL | "
                f"Replicate = {replicate} | "
                f"Rate = {slope:.6f} Abs/s | "
                f"R² = {r2:.6f}"
            )