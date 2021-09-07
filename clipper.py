def clipping(img1):
    import numpy as np
    import math
    import cv2
    heighty, widthx, ch = img1.shape

    if ch == 1:
        rmin = 0
        rmax = 0
        rcount = np.zeros(256, np.uint8)
        for i in range(0, heighty):
            for j in range(0, widthx):
                rcount[int(img1[i][j])] += 1

        countmin = min(rcount)
        countmax = max(rcount)
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
        if rmax-rmin >= 130:
            a = rmin+60
            b = rmax-60
            for i in range(0, heighty):
                for j in range(0, widthx):
                    if img1[i][j] < a:
                        img1[i][j] = 0
                    elif img1[i][j] > b:
                        img1[i][j] = 255

    if ch == 3:
        rmin0 = 0
        rmax0 = 0
        rmin1 = 0
        rmax1 = 0
        rmin2 = 0
        rmax2 = 0
        rcount = np.zeros((3, 256), np.uint8)
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
        if rmax0-rmin0 >= 130:
            a = rmin0+60
            b = rmax0-60
            for i in range(0, heighty):
                for j in range(0, widthx):
                    if img1[i][j][0] < a:
                        img1[i][j][0] = 0
                    elif img1[i][j][0] > b:
                        img1[i][j][0] = 255

        if rmax1-rmin1 >= 130:
            a = rmin1+60
            b = rmax1-60
            for i in range(0, heighty):
                for j in range(0, widthx):
                    if img1[i][j][1] < a:
                        img1[i][j][1] = 0
                    elif img1[i][j][1] > b:
                        img1[i][j][1] = 255

        if rmax2-rmin2 >= 130:
            a = rmin2+60
            b = rmax2-60
            for i in range(0, heighty):
                for j in range(0, widthx):
                    if img1[i][j][2] < a:
                        img1[i][j][2] = 0
                    elif img1[i][j][2] > b:
                        img1[i][j][2] = 255
