import cv2
import numpy as np

img = cv2.imread("mirror11.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray,100,0.01,150)
corners = np.int0(corners)


for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),1,(255,0,0),-1)

for i in range(len(corners)):
    for j in range(i+1,len(corners)):
        corner1 = tuple(corners[i].ravel())
        corner2 = tuple(corners[j].ravel())
        cv2.line(img,corner1,corner2,(0,0,0),1)


cv2.imshow("corner",img)
cv2.waitKey(0)
cv2.destroyAllWindows()