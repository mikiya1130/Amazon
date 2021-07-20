from django.conf import settings

import os
import numpy as np
import cv2

from ..exceptions import NotFoundChopsticksError


def get_chopsticks_length_per_pixel(img: np.ndarray) -> float:
    """割り箸を基準にmm/pixelを計算し、返す

    Args:
        img (np.ndarray): 元画像

    Returns:
        float: 画像の1pixel辺りの大きさ(単位:mm)

    Raises:
        NotFoundChopsticksError: 割り箸が検出できなかった場合に送出
    """
    mask = generating_mask(img)
    if len(mask) < 5:
        raise NotFoundChopsticksError

    (xx, yy), radius = line_fitting(mask)

    # ----------debug ここから ----------
    if settings.OUT_IMAGE:
        OutPath = "OutImage"
        if not os.path.exists(OutPath):
            os.makedirs(OutPath)
        cv2.imwrite(OutPath + os.sep + "apple1.png", img)
        cv2.imwrite(OutPath + os.sep + "apple2.png", mask)

        img_circle = img.copy()
        cv2.circle(img_circle,(xx, yy), radius,(0,255,0),2)
        cv2.imwrite(OutPath + os.sep + "apple5.png", img_circle)
    # ----------debug ここまで ----------

    size_per_pixel = 210 / (radius * 2)
    return size_per_pixel


def generating_mask(img):
    # 画像を読み込む。
    fg_img = img

    # # HSV に変換する。
    hsv = cv2.cvtColor(fg_img, cv2.COLOR_BGR2HSV)

    # 特定の色のそれぞれの値の下限と上限を閾値にして2値化する。
    bin_img = ~cv2.inRange(hsv, (0, 0, 200), (255, 255, 255))

    bin_img[bin_img == 0] = 1
    bin_img[bin_img == 255] = 0

    if np.count_nonzero(bin_img[:, :]) < 100:
        notmask = [0]
        return notmask

    # 輪郭抽出する。
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 面積が最大の輪郭を取得する
    contour = max(contours, key=lambda x: cv2.contourArea(x))

    # マスク画像を作成する。
    mask = np.zeros_like(fg_img)
    cv2.drawContours(mask, [contour], -1, color=(255, 255, 255), thickness=-1)

    return mask


def line_fitting(mask):
    img = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(img, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 1, 2)

    cnt = contours[0]

    maskb = np.zeros_like(mask)

    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)

    return center, radius
