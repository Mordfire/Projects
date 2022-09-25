import HandTrackingModule as htm
import cv2
import mediapipe as mp
import os
import psutil


cap = cv2.VideoCapture(0)
detector = htm.handDetector()
tipsid = [4,8,12,16,20]
while True:
    yae, img = cap.read()
    img = detector.findHands(img, True)
    lmlist = detector.findPosition(img,draw=False)

    if len(lmlist) != 0:
        fingers = []
        for id in range(0,5):
            if lmlist[tipsid[id]][2] < lmlist[tipsid[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        if fingers[1] == 1 and fingers[2] == 1:
            if r"C:\Users\jojo\AppData\Local\Discord\app-1.0.9006/Discord.exe" in (i.name() for i in psutil.process_iter()):
                os.system("TASKKILL /F /IM " + r"C:\Users\jojo\AppData\Local\Discord\app-1.0.9006/Discord.exe")
        elif fingers[1] == 1 and fingers[2] == 0:
            print("Discord on")
            if r"C:\Users\jojo\AppData\Local\Discord\app-1.0.9006/Discord.exe" not in (i.name() for i in psutil.process_iter()):
                os.startfile(r"C:\Users\jojo\AppData\Local\Discord\app-1.0.9006/Discord.exe")

    cv2.imshow("camera", img)
    if cv2.waitKey(1) == ord("q"):
        break
