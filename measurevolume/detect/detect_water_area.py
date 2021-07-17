from django.conf import settings

import os
import numpy as np
import cv2
import logging

from ..exceptions import NotFoundGlassError

if not settings.LITE:
    import torch
    from . import FCN_NetModel as FCN  # The net Class
    from . import CategoryDictionary as CatDic

############################################Input parameters###################################################################################
# -------------------------------------Input parameters-----------------------------------------------------------------------
UseGPU = False  # Use GPU or CPU  for prediction (GPU faster but demend nvidia GPU and CUDA installed else set UseGPU to False)
FreezeBatchNormStatistics = False  # wether to freeze the batch statics on prediction  setting this true or false might change the prediction mostly False work better
OutEnding = ""  # Add This to file name
nm = "Filled"

# -----------------------------------------Location of the pretrain model-----------------------------------------------------------------------------------
Trained_model_path = "measurevolume/detect/TrainedModelWeiht1m_steps_Semantic_TrainedWithLabPicsAndCOCO_AllSets.torch"


def detect_water_area(img: np.ndarray) -> np.ndarray:
    """水の領域を検出し2値画像で返す

    https://github.com/aspuru-guzik-group/Semantic-segmentation-of-materials-and-vessels-in-chemistry-lab-using-FCN

    Args:
        img (np.ndarray): 元画像

    Returns:
        np.ndarray: 2値画像(水領域:1, その他:0)

    Raises:
        NotFoundGlassError: コップが検出できなかった場合に送出
    """
    if settings.LITE:
        return img[:, :, 0]

    logger = logging.getLogger(__name__)
    ##################################Load net###########################################################################################
    # ---------------------Create and Initiate net and create optimizer------------------------------------------------------------------------------------
    Net = FCN.Net(CatDic.CatNum)  # Create net and load pretrained encoder path
    Net.load_state_dict(
        torch.load(Trained_model_path, map_location=torch.device("cpu"))
    )
    # --------------------------------------------------------------------------------------------------------------------------
    h, w, d = img.shape
    r = np.max([h, w])
    if (
        r > 840
    ):  # Image larger then 840X840 are shrinked (this is not essential, but the net results might degrade when using to large images
        fr = 840 / r
        img = cv2.resize(img, (int(w * fr), int(h * fr)))
    Imgs = np.expand_dims(img, axis=0)
    if not (type(img) is np.ndarray):
        logger.warning("img is not numpy array. type is {}".format(type(img)))
        raise NotFoundGlassError
    # ................................Make Prediction.............................................................................................................
    with torch.autograd.no_grad():
        OutProbDict, OutLbDict = Net.forward(
            Images=Imgs,
            TrainMode=False,
            UseGPU=UseGPU,
            FreezeBatchNormStatistics=FreezeBatchNormStatistics,
        )  # Run net inference and get prediction
    # ...............................Save prediction on fil
    Lb = OutLbDict[nm].data.cpu().numpy()[0].astype(np.uint8)
    if Lb.mean() < 0.001:
        raise NotFoundGlassError

    ImOut = np.zeros((h, w))
    ImOut[:, :][Lb == 1] = 1

    # ----------debug ここから ----------
    if settings.OUT_IMAGE:
        ImOverlay1 = img.copy()
        ImOverlay1[:, :, 0][Lb == 1] = 255
        ImOverlay1[:, :, 1][Lb == 1] = 0
        ImOverlay1[:, :, 2][Lb == 1] = 255
        FinIm = np.concatenate([img, ImOverlay1], axis=1)

        OutPath = "OutImage"
        if not os.path.exists(OutPath):
            os.makedirs(OutPath)
        OutName = OutPath + os.sep + "water_segmentation.png"
        cv2.imwrite(OutName, FinIm)
    # ----------debug ここまで ----------

    return ImOut
