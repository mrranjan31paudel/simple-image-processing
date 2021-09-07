def binarization(img):
    import numpy as np
    import gray
    h, w, ch = img.shape
    binImg = np.zeros((h, w, 1), np.uint8)
    if ch == 1:
        for i in range(0, h):
            for j in range(0, w):
                if img[i, j] >= 127:
                    binImg[i, j] = 255
                else:
                    binImg[i, j] = 0
        return binImg
    if ch == 3:
        grayImg = gray.grayscale(img)
        for i in range(0, h):
            for j in range(0, w):
                if grayImg[i, j] >= 127:
                    binImg[i, j] = 255
                else:
                    binImg[i, j] = 0
        return binImg
