import cv2 as cv
import mediapipe as mp
import time


class poseDetector():

    def __init__(self, mode = False, upBody = False, smooth = True, detectConfidence = 0.5, trackConfidence = 0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectConfidence = detectConfidence
        self.trackConfidence = trackConfidence

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,self.upBody,self.smooth,self.detectConfidence,self.trackConfidence)

    def findPose(self, img, draw = True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        
        return img
    
    def findPosition(self, img, draw = True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, 'Cx: ', cx, 'Cy: ', cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 10, (255, 255, 255), 2)
        return lmList
        


def main():
    cap = cv.VideoCapture('video1.mp4')
    pTime = 0
    detector = poseDetector()
    while(True):
        success, img = cap.read()   
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList)
        

        cTime = time.time() 
        fps = 1 /(cTime-pTime)
        pTime = cTime
        cv.putText(img, str(int(fps)), (70, 100), cv.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 4)
        cv.imshow('Video', img)

        cv.waitKey(1)


if __name__ == '__main__':
    main()