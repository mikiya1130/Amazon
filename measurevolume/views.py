from django import shortcuts
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.request import HttpRequest
from django.http.response import JsonResponse

import cv2
import base64
import numpy as np
import math
from .detect import detect_water_area, get_chopsticks_length_per_pixel
from .exceptions import NotFoundGlassError, NotFoundChopsticksError


def index(request):
    return render(request, "measurevolume/index.html")


@require_http_methods(["POST"])
def calc_volume(request: HttpRequest) -> JsonResponse:
    """水の容量を計算する

    Args:
        request (HttpRequest): Django HttpRequest オブジェクト
                               request.POST["img_base64"]でbase64エンコード画像取得

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
    img_base64 = request.POST["img_base64"]
    img_data = base64.b64decode(img_base64)
    img_np = np.frombuffer(img_data, np.uint8)
    src = cv2.imdecode(img_np, cv2.IMREAD_ANYCOLOR)

    try:
        img = detect_water_area(src)
        mm_pixel = get_chopsticks_length_per_pixel(src)

    except NotFoundGlassError:
        exist_glass = False
        volume = -1

    except NotFoundChopsticksError:
        exist_chopsticks = False
        volume = -1

    else:
        volume = 0
        p = 0
        while p < img.shape[0]:
            s = img[p : p + 3, 0 : img.shape[1]]
            o = np.count_nonzero(s)
            r = o / 6
            h = 3 * mm_pixel
            v = math.pi * r * r * h
            volume += v
            p += 3

        exist_glass = True
        exist_chopsticks = True

    finally:
        data = {
            "exist_glass": exist_glass,
            "exist_chopsticks": exist_chopsticks,
            "volume": volume,
        }
        return JsonResponse(data)
