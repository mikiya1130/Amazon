from django.test import TestCase
from django.urls import reverse

import numpy as np
import cv2
import base64
import json
from unittest import mock


def create_image(height=480, width=640, color=(0, 0, 0)):
    """単色のダミー画像を生成する

    Args:
        height (int, optional): 高さ. Defaults to 480.
        width (int, optional): 幅. Defaults to 640.
        color (tuple, optional): RGB. Defaults to (0, 0, 0).

    Returns:
        (np.ndarray): 画像データ.
    """
    img = np.zeros((height, width, 3))
    img += color[::-1]
    return img


class CalcVolumeViewTests(TestCase):
    @mock.patch("measurevolume.views.detect_water_area")
    @mock.patch("measurevolume.views.get_chopsticks_length_per_pixel")
    def test_base64_to_img(
        self, mock_get_chopsticks_length_per_pixel, mock_detect_water_area
    ):
        """base64から画像データへの変換をテスト"""
        mock_detect_water_area.return_value = create_image()  # dummy
        mock_get_chopsticks_length_per_pixel.return_value = 0.1  # dummy

        img = create_image()
        _, buf = cv2.imencode(".png", img)
        img_base64 = base64.b64encode(buf).decode("utf-8")

        data = {"img_base64": img_base64}

        _ = self.client.post(
            reverse("calc_volume"),
            data=json.dumps(data),
            content_type="application/json",
        )

        self.assertTrue(np.array_equal(img, mock_detect_water_area.call_args[0][0]))

    @mock.patch("measurevolume.views.detect_water_area")
    @mock.patch("measurevolume.views.get_chopsticks_length_per_pixel")
    def test_glass_and_chopsticks(
        self, mock_get_chopsticks_length_per_pixel, mock_detect_water_area
    ):
        """コップと割り箸の検出をテスト"""
        mock_detect_water_area.return_value = create_image()
        mock_get_chopsticks_length_per_pixel.return_value = 0.1

        img = create_image()
        _, buf = cv2.imencode(".png", img)
        img_base64 = base64.b64encode(buf).decode("utf-8")

        data = {"img_base64": img_base64}

        response = self.client.post(
            reverse("calc_volume"),
            data=json.dumps(data),
            content_type="application/json",
        )

        content = json.loads(response.content)

        self.assertTrue(content["exist_glass"])
        self.assertTrue(content["exist_chopsticks"])

    def test_glass(self):
        """コップの検出をテスト"""
        pass

    def test_chopsticks(self):
        """割り箸の検出をテスト"""
        pass

    def test_not_exist(self):
        """コップと割り箸の非検出をテスト"""
        pass

    def test_request_type_not_post(self):
        """POSTリクエスト以外の拒否をテスト"""
        pass

    def test_empty_json(self):
        """空のJSONに対する応答をテスト"""
        pass

    def test_no_key_img_base64(self):
        """キー'img_base64'を持たないJSONに対する応答をテスト"""
        pass

    def test_illegal_value_img_base64(self):
        """キー'img_base64'の値が不正なJSONに対する応答をテスト"""
        pass
