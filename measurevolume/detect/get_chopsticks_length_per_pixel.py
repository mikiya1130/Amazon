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
    return 0.1  # dummy
