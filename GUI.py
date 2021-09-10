import os  # def starter():
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import Menu
from PIL import Image, ImageTk
import image
import cv2 as cv
import numpy as np

from config import *

newWin = tk.Tk()
imgicon = ImageTk.PhotoImage(file=ICON_FILE)
newWin.title("Color Image Processing")
newWinht = newWin.winfo_screenheight()
newWinwd = newWin.winfo_screenwidth()
newWin.geometry(("%dx%d") % (newWinwd, newWinht))
newWin.tk.call('wm', 'iconphoto', newWin._w, imgicon)


class design:
    fileName = ""
    heighty = int
    widthx = int
    ch = int
    relcount = 0
    img = image
    size_of = []

    frame1 = tk.Frame(newWin, highlightbackground="green",
                      highlightcolor="green", highlightthickness=1, bg="white",
                      width="400", height="300", colormap="new", bd="0")
    frame1.place(x=445, y=21)
    frame1.pack_propagate(0)

    frame3 = tk.Frame(newWin, highlightbackground="green",
                      highlightcolor="green", highlightthickness=1, bg="white",
                      width="400", height="300", colormap="new", bd="0")
    frame3.place(x=5, y=21)
    frame3.pack_propagate(0)

    frame2 = tk.Frame(newWin, highlightbackground="green",
                      highlightcolor="green", highlightthickness=1, bg="light gray",
                      width="800", height="335", colormap="new", bd="0")
    frame2.place(x=5, y=351)
    frame2.pack_propagate(0)

    frame4 = tk.Frame(newWin, highlightbackground="green",
                      highlightcolor="green", highlightthickness=1, bg="white",
                      width="300", height="300", colormap="new", bd="0")
    frame4.place(x=935, y=21)
    frame4.pack_propagate(0)

    frame5 = tk.Frame(newWin, highlightbackground="green",
                      highlightcolor="green", highlightthickness=1, bg="white",
                      width="300", height="300", colormap="new", bd="0")
    frame5.place(x=935, y=351)
    frame5.pack_propagate(0)

    L = tk.Label(frame1, bg="white", fg="green",
                 text="(Your processed image appears here)")
    L.pack()

    L13 = tk.Label(frame3, bg="white", fg="green",
                   text="(Your original image appears here)")
    L13.pack()

    L11 = tk.Label(newWin, fg="black", text="Original Image:")
    L11.place(x=5, y=0)
    L11.pack_propagate(0)

    L12 = tk.Label(newWin, fg="black", text="Processed Image:")
    L12.place(x=445, y=0)
    L12.pack_propagate(0)

    L14 = tk.Label(newWin, fg="black", text="Magnitude Plot:")
    L14.place(x=935, y=0)
    L14.pack_propagate(0)

    L1 = tk.Label(newWin, fg="black", text="Normalized Histogram:")
    L1.place(x=5, y=330)
    L1.pack_propagate(0)

    L15 = tk.Label(newWin, fg="black", text="Phase Plot:")
    L15.place(x=935, y=330)
    L15.pack_propagate(0)

    L3 = tk.Label(frame2, bg="light gray", fg="blue", text="1")
    L3.place(x=3, y=0)
    L3.pack_propagate(0)

    L4 = tk.Label(frame2, bg="light gray", fg="blue", text="0")
    L4.place(x=3, y=308)
    L4.pack_propagate(0)

    L5 = tk.Label(frame2, bg="light gray", fg="blue", text="255")
    L5.place(x=770, y=308)
    L5.pack_propagate(0)

    L6 = tk.Label(frame2, bg="light gray", fg="blue", text="Intensity Levels")
    L6.place(x=int(800/3), y=308)
    L6.pack_propagate(0)

    L7 = tk.Label(frame2, bg="light gray", fg="blue",
                  text="Probability", wraplength=1)
    L7.place(x=0, y=int(330/4))
    L7.pack_propagate(0)

    L2 = tk.Label(frame2, bg="light gray", text=" ")
    L2.place(x=16, y=6)
    L2.pack_propagate(0)


