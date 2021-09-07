def negation(img):
    import cv2
    import numpy as np
    import math
    h, w, ch = img.shape
    if ch == 3:
        for i in range(0, h):
            for j in range(0, w):
                img[i][j][0] = 255-img[i][j][0]
                img[i][j][1] = 255-img[i][j][1]
                img[i][j][2] = 255-img[i][j][2]

    if ch == 1:
        for i in range(0, h):
            for j in range(0, w):
                img[i][j] = 255-img[i][j]
