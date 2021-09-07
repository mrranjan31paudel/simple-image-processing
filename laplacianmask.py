def lapmask(img):
    import math
    import numpy as np
    import image as img1

    hi, wi, ch = img.shape
    img1 = np.zeros((hi, wi, ch), np.uint8)

    mask = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    if ch == 1:
        for h in range(1, hi-1):
            for w in range(1, wi-1):
                q = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        aas = img[h+i, w+j]*mask[i+1, j+1]
                        q.append(aas)
                if np.sum(q) > 255:
                    s = 255
                elif np.sum(q) < 0:
                    s = 0
                else:
                    s = np.sum(q)
                value = s
                img1[h, w] = value
        for ha in range(1, hi-1):
            img1[ha][0] = img1[ha][1]
            img1[ha][wi-1] = img1[ha][wi-2]
        for wa in range(0, wi):
            img1[0][wa] = img1[1][wa]
            img1[hi-1][wa] = img1[hi-2][wa]

    if ch == 3:
        for h in range(1, hi-1):
            for w in range(1, wi-1):
                q0 = []
                q1 = []
                q2 = []
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        aas0 = img[h+i, w+j, 0]*mask[i+1, j+1]
                        aas1 = img[h+i, w+j, 1]*mask[i+1, j+1]
                        aas2 = img[h+i, w+j, 2]*mask[i+1, j+1]
                        q0.append(aas0)
                        q1.append(aas1)
                        q2.append(aas2)
                if np.sum(q0) > 255:
                    img1[h, w, 0] == 255
                elif np.sum(q0) < 0:
                    img1[h, w, 0] == 0
                else:
                    img1[h, w, 0] == np.sum(q0)

                if np.sum(q1) > 255:
                    img1[h, w, 1] == 255
                elif np.sum(q1) < 0:
                    img1[h, w, 1] == 0
                else:
                    img1[h, w, 1] == np.sum(q1)

                if np.sum(q2) > 255:
                    img1[h, w, 2] == 255
                elif np.sum(q2) < 0:
                    img1[h, w, 2] == 0
                else:
                    img1[h, w, 2] == np.sum(q2)

        for ha in range(1, hi-1):
            img1[ha, 0, 0] = img1[ha, 1, 0]
            img1[ha, wi-1, 0] = img1[ha, wi-2, 0]
            img1[ha, 0, 1] = img1[ha, 1, 1]
            img1[ha, wi-1, 1] = img1[ha, wi-2, 1]
            img1[ha, 0, 2] = img1[ha, 1, 2]
            img1[ha, wi-1, 2] = img1[ha, wi-2, 2]
        for wa in range(0, wi):
            img1[0, wa, 0] = img1[1, wa, 0]
            img1[hi-1, wa, 0] = img1[hi-2, wa, 0]
            img1[0, wa, 1] = img1[1, wa, 1]
            img1[hi-1, wa, 1] = img1[hi-2, wa, 1]
            img1[0, wa, 2] = img1[1, wa, 2]
            img1[hi-1, wa, 2] = img1[hi-2, wa, 2]
        for ih in range(0, hi):
            for iw in range(0, wi):
                img[ih][iw][0] = img1[ih][iw][0]
                img[ih][iw][1] = img1[ih][iw][1]
                img[ih][iw][2] = img1[ih][iw][2]
