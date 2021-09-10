def sobmask(img):
    import math
    import numpy as np
    import image as img1

    hi, wi, ch = img.shape
    img1 = np.zeros((hi, wi, ch), np.uint8)

    mask1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    mask2 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    if ch == 1:
        for h in range(1, hi-1):
            for w in range(1, wi-1):
                aas = 0
                bbs = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        aas = aas+img[h+i, w+j, 0]*mask1[i+1, j+1]
                        bbs = bbs+img[h+i, w+j, 0]*mask2[i+1, j+1]
                mag = np.sqrt(np.power(aas, 2)+np.power(bbs, 2))

                if mag > 255:
                    img1[h, w] = 255
                elif mag < 0:
                    img1[h, w] = 0
                else:
                    img1[h, w] = int(mag)

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
                aas0 = 0
                bbs0 = 0
                aas1 = 0
                bbs1 = 0
                aas2 = 0
                bbs2 = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        aas0 = aas0+img[h+i, w+j, 0]*mask1[i+1, j+1]
                        bbs0 = bbs0+img[h+i, w+j, 0]*mask2[i+1, j+1]
                        aas1 = aas1+img[h+i, w+j, 1]*mask1[i+1, j+1]
                        bbs1 = bbs1+img[h+i, w+j, 1]*mask2[i+1, j+1]
                        aas2 = aas2+img[h+i, w+j, 2]*mask1[i+1, j+1]
                        bbs2 = bbs2+img[h+i, w+j, 2]*mask2[i+1, j+1]
                mag0 = np.sqrt(np.power(aas0, 2)+np.power(bbs0, 2))
                mag1 = np.sqrt(np.power(aas1, 2)+np.power(bbs1, 2))
                mag2 = np.sqrt(np.power(aas2, 2)+np.power(bbs2, 2))
                if mag0 > 255:
                    img1[h, w, 0] = 255
                else:
                    img1[h, w, 0] = int(mag0)
                if mag1 > 255:
                    img1[h, w, 1] = 255
                else:
                    img1[h, w, 1] = int(mag1)
                if mag2 > 255:
                    img1[h, w, 2] = 255
                else:
                    img1[h, w, 2] = int(mag2)

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
