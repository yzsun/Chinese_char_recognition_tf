# -*- coding: utf-8 -*-
"""
Created on Wed Jan 04 15:52:10 2017

@author: yzsun
"""

from ImagePreprocess import ImagePreprocess
import numpy as np

class extract_chars_from_ImgArr():
    def __init__(self,ImgArr,minVal,minRange):
        self.ImgArr = ImgArr
        self.minVal = minVal
        self.minRange = minRange

        sum_axis1 = np.sum(self.ImgArr,axis=1)
        ixList_height = self.split_chars_form_ImgArr(sum_axis1,self.minVal,self.minRange)
        
        for start_h, end_h in ixList_height:
            sum_axis0 = np.sum(self.ImgArr[start_h:end_h,:])
            ixList_width = self.split_chars_form_ImgArr(sum_axis0,self.minVal,self.minRange)
            for start_w, end_w in ixList_width:
                charImg = self.ImgArr[start_h:end_h,start_w:end_w]

        
        
    
    def split_chars_form_ImgArr(self,sumArr,minVal,minRange):
        ixList=[]
        start,end = None,None
        for i,val in enumerate(sumArr):
            if val>=minVal and start is None:
                start=i
            if i !=len(sumArr)-1:
                if val<minVal and start is not None and i-start>=minRange:
                    end = i
                    ixList.append([start,end-1])
                    start,end = None,None
            else:
                if start is not None:
                    end = i
                    ixList.append([start,end])
                    del None,None
        return ixList
        