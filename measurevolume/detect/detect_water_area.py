import numpy as np
import cv2


def detect_water_area(img: np.ndarray) -> np.ndarray:
    """水の領域を検出し2値画像で返す

    Args:
        img (np.ndarray): 元画像

    Returns:
        np.ndarray: 2値画像(水領域:1, その他:0)

    Raises:
        NotFoundGlassError: コップが検出できなかった場合に送出
    """
    pass
