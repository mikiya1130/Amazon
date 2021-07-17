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
    check = check_chopsticks(mask)
    if check < 40:
        # return check + 200
        raise NotFoundChopsticksError
    line = line_fitting(mask)
    Matched_image = Match_image(mask, line)
    x1, y1, x2, y2 = find_corner(Matched_image)
    size_per_pixel = find_size_per_pixel(x1, y1, x2, y2)
    # cv2.imwrite("apple1.png", img)
    # cv2.imwrite("apple2.png", mask)
    # cv2.imwrite("apple3.png", Matched_image)
    return size_per_pixel


# def imshow(img):
#         """ndarray 配列をインラインで Notebook 上に表示する。
#         """
#         ret, encoded = cv2.imencode(".jpg", img)
#         display(Image(encoded))


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
    M = cv2.moments(cnt)

    maskb = np.zeros_like(mask)

    rows, cols = mask.shape[:2]
    [vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    img = cv2.line(maskb, (cols - 1, righty), (0, lefty), (0, 255, 0), 10)

    return img


def Match_image(mask, line):
    comparison = np.where(mask[1] == line[1], 0, 255)
    comparison = mask & line
    return comparison


def find_corner(mask):
    x_min = 1000000
    x_max = 0
    i = mask.shape[0]
    memory_y_min = 0
    memory_y_max = 0

    for counter in range(i):
        x_columns = mask[counter, :, 1]
        x_positions = np.where(x_columns != 0)
        check = np.array(x_positions)
        if check.size != 0:
            x_min_tmp = np.min(x_positions)
            x_max_tmp = np.max(x_positions)

            if x_min_tmp < x_min:
                x_min = x_min_tmp
                memory_y_min = counter
            if x_max_tmp > x_max:
                x_max = x_max_tmp
                memory_y_max = counter

    return x_min, memory_y_min, x_max, memory_y_max


def find_size_per_pixel(x1, y1, x2, y2):
    v1 = np.array([x1, y1])
    v2 = np.array([x2, y2])
    dis = np.linalg.norm(v1 - v2)
    per_pixel = 210 / dis
    return per_pixel


def check_chopsticks(mask):
    x1, y1, x2, y2 = find_corner(mask)
    v1 = np.array([x1, y1])
    v2 = np.array([x2, y2])
    diff = v2 - v1
    ratio = np.abs(diff[0] / diff[1])
    return np.round(ratio)
