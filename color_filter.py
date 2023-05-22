import cv2
import numpy as np

img_file = 'shapes.png'

# RGB이미지 데이터
img = cv2.imread(img_file)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

dst1= cv2.inRange(img, (0,0,100), (150, 150,255))
#H(색상):160~179 S(채도):200~255 V(진하기):0~255
dst2= cv2.inRange(img_hsv, (160,200,0), (179, 255,255))

cv2.imshow('original', img) #rgb
cv2.imshow('red only', dst1)
cv2.imshow('red only with hsv', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()