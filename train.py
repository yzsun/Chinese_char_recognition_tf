# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 19:58:09 2017

@author: yzsun
"""
from __future__ import division
import numpy as np
import cv2
from extractChars import extract_chars_from_ImgArr
from ImagePreprocess import ImagePreprocess






img = cv2.imread('test_data.png')


preprocess = ImagePreprocess(img)
resizedImg = preprocess.resize_keepRatio(img,(1024,1024))
grayImg = cv2.cvtColor(resizedImg, cv2.COLOR_RGB2GRAY)#RGB-->Gray

adaptive_threshold = cv2.adaptiveThreshold(  #二值化，binarization
    grayImg,
    255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY, 11, 2)
adaptive_threshold = 255 - adaptive_threshold #反转


charImg = extract_chars_from_ImgArr(adaptive_threshold)
imgs = charImg.charImgs


