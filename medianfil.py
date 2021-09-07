def noisered(img):
    import cv2
    import math
    import numpy as np
    import image as img1
    hi, wi, ch = img.shape
    img1 = np.zeros((hi, wi, ch), np.uint8)
    if ch == 1:
        for h in range(1, hi-1):
            for w in range(1, wi-1):
                q = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        aas = img[h+i, w+j]
                        q.append(aas)
                q.sort()
                value = q[4]
                img1[h, w] = value

        for ha in range(1, hi-1):
            img1[ha][0] = img1[ha][1]
            img1[ha][wi-1] = img1[ha][wi-2]
        for wa in range(0, wi):
            img1[0][wa] = img1[1][wa]
            img1[hi-1][wa] = img1[hi-2][wa]
        for ih in range(0, hi):
            for iw in range(0, wi):
                img[ih][iw] = img1[ih][iw]

    if ch == 3:
        for h in range(1, hi-1):
            for w in range(1, wi-1):
                q0 = []
                q1 = []
                q2 = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        aas0 = img[h+i, w+j, 0]
                        q0.append(aas0)
                        aas1 = img[h+i, w+j, 1]
                        q1.append(aas1)
                        aas2 = img[h+i, w+j, 2]
                        q2.append(aas2)
                q0.sort()
                q1.sort()
                q2.sort()
                value0 = q0[4]
                value1 = q1[4]
                value2 = q2[4]
                img1[h, w, 0] = value0
                img1[h, w, 1] = value1
                img1[h, w, 2] = value2

        for ha in range(1, hi-1):
            img1[ha][0][0] = img1[ha][1][0]
            img1[ha][0][1] = img1[ha][1][1]
            img1[ha][0][2] = img1[ha][1][2]
            img1[ha][wi-1][0] = img1[ha][wi-2][0]
            img1[ha][wi-1][1] = img1[ha][wi-2][1]
            img1[ha][wi-1][2] = img1[ha][wi-2][2]

        for wa in range(0, wi):
            img1[0][wa][0] = img1[1][wa][0]
            img1[0][wa][1] = img1[1][wa][1]
            img1[0][wa][2] = img1[1][wa][2]
            img1[hi-1][wa][0] = img1[hi-2][wa][0]
            img1[hi-1][wa][1] = img1[hi-2][wa][1]
            img1[hi-1][wa][2] = img1[hi-2][wa][2]

        for ih in range(0, hi):
            for iw in range(0, wi):
                img[ih][iw][0] = img1[ih][iw][0]
                img[ih][iw][1] = img1[ih][iw][1]
                img[ih][iw][2] = img1[ih][iw][2]
