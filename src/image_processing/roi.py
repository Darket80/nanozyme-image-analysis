import cv2
import numpy as np
def select_roi(image_path):

    image_path = str(image_path)

    img_array = np.fromfile(image_path, dtype=np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if img is None:
        raise FileNotFoundError(
            f"图片读取失败，请检查路径: {image_path}"
        )

    roi = cv2.selectROI(
        "select ROI",
        img
    )

    x,y,w,h = roi

    crop = img[y:y+h, x:x+w]

    cv2.destroyAllWindows()

    return crop