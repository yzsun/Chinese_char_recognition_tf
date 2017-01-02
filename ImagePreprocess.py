# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 19:16:32 2017

@author: Administrator
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
    # resize
    def resize(self,ImageArr):
        
    # crop zeros 
    # crop the rows and columns whose elements are all zeros
    def cropZeros(self,ImageArr):
        height_sum = np.sum(ImageArr,axis=0)
        width_sum = np.sum(ImageArr,axis=1)
        return ImageArr[width_sum!=0][:,height_sum!=0]
        
        