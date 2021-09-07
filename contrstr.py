def normalization(img1):
    import numpy as np
    import math
    import cv2
    import image as img2
    heighty, widthx, ch = img1.shape

    img2 = np.zeros((heighty, widthx, ch), np.uint8)
    Imax = 285
    Imin = -30
    Idif = Imax-Imin

    if ch == 1:
        rmin = 0
        rmax = 0
        rcount = np.zeros(256, np.uint8)
        news = np.zeros(256, np.uint8)
        for i in range(0, heighty):
            for j in range(0, widthx):
                rcount[img1[i][j]] += 1

        countmin = np.min(rcount)
        countmax = np.max(rcount)
        flagmin = 1
        flagmax = 1
        for levels in range(0, 256):
            if rcount[levels] > 0 and flagmin == 1:
                rmin = levels
                flagmin = 0
            if rcount[255-levels] > 0 and flagmax == 1:
                rmax = 255-levels
                flagmax = 0
            if flagmin == 0 and flagmax == 0:
                break
        if rmax < Imax or rmin > Imin:
            rdif = rmax-rmin
            for r in range(rmin, rmax+1):
                sub = Idif*(r-rmin)/rdif+Imin
                if sub > 255:
                    sub = 255
                if sub < 0:
                    sub = 0
                s = int(round(sub, 0))
                news[r] = s

            for i in range(0, heighty):
                for j in range(0, widthx):
                    img1[i][j] = news[img1[i][j]]

    if ch == 3:
        rmin0 = 0
        rmax0 = 0
        rmin1 = 0
        rmax1 = 0
        rmin2 = 0
        rmax2 = 0
        rcount = np.zeros((3, 256), np.uint8)
        news = np.zeros((3, 256), np.uint8)
        flagmin = np.zeros(3, np.uint8)
        flagmax = np.zeros(3, np.uint8)

        for i in range(0, heighty):
            for j in range(0, widthx):
                rcount[0][int(img1[i][j][0])] += 1
                rcount[1][int(img1[i][j][1])] += 1
                rcount[2][int(img1[i][j][2])] += 1

        countmin0 = min(rcount[0])
        countmax0 = max(rcount[0])
        countmin1 = min(rcount[1])
        countmax1 = max(rcount[1])
        countmin2 = min(rcount[2])
        countmax2 = max(rcount[2])
        flagmin[0] = 1
        flagmax[0] = 1
        flagmin[1] = 1
        flagmax[1] = 1
        flagmin[2] = 1
        flagmax[2] = 1
        for levels in range(0, 256):
            if rcount[0][levels] > 0 and flagmin[0] == 1:
                rmin0 = levels
                flagmin[0] = 0
            if rcount[0][255-levels] > 0 and flagmax[0] == 1:
                rmax0 = 255-levels
                flagmax[0] = 0
            if rcount[1][levels] > 0 and flagmin[1] == 1:
                rmin1 = levels
                flagmin[1] = 0
            if rcount[1][255-levels] > 0 and flagmax[1] == 1:
                rmax1 = 255-levels
                flagmax[1] = 0
            if rcount[2][levels] > 0 and flagmin[2] == 1:
                rmin2 = levels
                flagmin[2] = 0
            if rcount[2][255-levels] > 0 and flagmax[2] == 1:
                rmax2 = 255-levels
                flagmax[2] = 0
            if np.sum(flagmin) == 0 and np.sum(flagmax) == 0:
                break
        if rmax0 < Imax or rmin0 > Imin:
            rdif0 = rmax0-rmin0
            for r0 in range(rmin0, rmax0+1):
                sub0 = Idif*(r0-rmin0)/rdif0+Imin
                if sub0 > 255:
                    sub0 = 255
                if sub0 < 0:
                    sub0 = 0
                s0 = int(round(sub0, 0))
                news[0, r0] = s0
            for i in range(0, heighty):
                for j in range(0, widthx):
                    img1[i][j][0] = news[0, img1[i][j][0]]
        if rmax1 < Imax or rmin1 > Imin:
            rdif1 = rmax1-rmin1
            for r1 in range(rmin1, rmax1+1):
                sub1 = Idif*(r1-rmin1)/rdif1+Imin
                if sub1 > 255:
                    sub1 = 255
                if sub1 < 0:
                    sub1 = 0
                s1 = int(round(sub1, 0))
                news[1, r1] = s1
            for i in range(0, heighty):
                for j in range(0, widthx):
                    img1[i][j][1] = news[1, img1[i][j][1]]
        if rmax2 < Imax or rmin2 > Imin:
            rdif2 = rmax2-rmin2
            for r2 in range(rmin2, rmax2+1):
                sub2 = Idif*(r2-rmin2)/rdif2+Imin
                if sub2 > 255:
                    sub2 = 255
                if sub2 < 0:
                    sub2 = 0
                s2 = int(round(sub2, 0))
                news[2, r2] = s2
            for i in range(0, heighty):
                for j in range(0, widthx):
                    img1[i][j][2] = news[2, img1[i][j][2]]
