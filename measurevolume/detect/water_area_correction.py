import cv2
import numpy as np


def water_area_correction(img: np.ndarray) -> np.ndarray:
    img = img.astype(np.uint8)
    contours = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    max_cnt = max(contours, key=lambda x: cv2.contourArea(x))

    out = np.zeros_like(img)
    cv2.drawContours(out, [max_cnt], -1, color=1, thickness=-1)

    return out
