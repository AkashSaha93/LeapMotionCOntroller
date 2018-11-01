# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:22:03 2018

@author: as7933
"""

import pandas as pd
import numpy as np

# Getting the csv dataread for Thumb
dataThumb = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\thumb.csv")
thumbData = dataThumb['Data'].tolist()
thumbDirection = dataThumb['Direction'].tolist()

# Reading csv Data for Index Finger
dataindex = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\index.csv")
indexData = dataindex['Data'].tolist()
indexDirection = dataindex['Direction'].tolist()

length = len(thumbData)
lenDir = len(thumbDirection)
#dataLen = length/4
thumbX_axis = np.transpose(np.zeros(length))
thumbY_axis = np.transpose(np.zeros(length))
thumbZ_axis = np.transpose(np.zeros(length))

thumbDirectionX_axis = np.transpose(np.zeros(length))
thumbDirectionY_axis = np.transpose(np.zeros(length))
thumbDirectionZ_axis = np.transpose(np.zeros(length))


# Separating the values from the str to array of separate X,Y,Z values
for i in range(length):
    a = thumbData[i]
    a = a[1: -1]
    thumbData[i] = a
    b = list(a.split(","))
    thumbData_ex = list(thumbData[i].split(","))
    thumbX_axis[i] = thumbData_ex[0]
    thumbY_axis[i] = thumbData_ex[1]
    thumbZ_axis[i] = thumbData_ex[2]
   
for j in range(lenDir):
    c = thumbDirection[j]
    c = c[1: -1]
    thumbDirection[j] = c
    d = list(c.split(","))
    thumbDirection_ex = list(thumbDirection[j].split(","))
    thumbDirectionX_axis[j] = thumbDirection_ex[0]
    thumbDirectionY_axis[j] = thumbDirection_ex[1]
    thumbDirectionZ_axis[j] = thumbDirection_ex[2]

size = int(thumbX_axis.shape[0])
length1 = size/4


#getting the metacarpal direction an start position values for the thumb
thumbMetacarpalX_axis = sum(thumbX_axis[0:length1])/length1
thumbMetacarpalY_axis = sum(thumbY_axis[0:length1])/length1
thumbMetacarpalZ_axis = sum(thumbZ_axis[0:length1])/length1
thumbMetaDirectionX_axis = sum(thumbDirectionX_axis[0:length1])/length1
thumbMetaDirectionY_axis = sum(thumbDirectionY_axis[0:length1])/length1
thumbMetaDirectionZ_axis = sum(thumbDirectionZ_axis[0:length1])/length1
thumbMetacarpal = np.hstack((thumbMetacarpalX_axis,thumbMetacarpalY_axis, thumbMetacarpalZ_axis))
thumbMetacarpalDirection = np.hstack((thumbMetaDirectionX_axis,thumbMetaDirectionY_axis,thumbMetaDirectionZ_axis))


# Getting the Proximal Bone position and Direction Values for the Thumb
thumbProximalX_axis = sum(thumbX_axis[length1:(2*length1)])/length1
thumbProximalY_axis = sum(thumbY_axis[length1:(2*length1)])/length1
thumbProximalZ_axis = sum(thumbZ_axis[length1:(2*length1)])/length1
thumbProxDirectionX_axis = sum(thumbDirectionX_axis[length1:(2*length1)])/length1
thumbProxDirectionY_axis = sum(thumbDirectionY_axis[length1:(2*length1)])/length1
thumbProxDirectionZ_axis = sum(thumbDirectionZ_axis[length1:(2*length1)])/length1
thumbProximal = np.hstack((thumbProximalX_axis,thumbProximalY_axis, thumbProximalZ_axis))
thumbProximalDirection = np.hstack((thumbProxDirectionX_axis,thumbProxDirectionY_axis,thumbProxDirectionZ_axis))


# Getting the Intermediate Bone Position and Direction Values for the thumb
thumbInterX_axis = sum(thumbX_axis[(2*length1):(3*length1)])/length1
thumbInterY_axis = sum(thumbY_axis[(2*length1):(3*length1)])/length1
thumbInterZ_axis = sum(thumbZ_axis[(2*length1):(3*length1)])/length1
thumbInterDirectionX_axis = sum(thumbDirectionX_axis[(2*length1):(3*length1)])/length1
thumbInterDirectionY_axis = sum(thumbDirectionY_axis[(2*length1):(3*length1)])/length1
thumbInterDirectionZ_axis = sum(thumbDirectionZ_axis[(2*length1):(3*length1)])/length1
thumbInter = np.hstack((thumbInterX_axis, thumbInterY_axis, thumbInterZ_axis))
thumbIntermediateDirection = np.hstack((thumbInterDirectionX_axis,thumbInterDirectionY_axis,thumbInterDirectionZ_axis))



# Getting the Distal Bone Position and Direction Values or the Thumb
thumbDistalX_axis = sum(thumbX_axis[(3*length1):size])/length1
thumbDistalY_axis = sum(thumbY_axis[(3*length1):size])/length1
thumbDistalZ_axis = sum(thumbZ_axis[(3*length1):size])/length1
thumbDistDirectionX_axis = sum(thumbDirectionX_axis[-3:])/length1
thumbDistDirectionY_axis = sum(thumbDirectionY_axis[-3:])/length1
thumbDistDirectionZ_axis = sum(thumbDirectionZ_axis[-3:])/length1
thumbDistal = np.hstack((thumbDistalX_axis, thumbDistalY_axis,thumbDistalZ_axis))
thumbDistalDirection = np.hstack((thumbDistDirectionX_axis, thumbDistDirectionY_axis, thumbDistDirectionZ_axis))


#palmPos = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\palm_position.csv")
