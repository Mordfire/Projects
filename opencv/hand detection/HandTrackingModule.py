import cv2
import mediapipe as mp
import time



class handDetector():
    def __init__(self,mode=False,maxHands=2,model_compl=1,detectioncon=0.5,trackcon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.model_compl = model_compl
        self.detectioncon = detectioncon
        self.trackcon = trackcon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.model_compl,self.detectioncon,self.trackcon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLandmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLandmarks, self.mpHands.HAND_CONNECTIONS)

        return img

    def findPosition(self,img,handNumber=0,draw=True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNumber]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id,cx,cy])
                if draw:
                    cv2.circle(img,(cx,cy),10,(255,40,29),cv2.FILLED)
        return lmlist





def main():
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        yae, img = cap.read()
        img = detector.findHands(img,True)
        lmlist = detector.findPosition(img)
        print(lmlist)
        cv2.imshow("camera", img)
        if cv2.waitKey(1) == ord("q"):
            break




if __name__ == '__main__':
    main()