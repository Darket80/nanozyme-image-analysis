import cv2

def select_roi(image_path):

    img = cv2.imread(image_path)

    roi = cv2.selectROI(
        "select ROI",
        img
    )

    x,y,w,h = roi

    crop = img[y:y+h, x:x+w]

    cv2.destroyAllWindows()

    return crop