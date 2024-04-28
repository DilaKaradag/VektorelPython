# resim1 = ([[250],[200],[150],[100]]) # gri tonlarda 4 pixellik bir resim olabilir.
# resim2 = [
    # [250,200,150,100],
    # [250,200,150,100],
    # [250,200,150,100],
    # ] # gri tonları 4x3 pixellik bir resim olabilir.
# resim3 = [[250,0,0],[200,0,0],[150,0,0],[100,0,0]] # kırmızı tonlarda RGB 4 pixellik bir resim olabilir.

# resim4 = [
#     [[250,0,0],[200,0,0],[150,0,0],[100,0,0]],
#     [[250,0,0],[200,0,0],[150,0,0],[100,0,0]],
#     [[250,0,0],[200,0,0],[150,0,0],[100,0,0]]
#     ] # kırmızı tonlarda RGB 12 pixellik bir resim olabilir.

# pip install numpy
import numpy as np
resim5= np.full((300, 500, 3), [255, 0, 0], dtype=np.uint8)
resim6= np.full((5, 7, 3), [100, 0, 100], dtype=np.uint8)
print(resim6)

import cv2
# img = cv2.imread('images/bayrak1.png')
cv2.namedWindow("Deneme", cv2.WINDOW_NORMAL)
cv2.imshow('Deneme',resim6)
cv2.waitKey(0) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kapa

# pip install opencv-python
# import cv2
# print(cv2.__version__)
