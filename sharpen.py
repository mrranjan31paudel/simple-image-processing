def sharpening(img1):
    import cv2
    import math
    import numpy as np
    import image as img2
    heighty, widthx, ch = img1.shape
    img2 = np.zeros((heighty, widthx, ch), np.uint8)
    if ch == 1:
        for i in range(0, heighty):
            for j in range(0, widthx):
                Lap_filt = int(img1[i][j])
                if i > 0 and i < heighty-1:
                    if j > 0 and j < widthx-1:
                        Lap_filt = img1[i-1][j-1]+img1[i+1][j+1]+img1[i+1][j-1]+img1[i-1][j+1] + \
                            img1[i+1][j] + img1[i-1][j] + \
                            img1[i][j+1] + img1[i][j-1] - 8*img1[i][j]
                        if img1[i][j]-Lap_filt > 255:
                            img2[i][j] = 255
                        elif img1[i][j]-Lap_filt < 0:
                            img2[i][j] = 0
                        else:
                            img2[i][j] = img1[i][j]-Lap_filt
                else:
                    img2[i][j] = Lap_filt

        for inew in range(0, heighty):
            for jnew in range(0, widthx):
                img1[inew][jnew] = img2[inew][jnew]
