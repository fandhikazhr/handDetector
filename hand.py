import math
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import cvzone

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
