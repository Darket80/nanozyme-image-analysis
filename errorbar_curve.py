import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os


# =====================
# 读取数据
# =====================

data = pd.read_csv(
    "results/nanozyme_dataset.csv"
)


# 按浓度统计
group = data.groupby("concentration")["Abs652"]

mean = group.mean()


x = mean.index.values
y = mean.values


# =====================
# 线性拟合
# =====================

result = linregress(x, y)


slope = result.slope
intercept = result.intercept
r2 = result.rvalue**2


print("===================")
print("Linear fitting")
print("===================")

print(
    f"Slope = {slope:.5f}"
)

print(
    f"Intercept = {intercept:.5f}"
)

print(
    f"R² = {r2:.5f}"
)


print(
    f"Equation: y = {slope:.5f}x + {intercept:.5f}"
)



# =====================
# 输出活性比较表
# =====================

activity = pd.DataFrame({

    "concentration":x,

    "Abs652_mean":y

})


activity["activity_slope"] = slope

activity["R2"] = r2


os.makedirs(
    "results",
    exist_ok=True
)


activity.to_csv(
    "results/activity_comparison.csv",
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
    slope*x+intercept,
    label="Linear fit"
)


plt.xlabel(
    "CuMnZnS concentration (μg/mL)"
)


plt.ylabel(
    "Abs652"
)


plt.title(
    "CuMnZnS nanozyme activity"
)



# 显示方程

text = (
    f"y={slope:.4f}x+{intercept:.4f}\n"
    f"R²={r2:.4f}"
)


plt.text(
    0.05,
    0.9,
    text,
    transform=plt.gca().transAxes
)



plt.legend()

plt.grid()


plt.savefig(
    "results/activity_fit_curve.png",
    dpi=300,
    bbox_inches="tight"
)


plt.show()