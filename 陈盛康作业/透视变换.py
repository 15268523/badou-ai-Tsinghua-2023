import cv2
import numpy as np

img = cv2.imread('photol.jpg')

result3 = img.copy()

src = np.float32([[533,49],[1801,389],[21,1825],[1309,2173]])
dst = np.float32([[0,0],[1312,0],[0,1848],[1312,1848]])
print(img.shape)
m=cv2.getPerspectiveTransform(src,dst)
print("wrapMatrix:")
print(m)
result = cv2.warpPerspective(result3, m, (1312, 1848))
cv2.imshow("src",img)
cv2.imshow("result",result)
cv2.waitKey(0)
