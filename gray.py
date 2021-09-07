def grayscale(img):
    import numpy as np
    #import image as img2
    h, w, ch = img.shape
    img2 = np.zeros((h, w, 1), np.uint8)
    if ch == 3:
        for i in range(0, h):
            for j in range(0, w):
                img2[i][j] = int(0.07*img[i][j][0]+0.72*img[i]
                                 [j][1]+0.21*img[i][j][2])

        return img2
    if ch == 1:
        return img
