# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 19:16:32 2017

@author: yzsun

Inspired by 
《Multi-Column Deep Neural Networks for Offline Handwritten Chinese Character Classification》

"""
import numpy as np

from PIL import Image
from __future__ import division



class ImagePreprocess():

    def __init__(self,ImageArr):
        self.ImageArr = ImageArr

    # padding, make sure heigth=width
    def padding(self,ImageArr):
        height,width = np.shape(self.ImageArr)
        if height == width:
            return self.ImageArr
        else:
            pad_size = abs(height-width)
            if height < width:
                pad_dims = ((0,0),(pad_size,pad_size))
            else:
                pad_dims = ((pad_size,pad_size),(0,0))
            return np.lib.pad(self.ImageArr,pad_dims,'constant')

    # put image into center,general in the preprocess resize
    def img2center(img_New, img):
        height,width = img.shape
        height_New,width_New = img_New.shape
        
        assert (width_New > width) and (height_New > height)
        
        widthIndex = int((width_New - width) / 2)
        heightIndex = int((height_New - height) / 2)
        img_New[heightIndex:heightIndex + height,
                  widthIndex:widthIndex+width] = img
        return img_New

    # resize
    def resize(self,ImageArr):


    # crop zeros 
    # crop the rows and columns whose elements are all zeros
    def cropZeros(self,ImageArr):
        height_sum = np.sum(ImageArr,axis=0)
        width_sum = np.sum(ImageArr,axis=1)
        return ImageArr[width_sum!=0][:,height_sum!=0]
        
        