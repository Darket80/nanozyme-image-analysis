import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score


# =====================
# 读取数据
# =====================

data = pd.read_csv(
    "../results/nanozyme_dataset.csv"
)


x = data["concentration"]
y = data["Abs652"]


# =====================
# 线性拟合
# =====================

coef = np.polyfit(x, y, 1)

a = coef[0]
b = coef[1]


y_fit = a*x + b


# R²
r2 = r2_score(
    y,
    y_fit
)


# =====================
# 输出结果
# =====================

print("----------------")
print("Linear fitting")
print("----------------")

print(
    f"y = {a:.5f}x + {b:.5f}"
)

print(
    f"R² = {r2:.5f}"
)


# 保存拟合参数

fit_result = pd.DataFrame({

    "slope_a":[a],

    "intercept_b":[b],

    "R2":[r2]

})


fit_result.to_csv(
    "results/fit_result.csv",
    index=False
)


# =====================
# 绘图
# =====================

plt.figure(
    figsize=(6,4)
)


plt.scatter(
    x,
    y,
    label="Experimental"
)


plt.plot(
    x,
    y_fit,
    label="Linear fit"
)


# 添加公式文字

text = (
    f"y = {a:.4f}x + {b:.4f}\n"
    f"R² = {r2:.4f}"
)


plt.text(
    0.05,
    0.90,
    text,
    transform=plt.gca().transAxes
)


plt.xlabel(
    "CuMnZnS concentration (μg/mL)"
)


plt.ylabel(
    "Abs652"
)


plt.title(
    "CuMnZnS nanozyme activity curve"
)


plt.legend()


plt.grid()


plt.savefig(
    "results/activity_curve_fit.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()