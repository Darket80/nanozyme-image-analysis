import cv2
import numpy as np


def calculate_color(crop):

    rgb=cv2.cvtColor(
        crop,
        cv2.COLOR_BGR2RGB
    )

    hsv=cv2.cvtColor(
        crop,
        cv2.COLOR_BGR2HSV
    )


    mean_rgb=np.mean(
        rgb,
        axis=(0,1)
    )

    mean_hsv=np.mean(
        hsv,
        axis=(0,1)
    )


    return mean_rgb, mean_hsv