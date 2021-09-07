def gaussfiltering(img):
    import math
    import numpy as np
    import image as img1
    pi = 3.1416
    sigma = 1.823
    a = 0
    b = 0

    hi, wi, ch = img.shape
    img1 = np.zeros((hi, wi, ch), np.uint8)
    g = np.zeros((5, 5), np.float)

    for i in range(0, 5):
        for j in range(0, 5):
            d = ((-1)*((i-2)**2+(j-2)**2))/(2*(sigma**2))
            p = math.exp(d)
            g[i, j] = p/(2*pi*(sigma**2))
    sumg = np.sum(g)

    if ch == 1:
        for h in range(2, hi-2):
            for w in range(2, wi-2):
                q = []
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        G = g[i+2, j+2]*img[h+i, w+j]/sumg
                        q.append(G)

                value = int(np.sum(q))
                img1[h, w] = value

        for ha in range(2, hi-2):
            img1[ha][0] = img1[ha][2]
            img1[ha][1] = img1[ha][2]
            img1[ha][wi-2] = img1[ha][wi-3]
            img1[ha][wi-2] = img1[ha][wi-3]
        for wa in range(0, wi):
            img1[0][wa] = img1[2][wa]
            img1[1][wa] = img1[2][wa]
            img1[hi-1][wa] = img1[hi-3][wa]
            img1[hi-2][wa] = img1[hi-3][wa]
        for ih in range(0, hi):
            for iw in range(0, wi):
                img[ih][iw] = img1[ih][iw]

    if ch == 3:
        for h in range(2, hi-2):
            for w in range(2, wi-2):
                q0 = []
                q1 = []
                q2 = []
                for i in range(-2, 3):
                    for j in range(-2, 3):
                        G0 = g[i+2, j+2]*img[h+i, w+j, 0]/sumg
                        G1 = g[i+2, j+2]*img[h+i, w+j, 1]/sumg
                        G2 = g[i+2, j+2]*img[h+i, w+j, 2]/sumg
                        q0.append(G0)
                        q1.append(G1)
                        q2.append(G2)
                value0 = int(np.sum(q0))
                value1 = int(np.sum(q1))
                value2 = int(np.sum(q2))
                img1[h, w, 0] = value0
                img1[h, w, 1] = value1
                img1[h, w, 2] = value2
        for ha in range(2, hi-2):
            img1[ha][0][0] = img1[ha][2][0]
            img1[ha][1][0] = img1[ha][2][0]
            img1[ha][0][1] = img1[ha][2][1]
            img1[ha][1][1] = img1[ha][2][1]
            img1[ha][0][2] = img1[ha][2][2]
            img1[ha][1][2] = img1[ha][2][2]
            img1[ha][wi-2][0] = img1[ha][wi-3][0]
            img1[ha][wi-1][0] = img1[ha][wi-3][0]
            img1[ha][wi-2][1] = img1[ha][wi-3][1]
            img1[ha][wi-1][1] = img1[ha][wi-3][1]
            img1[ha][wi-2][2] = img1[ha][wi-3][2]
            img1[ha][wi-1][2] = img1[ha][wi-3][2]
        for wa in range(0, wi):
            img1[0][wa][0] = img1[2][wa][0]
            img1[1][wa][0] = img1[2][wa][0]
            img1[0][wa][1] = img1[2][wa][1]
            img1[1][wa][1] = img1[2][wa][1]
            img1[0][wa][2] = img1[2][wa][2]
            img1[1][wa][2] = img1[2][wa][2]
            img1[hi-1][wa][0] = img1[hi-3][wa][0]
            img1[hi-2][wa][0] = img1[hi-3][wa][0]
            img1[hi-1][wa][1] = img1[hi-3][wa][1]
            img1[hi-2][wa][1] = img1[hi-3][wa][1]
            img1[hi-1][wa][2] = img1[hi-3][wa][2]
            img1[hi-2][wa][2] = img1[hi-3][wa][2]
        for ih in range(0, hi):
            for iw in range(0, wi):
                img[ih][iw][0] = img1[ih][iw][0]
                img[ih][iw][1] = img1[ih][iw][1]
                img[ih][iw][2] = img1[ih][iw][2]
