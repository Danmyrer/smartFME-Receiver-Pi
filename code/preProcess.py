# TODO
# - bereitet img[] für tesseract.py vor
# - returns processedImg[]

import cv2
import os
import glob

USE_DUMMY = True
LOG_IMAGES = True

def preProcess(img):
    print("[preProcess] PreProcessing images")
    
    temp = []
    for i in img:
        n = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
        temp.append(n)
    img = temp
    
    temp = []
    for i in img:
        n = cv2.threshold(i, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        temp.append(n)
    img = temp

    temp = []
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    for i in img:
        n = cv2.erode(i, None, iterations = 5)
        temp.append(n)
    img = temp

    if LOG_IMAGES == True:
        for i in range(len(img)):
            print("[preProcess] Logging images", end=" ")
            print(str(i+1) + " / " + str(len(img)))
            cv2.imwrite("closed" + str(i) + ".png", img[i])
            
#region debug
def import_dummy():
    print("[preProcess] Importing dummy images")
    path = glob.glob("*.jpg")
    img = []
    for i in path:
        n = cv2.imread(i)
        img.append(n)
    return img

os.chdir('git/smartFME-Reciever/code/test_images')
preProcess(import_dummy())
#endregion