def design_fun():
    menubar = Menu(newWin)
    # FILE
    filedrop = Menu(menubar, tearoff=0)
    filedrop.add_command(label="Open", command=lambda: openi(design.fileName))
    filedrop.add_command(label="Save", command=save)
    filedrop.add_separator()
    filedrop.add_command(label="Exit", command=exitfun)
    menubar.add_cascade(label="File", menu=filedrop)
    # EDIT
    sptdom = Menu(menubar, tearoff=0)
    sptdom.add_command(label="Grayscale", command=grayconv)
    sptdom.add_separator()
    filtersel = Menu(sptdom, tearoff=0)  # Filters
    filtersel.add_command(label="Median", command=median)
    filtersel.add_command(label="Mean", command=mean)
    filtersel.add_command(label="Weighted Mean", command=wtmean)
    filtersel.add_command(label="Min", command=mini)
    filtersel.add_command(label="Max", command=maxi)
    filtersel.add_command(label="Gaussian", command=gauss)
    sptdom.add_cascade(label="Filters", menu=filtersel)

    enhancsel = Menu(sptdom, tearoff=0)  # Enhancements
    enhancsel.add_command(label="Contrast Stretching", command=contstrt)
    enhancsel.add_command(label="Clipping", command=clipp)
    enhancsel.add_command(label="Sharpening", command=sharpe)
    sptdom.add_cascade(label="Enahancements", menu=enhancsel)

    transel = Menu(sptdom, tearoff=0)  # Transformation
    transel.add_command(label="Negative", command=neget)
    transel.add_command(label="Logarithmic", command=logtr)
    transel.add_command(label="Power", command=powe)
    sptdom.add_cascade(label="Transformations", menu=transel)

    transel = Menu(sptdom, tearoff=0)  # Derivative filter
    transel.add_command(label="Prewitt", command=prewit)
    transel.add_command(label="Sobel", command=sobel)
    transel.add_command(label="Laplacian", command=lapla)
    sptdom.add_cascade(label="Derivative filter", menu=transel)

    sptdom.add_separator()
    sptdom.add_command(label="Binarize", command=bnrize)
    menubar.add_cascade(label="Spatial Domain", menu=sptdom)

    freqdom = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Frequency Domain", menu=freqdom)

    newWin.config(menu=menubar)

    but1 = tk.Button(newWin, text="Red", fg="red",
                     command=lambda: histogram(2))
    but1.place(x=806, y=371)
    but2 = tk.Button(newWin, text="Green", fg="green",
                     command=lambda: histogram(1))
    but2.place(x=806, y=398)
    but3 = tk.Button(newWin, text="Blue", fg="blue",
                     command=lambda: histogram(0))
    but3.place(x=806, y=425)

    but11 = tk.Button(newWin, text="Red", fg="red")
    but11.place(x=1236, y=21)
    but22 = tk.Button(newWin, text="Green", fg="green")
    but22.place(x=1236, y=48)
    but33 = tk.Button(newWin, text="Blue", fg="blue")
    but33.place(x=1236, y=75)

    but111 = tk.Button(newWin, text="Red", fg="red")
    but111.place(x=1236, y=371)
    but222 = tk.Button(newWin, text="Green", fg="green")
    but222.place(x=1236, y=398)
    but333 = tk.Button(newWin, text="Blue", fg="blue")
    but333.place(x=1236, y=425)

    butreload = tk.Button(newWin, text="Reload", fg="black", command=relod)
    butreload.place(x=846, y=21)


def openi(name):
    design.fileName = name
    newName = filedialog.askopenfilename(filetypes=(("JPEG", "*.jpg"),
                                                    ("PNG", "*.png"),
                                                    ("All Files", "*.*")))
    if newName:
        design.fileName = newName
        if name == newName:
            name = ""
    design.heighty = 0
    design.widthx = 0
    design.ch = 0
    if design.fileName != "" and design.fileName != name:
        design.img = cv.imread(design.fileName)
        design.heighty, design.widthx, design.ch = design.img.shape
        img1 = Image.open(design.fileName)
        ph1 = resize_img(img1, design.widthx, design.heighty)
        ph = ImageTk.PhotoImage(ph1)

        design.L.pack_forget()
        design.frame1.update()

        design.L13.pack_forget()
        design.frame3.update()

        if design.heighty > 300 or design.widthx > 400:
            design.heighty = design.size_of[1]
            design.widthx = design.size_of[0]
            design.img = cv.resize(
                design.img, (design.widthx, design.heighty), interpolation=cv.INTER_CUBIC)
            design.size_of = []

        design.L = tk.Label(design.frame1, image=ph)
        design.L.image = ph
        design.L.pack()

        design.L13 = tk.Label(design.frame3, image=ph)
        design.L13.image = ph
        design.L13.pack()


def relod():
    if design.fileName != "" and design.relcount > 0:
        design.img = cv.imread(design.fileName)
        design.heighty, design.widthx, design.ch = design.img.shape
        img1 = Image.open(design.fileName)
        ph1 = resize_img(img1, design.widthx, design.heighty)
        ph = ImageTk.PhotoImage(ph1)

        design.L.pack_forget()
        design.frame1.update()

        design.L13.pack_forget()
        design.frame3.update()

        if design.heighty > 300 or design.widthx > 400:
            design.heighty = design.size_of[1]
            design.widthx = design.size_of[0]
            design.img = cv.resize(
                design.img, (design.widthx, design.heighty), interpolation=cv.INTER_CUBIC)
            design.size_of = []

        design.L = tk.Label(design.frame1, image=ph)
        design.L.image = ph
        design.L.pack()

        design.L13 = tk.Label(design.frame3, image=ph)
        design.L13.image = ph
        design.L13.pack()
        design.relcount = 0


def save():
    if design.fileName != "":
        ph = prepare_display_image(design.img)
        f = filedialog.asksaveasfile(mode='wb')
        if f:
            ph.save(f)
            f.close()


