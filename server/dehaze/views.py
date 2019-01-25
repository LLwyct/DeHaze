from django.shortcuts import render
from django.http import HttpResponse
import json, base64, os
import numpy as np
import json
import cv2 as cv
# from dehaze.main import dehaze

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


# # 最小堆调整
# def heapAdjust(h, lo, hi):
#     temp = h[lo]
#     i = (lo << 1)
#     while i <= hi:
#         if i < hi and h[i+1][2] < h[i][2]:
#             i += 1
#         if h[i][2] > temp[2]:
#             break
#         h[lo] = h[i]
#         lo = i
#         i = (i<<1)
#     h[lo] = temp


# # 初建堆，使前k个元素成为大根堆
# def heapConstruct(heap, k):
#     for i in range(k//2, 0, -1):
#         heapAdjust(heap, i, k)


# def topKMaxValue(heap, k):
#     heapConstruct(heap, k)
#     for i in range(k+1, len(heap)):
#         if heap[i][2] > heap[1][2]:
#             temp = heap[1]
#             heap[1] = heap[i]
#             heap[i] = temp
#             heapAdjust(heap, 1, k)
# 
# 
# def imgShow(img):
#     cv.namedWindow('img', cv.WINDOW_AUTOSIZE)
#     cv.imshow('img', img)
#     cv.waitKey(0)


def calculate_J(ori_img, airlight, Rough_T):
    (x, y) = Rough_T.shape
    temp_ori_img = ori_img.astype(np.int16)
    for i in range(3):
        temp_ori_img[:, :, i] = ((temp_ori_img[:,:,i] - airlight[i]) / Rough_T) + airlight[i]
    temp_ori_img[temp_ori_img < 0] = 0
    temp_ori_img[temp_ori_img > 255] = 255
    return temp_ori_img.astype(np.uint8)


def getRough_T(J_D, omg=0.98):
    Rough_T = np.zeros(J_D.shape, np.float32)
    Rough_T = J_D / 255
    Rough_T = (1 - Rough_T)*omg
    Rough_T[Rough_T<0.05] = 0.05
    return Rough_T


def getAirlight(J_D, ori_img):
    # (x, y) = J_D.shape
    # num = x*y // 1000
    # arr = [[-1,-1,-1]]
    # for i in range(x):
    #     for j in range(y):
    #         arr.append([i,j,J_D[i][j]])
    # topKMaxValue(arr, num)
    # arr = arr[1: 1+num]
    # sum_b = 0
    # sum_g = 0
    # sum_r = 0
    # for i in arr:
    #     if i[0] != -1:
    #         sum_b += ori_img[i[0]][i[1]][0]
    #         sum_g += ori_img[i[0]][i[1]][1]
    #         sum_r += ori_img[i[0]][i[1]][2]
    # return (sum_b//num, sum_g//num, sum_r//num)
    ht = np.histogram(J_D, 1000)
    d = np.cumsum(ht[0]) / float(J_D.size)
    divide = None
    for divide in range(999, 0, -1):
        if d[divide] <= 0.999:
            break
    a_b = ori_img[:, :, 0][J_D >= ht[1][divide]].mean()
    a_g = ori_img[:, :, 1][J_D >= ht[1][divide]].mean()
    a_r = ori_img[:, :, 2][J_D >= ht[1][divide]].mean()
    return (int(a_b), int(a_g), int(a_r))


def getDarkChannelImage(ori_img, windowsize=3):
    return cv.erode(np.min(ori_img, 2), cv.getStructuringElement(cv.MORPH_RECT, (windowsize, windowsize)))


def dehaze(ori_img):
    J_D = getDarkChannelImage(ori_img)
    airlight = getAirlight(J_D, ori_img)
    Rough_T = getRough_T(J_D)
    res = calculate_J(ori_img, airlight, Rough_T)
    return res


def handle_uploaded_file(file):
    with open(os.path.join(BASE_DIR, 'static', file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def index(request):
    if request.method == "POST":
        file = request.FILES['file']
        handle_uploaded_file(file)
        res = dehaze(cv.imread(os.path.join(BASE_DIR, 'static', file.name)))
        cv.imwrite(os.path.join(BASE_DIR, 'static', 'dehaze_'+file.name), res)
        with open(os.path.join(BASE_DIR, 'static', 'dehaze_'+file.name), 'rb+') as f:
            image_byte = base64.b64encode(f.read())
        return HttpResponse(json.dumps({
            "msg": "ok",
            "img": image_byte.decode('ascii')
        }))
    return HttpResponse("<h1>nothing</h1>")
# Create your views here.
# python manage.py runserver 8081
