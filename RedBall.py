# https://www.gamepix.com/play/red-ball
# For Red Ball 4(Copy) Online

import cv2 as cv
import time
import PoseModule as pm
import math
from pynput.keyboard import Key, Controller

keyboard = Controller()

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
pTime = 0
detector = pm.poseDetector()

flag = 0 # 1 for up, 0 for down
count = 0
while(True):
    success, img = cap.read()   
    img = detector.findPose(img)
    lmList = detector.findPosition(img, False)
    if len(lmList) != 0:
        left_wrist = lmList[15]
        left_elbow = lmList[13]
        left_shoulder = lmList[11]
        right_wrist = lmList[16]
        right_elbow = lmList[14]
        right_shoulder = lmList[12]


        cv.circle(img, (left_wrist[1], left_wrist[2]), 6, (255, 255, 255), -1)
        cv.circle(img, (left_elbow[1], left_elbow[2]), 6, (255, 255, 255), -1)
        cv.circle(img, (right_wrist[1], right_wrist[2]), 6, (255, 255, 255), -1)
        cv.circle(img, (right_elbow[1], right_elbow[2]), 6, (255, 255, 255), -1)
        cv.circle(img, (left_shoulder[1], left_shoulder[2]), 6, (255, 255, 255), -1)
        cv.circle(img, (right_shoulder[1], right_shoulder[2]), 6, (255, 255, 255), -1)

        # print('Right Wrist: ', right_wrist[1], right_wrist[2])
        # print('Right Elbow: ', right_elbow[1], right_elbow[2])
        # print('Right Shoulder: ', right_shoulder[1], right_shoulder[2])

        if right_wrist[1]<=(right_elbow[1] - 15):
            print("RIGHT!")
            keyboard.press(Key.right)
        else:
            print("NOT RIGHT")
            keyboard.release(Key.right)
            # keyboard.press(Key.left)
            # keyboard.release(Key.left)
        
        if left_wrist[1]>=(left_elbow[1] + 15):
            print("LEFT!")
            keyboard.press(Key.left)
        else:
            print("NOT LEFT")
            keyboard.release(Key.left)
            # keyboard.press(Key.right)
            # keyboard.release(Key.right)
        
        if left_elbow[2]<=(left_shoulder[2] + 10) or right_elbow[2]<=(right_shoulder[2] + 10):
            print("UP!")
            keyboard.press(Key.up)
        else:
            print("NOT UP")
            keyboard.release(Key.up)


    
    # cTime = time.time() 
    # fps = 1 /(cTime-pTime)
    # pTime = cTime

    # cv.putText(img, str(int(fps)), (70, 100), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 4)
    cv.imshow('Video', img)

    

    if cv.waitKey(20) & 0xFF== ord('q'): # break when q is pressed
        break

cv.capture.release()
cv.destroyAllWindows()

