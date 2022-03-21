import math
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detector = HandDetector(detectionCon=0.8, maxHands=1)

x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    # hands = detector.findHands(img, draw=False)
    if hands:
        lmList = hands[0]['lmList']
        x, y, w, h = hands[0]['bbox']
        # print (lmList)
        x1, y1 = lmList[5]
        x2, y2 = lmList[17]
        distance = int(math.sqrt((y2-y1) ** 2 + (x2-x1) ** 2))
        A, B, C = coff
        distanceCM = A*distance**2 + B*distance + C
        # cvzone.rectangle(img, (x,y), (x + w, y + h), (255, 0, 255), 3)
        # cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x+5,y-10))
        cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x, y))
        # print(distanceCM, distance)
        # print(abs(x2-x1), distance)
    cv2.imshow("Webcam", img)
    cv2.waitKey(1)