def exitfun():
    sys.exit()


def grayconv():
    if design.fileName != "":
        import gray
        import image as img1
        hi, wi, ch = design.img.shape
        img1 = gray.grayscale(design.img)
        design.img = None
        design.img = img1
        hi, wi, ch = design.img.shape
        tup = (wi, hi)
        pi = Image.frombytes("L", tup, design.img.tobytes())
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def bnrize():
    if design.fileName != "":
        import binarize
        import image as img1
        hi, wi, ch = design.img.shape
        img1 = binarize.binarization(design.img)
        design.img = None
        design.img = img1
        hi, wi, ch = design.img.shape
        tup = (wi, hi)
        pi = Image.frombytes("L", tup, design.img.tobytes())
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def median():
    if design.fileName != "":
        import medianfil

        medianfil.noisered(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def mean():
    if design.fileName != "":
        import meanfil

        meanfil.meanfiltering(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def wtmean():
    if design.fileName != "":
        import weightmeanfil

        weightmeanfil.wtmeanfiltering(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def maxi():
    if design.fileName != "":
        import maxfil

        maxfil.maxfiltering(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def mini():
    if design.fileName != "":
        import minfil

        minfil.minfiltering(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def gauss():
    if design.fileName != "":
        import gaussfil

        gaussfil.gaussfiltering(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def prewit():
    if design.fileName != "":
        import prewittmask as prewt

        prewt.premask(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def sobel():
    if design.fileName != "":
        import sobelmask as sobl

        sobl.sobmask(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def lapla():
    if design.fileName != "":
        import laplacianmask

        laplacianmask.lapmask(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def neget():
    if design.fileName != "":
        import negativeen as neg

        neg.negation(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def logtr():
    if design.fileName != "":
        import logger

        logger.logging(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def powe():
    if design.fileName != "":
        import powertr

        powertr.powring(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def contstrt():
    if design.fileName != "":
        import contrstr

        contrstr.normalization(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def sharpe():
    if design.fileName != "":
        import sharpen

        sharpen.sharpening(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def clipp():
    if design.fileName != "":
        import clipper

        clipper.clipping(design.img)
        pi = prepare_display_image(design.img)
        update_display_image(pi)
    else:
        update_for_no_image()
    design.relcount += 1


def histogram(chval):
    if design.fileName != "":
        import histo
        import image as img1
        img1 = histo.histoplot(design.img, chval)
        hi, wi, ch = img1.shape
        tup = (wi, hi)
        if ch == 1:
            pi = Image.frombytes("L", tup, img1.tobytes())
        else:
            for i in range(0, hi):
                for j in range(0, wi):
                    temp = img1[i][j][0]
                    img1[i][j][0] = img1[i][j][2]
                    img1[i][j][2] = temp
            pi = Image.frombytes("RGB", tup, img1.tobytes())

        ph = ImageTk.PhotoImage(pi)
        design.L2.pack_forget()
        design.frame2.update()
        design.L2 = tk.Label(design.frame2, image=ph)
        design.L2.image = ph
        design.L2.place(x=16, y=6)
        design.L2.pack_propagate(0)

    else:
        design.L2.pack_forget()
        design.frame2.update()
        design.L2 = tk.Label(design.frame2, bg="white",
                             fg="red", text="Please select an image to proceed!")
        design.L2.place(x=16, y=6)
        design.L2.pack_propagate(0)


def resize_img(img, widthx, heighty):
    th = heighty
    tw = widthx
    if ((heighty > 300) or (widthx > 400)):
        if widthx/heighty >= 400/300:
            r = widthx/heighty
            w = 400
            h = int(w/r)
        else:
            r = heighty/widthx
            h = 300
            w = int(h/r)
        img = img.resize((w, h), Image.ANTIALIAS)
        design.size_of.append(w)
        design.size_of.append(h)
    return img


def prepare_display_image(img):
    hi, wi, ch = img.shape
    img1 = np.zeros((hi, wi, ch), np.uint8)
    mode = "L"

    if ch == 1:
        for i in range(0, hi):
            for j in range(0, wi):
                img1[i][j] = img[i][j]
    else:
        mode = "RGB"
        for i in range(0, hi):
            for j in range(0, wi):
                img1[i][j][0] = img[i][j][2]
                img1[i][j][1] = img[i][j][1]
                img1[i][j][2] = img[i][j][0]

    return Image.frombytes(mode, (wi, hi), img1.tobytes())


def update_display_image(pi):
    ph = ImageTk.PhotoImage(pi)
    design.L.pack_forget()
    design.frame1.update()
    design.L = tk.Label(design.frame1, image=ph)
    design.L.image = ph
    design.L.pack()


def update_for_no_image():
    design.L.pack_forget()
    design.frame1.update()
    design.L = tk.Label(design.frame1, bg="white", fg="red",
                        text="Please select an image to proceed!")
    design.L.pack()


if __name__ == "__main__":
    design_fun()
    newWin.mainloop()
