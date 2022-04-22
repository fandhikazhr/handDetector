import cv2
import mediapipe as mp
import time

class handTrack():
    def __init__(self, mode=False, maxHands=2, minDetectConfidence=0.5, minTrackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.minDetectConfidence = minDetectConfidence
        self.minTrackConfidence = minTrackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDrawStyles = mp.solutions.drawing_styles
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        img = cv2.flip(img , 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.hands.process(imgRGB)
