cap = cv2.VideoCapture("MOVI0035.avi")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    widght = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100,100,100])
    upper_blue = np.array([255,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",result)


    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()