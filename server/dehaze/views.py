from django.shortcuts import render
from django.http import HttpResponse
import json, base64, os
import numpy as np
import json
import cv2 as cv
# from dehaze.main import dehaze

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


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
    ht = np.histogram(J_D, 256)
    d = np.cumsum(ht[0]) / float(J_D.size)
    divide = None
    for divide in range(255, 0, -1):
        if d[divide] < 0.999:
            break
    a_b = ori_img[:, :, 0][J_D >= ht[1][divide+1]].mean()
    a_g = ori_img[:, :, 1][J_D >= ht[1][divide+1]].mean()
    a_r = ori_img[:, :, 2][J_D >= ht[1][divide+1]].mean()
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


def checkAuth(request):
    if request.method == "POST":
        filnamelist = []
        for file in os.listdir("./dehaze/static"):
            # print(file)
            if os.path.isfile("./dehaze/static/" + file):
                filnamelist.append(file)
        return HttpResponse(
            json.dumps({
                "msg": "ok",
                "filenamelist": json.dumps(filnamelist)
            })
        )

    
# Create your views here.
# python manage.py runserver 8081
