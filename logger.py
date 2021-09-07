def logging(img):
    import cv2
    import numpy as np
    import math

    h, w, ch = img.shape
    c = 255/np.log(1+255)
    s = np.zeros(256, np.float)
    for rr in range(0, 256):
        s[rr] = c*np.log(1+rr)
    if ch == 1:
        for i in range(0, h):
            for j in range(0, w):
                img[i][j] = int(s[img[i][j]])

    if ch == 3:
        for i in range(0, h):
            for j in range(0, w):
                img[i][j][0] = int(s[img[i][j][0]])
                img[i][j][1] = int(s[img[i][j][1]])
                img[i][j][2] = int(s[img[i][j][2]])
