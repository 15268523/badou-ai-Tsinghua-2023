import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
equalizeHist-直方图均衡化
函数原型：equalizeHist(src,dst=None)
src:图像矩阵(单通道图像)
dst:默认即可
'''

img = cv2.imread("lenna.png",1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

dst=cv2.equalizeHist(gray)

hist=cv2.calcHist([dst],[0],None,[256],[0,256])
plt.figure()
plt.hist(dst.ravel(),256)
plt.show()

cv2.imshow("Histogram Equalization",np.hstack([gray,dst]))
cv2.waitKey(0)