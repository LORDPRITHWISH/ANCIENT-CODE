import cv2
import numpy as np

size = (40, 40)

blank_image = np.zeros((size[0], size[1], 4), np.uint8)

# Make first 10 rows red and opaque
blank_image[:10] = [255,0,0,255]

# Make first 10 columns green and opaque
blank_image[:,:10] = [0,255,0,255]

cv2.imwrite('testy.png', blank_image)