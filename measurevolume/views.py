from measurevolume.detect.water_area_correction import water_area_correction
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import cv2
import base64
import json
import numpy as np
import math
from .detect import detect_water_area, get_chopsticks_length_per_pixel, water_area_correction
from .exceptions import NotFoundGlassError, NotFoundChopsticksError


def index(request):
    return render(request, "measurevolume/index.html")


@csrf_exempt
@require_http_methods(["POST"])
def calc_volume(request: HttpRequest) -> JsonResponse:
    """水の容量を計算する

    Args:
        request (HttpRequest): Django HttpRequest オブジェクト
                               json.loads(request.body)["img_base64"]でbase64エンコード画像取得

    Returns:
        JsonResponse: JsonResponse オブジェクトは Django HttpResponse クラスのサブクラス
                                   以下を返す
                                   {
                                       exist_glass (boolean): コップの有無,
                                       exist_chopsticks (boolean): 割り箸の有無,
                                       volume (number): 容量(mL),
                                   }

    Note:
        POSTメソッドのみ受け付ける
    """

    img_base64 = json.loads(request.body)["img_base64"]
    img_data = base64.b64decode(img_base64)
    img_np = np.frombuffer(img_data, np.uint8)
    src = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)

    exist_glass = False
    exist_chopsticks = False
    volume = 0

    try:
        img = detect_water_area(src)

    except NotFoundGlassError:
        exist_glass = False
        volume = -1

    else:
        exist_glass = True

    try:
        mm_pixel = get_chopsticks_length_per_pixel(src)

    except NotFoundChopsticksError:
        exist_chopsticks = False
        volume = -1

    else:
        exist_chopsticks = True

    if exist_glass and exist_chopsticks:
        water = water_area_correction(img)
        one_cnt = np.count_nonzero(water, axis=1)
        area_of_circle = math.pi * (one_cnt * mm_pixel / 2) ** 2
        volume = np.sum(area_of_circle) * mm_pixel
        volume /= 1000

        exist_glass = True
        exist_chopsticks = True

    data = {
        "exist_glass": exist_glass,
        "exist_chopsticks": exist_chopsticks,
        "volume": volume,
    }
    return JsonResponse(data)
