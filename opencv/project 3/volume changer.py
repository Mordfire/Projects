import math
import cv2
import numpy as np
import time
import HandTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectioncon=0.75)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

minVol = volume.GetVolumeRange()[0]
maxVol = volume.GetVolumeRange()[1]


while True:
    success, img = cap.read()

    img = detector.findHands(img)
    landmark = detector.findPosition(img,draw=False)
    if len(landmark) != 0:
        index1,x1,y1 = landmark[4]
        index2, x2, y2 = landmark[8]
        cx,cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img,(x1,y1),3,(255,0,0),3)
        cv2.circle(img, (x2, y2), 3, (255, 0, 0), 3)
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)
        cv2.circle(img, (cx, cy), 3, (255, 0, 0), 3)

        lenght_line = math.hypot(x2-x1,y2-y1)
        if lenght_line<50:
            cv2.circle(img, (cx, cy), 3, (0, 255, 0), 3)
        vol = np.interp(lenght_line,[20,200],[minVol,maxVol])
        volume.SetMasterVolumeLevel(vol, None)

    cv2.imshow("Original", img)
    cv2.waitKey(1)