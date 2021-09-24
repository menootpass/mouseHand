import HandTrackingModule as htm
import pyautogui as pt
import keyboard as key
import numpy as np
import json
import time
import math
import cv2

from time import sleep

menu = str(input("=> Menu :\nKlik A untuk memulai program\nKlik S untuk setting\nKlik Q untuk keluar\n>>"))

hasil_data = open("data.json", "r+")
data = json.loads(hasil_data.read())

os = data["os"]
vidCap = data["vidcap"]

hasil_data.close()

#######################################
wCam, hCam = 512, 384
frameR = 100
smoothening = 5
wScr, hScr = pt.size()[0], pt.size()[1]#
#######################################

clocX, clocY = 0, 0
plocX, plocY = 0, 0

cap = cv2.VideoCapture(vidCap)
cap.set(5, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(maxHands=1, detectionCon=0.7)

print("Starting...")
while jalan:
    
    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img, draw=False)

    # cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR),
                    # (255, 0, 220), 2)

    if len(lmList) != 0:
        # print(lmList[4], lmList[8])
        try:
            x1, y1 = lmList[8 ][1:]
            x2, y2 = lmList[12][1:]
            x4, y4 = lmList[4 ][1:]
            x5, y5 = lmList[16][1:]
            x6, y6 = lmList[20][1:]
            cx, cy = (x1+x2)//2, (y1+y2) // 2

            # cv2.circle(img, (x1, y1), 15, (255, 255, 0), cv2.FILLED)
            # cv2.circle(img, (x2, y2), 15, (255, 255, 0), cv2.FILLED)
            # cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
            # cv2.circle(img, (cx, cy), 5, (255, 255, 0), cv2.FILLED)

            x3 = np.interp(x2, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y2, (frameR, hCam - frameR), (0, hScr))

            # smoothening values
            # clocX = plocX + (x3 - plocX) / smoothening
            # clocX = plocY + (y3 - plocY) / smoothening

            pt.moveTo(wScr - x3, y3)

            # plocX, plocY = clocX, clocY

            length = math.hypot(x2 - x1, y2 - y1)
            length2 = math.hypot(x4 - x2, y4 - y2)
            scrollUp = math.hypot(x4 - x1, y4 - y1)
            scrollDown = math.hypot(x5 - x4, y5 - y4)
            # drag = math.hypot(x6 - x4, y6 - y4)
            # print(length)

            # find distance
            if length < 20:
                pt.click()
                sleep(0.7)
            if length2 < 20:
                pt.click(button="right")
            if scrollUp < 20:
                pt.scroll(10)
            if scrollDown < 20:
                pt.scroll(-10)
            # if drag < 20:
            #     pt.dragTo(wScr - x3, y3, 2, button="left")

            

        except:
            pass

    
    # cTime = time.time()
    # fps = 1/(cTime-pTime)
    # pTime = cTime
    # cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
    #     (255, 0, 0), 3)
    # 12. Display

    # cv2.imshow('image', img)
    cv2.waitKey(1)
    cv2.destroyAllWindows()