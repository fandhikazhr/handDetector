import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDrawStyles = mp.solutions.drawing_styles
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img , 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLM in results.multi_hand_landmarks:
            for id, lm in enumerate(handLM.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 12 or id == 8:
                    cv2.circle(img, (cx,cy), 10, (0, 255, 0), 5)
            mpDraw.draw_landmarks(img, handLM, mpHands.HAND_CONNECTIONS)
            # mpDraw.draw_landmarks(img, handLM, mpHands.HAND_CONNECTIONS, mpDrawStyles.get_default_hand_landmarks_style(), 
                # mpDrawStyles.get_default_hand_connections_style())
        print("\n")
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, "FPS : " + str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
