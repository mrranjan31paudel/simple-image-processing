def powring(img):
    import cv2
    import numpy as np
    import math

    h, w, ch = img.shape
    c = 1
    gamma = 0.25
    s = np.zeros(256, np.float)
    for rr in range(0, 256):
        s[rr] = c*np.power(rr/255, 1/gamma)

    if ch == 1:
        for i in range(0, h):
            for j in range(0, w):
                img[i][j] = (255*s[img[i][j]])

    if ch == 3:
        for i in range(0, h):
            for j in range(0, w):
                img[i][j][0] = (255*s[img[i][j][0]])
                img[i][j][1] = (255*s[img[i][j][1]])
                img[i][j][2] = (255*s[img[i][j][2]])
