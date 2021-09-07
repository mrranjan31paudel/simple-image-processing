def histoplot(img, chval):
    import numpy as np
    import cv2 as cv
    h, w, ch = img.shape
    if ch == 1:
        glevel = np.zeros(256, np.uint)
        res = h*w
        for i in range(0, h):
            for j in range(0, w):
                glevel[img[i, j]] += 1

        maxh = np.max(glevel)
        normaxh = maxh/res
        limitu = res*0.9/maxh
        img1 = np.zeros((300, 766, 1), np.uint8)

        for levels in range(0, 256):
            point = int(limitu*(glevel[levels]/res)*300)
            for ii in range(0, 300):
                if ii >= 300-point:
                    img1[ii, levels*3] = 0
                    img1[ii, levels*3-1] = 0
                    img1[ii, levels*3-2] = 255
                else:
                    img1[ii, levels*3] = 255
                    img1[ii, levels*3-1] = 255
                    img1[ii, levels*3-2] = 255

    if ch == 3:
        glevel = np.zeros((ch, 256), np.uint)
        res = h*w
        for i in range(0, h):
            for j in range(0, w):
                glevel[chval, img[i, j, chval]] += 1

        maxh = np.max(glevel[chval])
        normaxh = maxh/res
        limitu = res*0.9/maxh
        img1 = np.zeros((300, 766, 3), np.uint8)

        for levels in range(0, 256):
            point = int(limitu*(glevel[chval, levels]/res)*300)
            for ii in range(0, 300):
                if ii >= 300-point:
                    img1[ii, levels*3, chval] = 255
                    img1[ii, levels*3-1, chval] = 255
                    img1[ii, levels*3-2] = [255, 255, 255]
                else:
                    img1[ii, levels*3] = [255, 255, 255]
                    img1[ii, levels*3-1] = [255, 255, 255]
                    img1[ii, levels*3-2] = [255, 255, 255]
    return img1
