from django.test import TestCase
from django.test import Client


class CalcVolumeViewTests(TestCase):
    def test_glass_and_chopsticks(self):
        """コップと割り箸の検出をテスト"""
        pass

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
