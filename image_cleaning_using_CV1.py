# -*- coding: utf-8 -*-
"""
Created on Wed Aug 1 13:53:43 2021

@author: user
"""

import cv2
import numpy as np
import os

def back_rm():
    current_path1 = os.getcwd()
    path = os.path.join(r"D:\otimised_poc_ocr\uploads")
    path1 =  os.path.join(r"D:\otimised_poc_ocr\images\\")
    DirPath=os.chdir(path)
    Files=os.listdir(DirPath)
    
    for File in Files:
        DirPath=os.chdir(path)
        # print(File)
        img = cv2.imread(File)
        gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bg = gr.copy()
        for i in range(5):
            kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2 * i + 1, 2 * i + 1))
            bg = cv2.morphologyEx(bg, cv2.MORPH_CLOSE, kernel2)
            bg = cv2.morphologyEx(bg, cv2.MORPH_OPEN, kernel2)

        dif = cv2.subtract(bg, gr)
        bw = cv2.threshold(dif, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        dark = cv2.threshold(bg, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        darkpix = gr[np.where(dark > 0)]

    # Threshold the dark region to get the darker pixels inside it
        darkpix = cv2.threshold(darkpix, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Paste the extracted darker pixels in the watermark region
        bw[np.where(dark > 0)] = darkpix.T
        os.chdir(path1)
        cv2.imwrite("Final_"+File+"", bw)


# back_rm()












