import cv2
import imutils
img = cv2.imread("4731772-cover-op-bien-so-xe-hoi-1578451851-width1004height565.jpg")
#lay do dai, cao anh
h, w, c = img.shape
#du doan neu no khong phai la chup can bien so xe thif zoom len
if h != 160 and w != 718:
    #tim contour bien so xe
    # - chuyen xam
    # - ap threshhold
    # - tim contour
    # - lay list
    # - zoom len
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thres = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 10)
    contours = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    list = imutils.grab_contours(contours)
    contours = sorted(list, key=cv2.contourArea, reverse=False)
    i = contours[len(list) - 2]
    (x, y, w, h) = cv2.boundingRect(i)
    img = img[ y:y+h, x:x+w,]
    img = cv2.resize(img, (718, 160))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#ap thresh hold -> anh nhi phan(trang den)
thres = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 10)
#tim contour
contours = cv2.findContours(thres, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#ham find ra 3 cai : anh chinh sua, DANH SACH VIEN, he so thuoc tinh
#tuy nhien ta chi can lay danh sach vien nen ta xai ham grab
list = imutils.grab_contours(contours)
h1, w1, c1 = img.shape
for i in list:
    #chay i tao cai khung bao quanh cai vat the da contour
    (x, y, w, h) = cv2.boundingRect(i)
    if (30 < w <150) and (h1 // 2 + 20 < h <150):
        cv2.rectangle(img, (x,y), (x + w, y+h), (0, 26, 131), 2)
cv2.imshow("Detected N", img)
cv2.waitKey(0)
cv2.destroyAllWindows()