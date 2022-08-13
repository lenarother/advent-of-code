import time
from random import randint

import cv2
import numpy as np

# Color format: BGR
BLUE = 255, 0, 0
GREEN = 0, 255, 0
RED = 0, 0, 255

SIZE = 700


def circle(a, xcenter, ycenter, radius, color):
    Y, X = np.ogrid[0:SIZE, 0:SIZE]
    square_dist = (X - xcenter) ** 2 + (Y - ycenter) ** 2
    mask = square_dist < radius ** 2
    a[mask] = color


bg = np.zeros((SIZE, SIZE, 3), dtype=np.uint8)
print(bg.shape)

square = bg.copy()
square[100:-100, 100:-100] = RED
square[200:-200, 200:-200] = GREEN
square[300:-300, 300:-300] = BLUE


x, y = SIZE // 2,  SIZE // 2
while True:
    img = square.copy()
    circle(img, y, x, 20, RED)
    cv2.imshow('title', img)
    x = randint(50, SIZE - 50)
    y = randint(50, SIZE - 50)
    time.sleep(0.2)
    key = chr(cv2.waitKey(1) & 0xFF)
    if key == 'q':
        break


cv2.destroyAllWindows()
