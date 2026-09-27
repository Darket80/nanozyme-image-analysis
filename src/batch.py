import os
import pandas as pd
from images_analysis import calculate_color
from roi import select_roi


# 图片文件夹
image_folder = "images"


# 保存结果
results = []


# 遍历图片

for filename in os.listdir(image_folder):

    if filename.endswith(".jpg"):

        path = os.path.join(
            image_folder,
            filename
        )


        print("正在处理:", filename)


        crop = select_roi(path)
        mean_rgb , mean_hsv= calculate_color(crop)


        results.append({

            "image": filename,

            "R": mean_rgb[0],
            "G": mean_rgb[1],
            "B": mean_rgb[2],

            "H": mean_hsv[0],
            "S": mean_hsv[1],
            "V": mean_hsv[2]

        })


# 转DataFrame

df = pd.DataFrame(results)


# 保存CSV

df.to_csv(
    "results/color_data.csv",
    index=False
)


print("全部图片分析完成")