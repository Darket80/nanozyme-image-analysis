import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
data = pd.read_csv(
    "../results/nanozyme_dataset.csv"
)


# 查看数据
print(data)


# 浓度
x = data["concentration"]


# 吸光度
y = data["Abs652"]


# 绘图
plt.figure(figsize=(6,4))

plt.plot(
    x,
    y,
    marker="o"
)


plt.xlabel("CuMnZnS concentration")
plt.ylabel("Abs652")

plt.title(
    "CuMnZnS nanozyme activity response"
)


plt.grid(True)

plt.savefig(
    "results/concentration_abs652.png",
    dpi=300
)


plt.show()


print("曲线生成完成")