from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.request import HttpRequest
from django.http.response import JsonResponse

import cv2


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
    pass
