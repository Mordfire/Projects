cap = cv2.VideoCapture("MOVI0035.avi")

while True:
    ret, frame = cap.read()
    widght = int(cap.get(3))
    height = int(cap.get(4))
    image = np.zeros(frame.shape,np.uint8)

    smaller_frame = cv2.resize(frame*1.5,(0,0),fx=0.5,fy=0.5)
    image[:height//2,:widght//2] = cv2.rotate(smaller_frame,cv2.ROTATE_180)
    image[height // 2:height,widght // 2:widght] = smaller_frame
    image[height // 2:, :widght // 2] = smaller_frame
    image[:height // 2,widght // 2:] = smaller_frame
    cv2.imshow("frame",image)


    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()