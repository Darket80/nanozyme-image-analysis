import pandas as pd


# 读取实验条件数据
experiment = pd.read_csv(
    "../../data/processed/experiment_data.csv"
)


# 读取颜色分析数据
color = pd.read_csv(
    "../../results/tables/color_data.csv"
)


# 按图片名字合并
data = pd.merge(
    experiment,
    color,
    on="image",
    how="inner"
)


# 保存最终数据集
data.to_csv(
    "nanozyme_dataset.csv",
    index=False
)


print("数据合并完成！")
print(data)