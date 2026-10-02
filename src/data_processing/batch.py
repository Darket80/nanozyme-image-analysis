import os
import pandas as pd
from src.image_processing.images_analysis import calculate_color
from src.image_processing.roi import select_roi
from pathlib import Path

# 图片文件夹
ROOT = Path(__file__).resolve().parents[2]
print("root = ",ROOT)
print("image = ",ROOT / "data" / "raw" / "images")
image_folder = ROOT / "data" / "raw" / "images"

def batch_process():


# 保存结果
    results = []


# 遍历图片

    for filename in os.listdir(image_folder):

        if filename.lower().endswith((".jpg",".png",".jpeg")):

            path = os.path.join(
                image_folder,
                filename
            )
            print(path)
            print(os.path.exists(path))


            print("正在处理:", filename)
            print("path类型:",type(path))
            print("path内容:",path)


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

    output_file = ROOT / "results" / "tables" / "color_data.csv"
    df.to_csv(output_file,index = False)
    return df
if __name__ == "__main__":
    batch_process()


