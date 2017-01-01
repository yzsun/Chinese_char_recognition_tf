# -*- coding: utf-8 -*-
"""
Created on Sun Jan 01 19:16:32 2017

@author: Administrator
"""
import numpy as np

from PIL import Image
from __future__ import division



class preProcess():
    # padding to make heigth=width
    def __init__(self,ImageArr):
        self.ImageArr = ImageArr
    
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
        