# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 11:35:12 2016
@author: yzsun
1.探索数据格式；
2.查看各图片缩略图（缩略图简易查看，尝试过windows 和 ubuntu）
3.训练集：HWDB1.1trn_gnt
    240个.gnt文件(1001-c.gnt ~ 1240-c.gnt)
    6081张训练图，903个字
4.测试集：HWDB1.1tst_gnt
    60个.gnt文件(1241-c.gnt ~ 1399-c.gnt)
    1174张测试图，402个字

"""

import numpy as np
import os
from PIL import Image
import struct

def Browser(dir):
    headSize = 10
    label2count = {} # count number of every Chinese character 
    imageCount = 0 # different from labelCount
    for file in os.listdir(dir+'/gnt/'):
        if file.endswith('.gnt'):
            filepath = os.path.join(dir,'gnt',file)
            with open(filepath) as curFile:
                while True:
                    # head
                    head = np.fromfile(curFile, dtype='uint8', count=headSize) #type:1Darray; len:10
                    if head.size != 10:
                        break
                    sampleSize = head[0] + (head[1]<<8) + (head[2]<<16) + (head[3]<<24) #LH
                    label = struct.pack('>H',head[5] + (head[4]<<8)).decode('gb2312') #HL
                    width = head[6] + (head[7]<<8) #LH
                    height = head[8] + (head[9]<<8) #LH
                    imageSize = width*height
                    assert sampleSize == imageSize + headSize
                    # image
                    image_1Darr = np.fromfile(curFile,dtype='uint8',count=width*height)
                    if image_1Darr.size != imageSize:
                        break
                    imageArr = image_1Darr.reshape((height,width))
                    image = Image.fromarray(imageArr) #type:Image
                    # statistics
                    if label in label2count:
                        label2count[label] +=1
                    else:
                        label2count[label] = 1
                    imageCount +=1

                    # save image
                    imSavePath = dir+'/imageCat'
                    if not os.path.exists(imSavePath):
                        os.makedirs(imSavePath)
                    image.save(os.path.join(imSavePath,label+str(label2count[label])+"_"+str(imageCount)+'.png'))
    return label2count,imageCount

trDir = './data/HWDB1.1trn_gnt'
teDir = './data/HWDB1.1tst_gnt'
if __name__=="__main__":
    for dir in [trDir,teDir]:
        label2count,imageCount = Browser(teDir)
        print('######'+dir+'######')
        print('Chinese character numbers:',len(label2count))
        print('Iamge numbers:',imageCount)

