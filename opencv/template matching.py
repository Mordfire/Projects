img = cv2.imread("assets/soccer_practice.jpg",0)
template = cv2.imread("assets/shoe.png",0)
h,w = template.shape
print(h)
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:  #metodi koito rabotqt s min loc
        location = min_loc
    else:
        location = max_loc

    cv2.rectangle(img2,location,(location[0]+w,location[1]+h),255,5)
    cv2.imshow("match",img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()