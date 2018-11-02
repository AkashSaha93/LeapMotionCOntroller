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

# thumb Finger Position and Direction Axes Initialization
thumbX_axis = np.transpose(np.zeros(length))
thumbY_axis = np.transpose(np.zeros(length))
thumbZ_axis = np.transpose(np.zeros(length))
thumbDirectionX_axis = np.transpose(np.zeros(length))
thumbDirectionY_axis = np.transpose(np.zeros(length))
thumbDirectionZ_axis = np.transpose(np.zeros(length))

#Index Finger Position and Direction Axes Initialization
indexX_axis = np.transpose(np.zeros(length))
indexY_axis = np.transpose(np.zeros(length))
indexZ_axis = np.transpose(np.zeros(length))
indexDirectionX_axis = np.transpose(np.zeros(length))
indexDirectionY_axis = np.transpose(np.zeros(length))
indexDirectionZ_axis = np.transpose(np.zeros(length))


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


# Separating the values from the str to array of separate X,Y,Z values
for i in range(length):
    a = indexData[i]
    a = a[1: -1]
    indexData[i] = a
    b = list(a.split(","))
    indexData_ex = list(indexData[i].split(","))
    indexX_axis[i] = indexData_ex[0]
    indexY_axis[i] = indexData_ex[1]
    indexZ_axis[i] = indexData_ex[2]
   
for j in range(lenDir):
    c = indexDirection[j]
    c = c[1: -1]
    indexDirection[j] = c
    d = list(c.split(","))
    indexDirection_ex = list(indexDirection[j].split(","))
    indexDirectionX_axis[j] = indexDirection_ex[0]
    indexDirectionY_axis[j] = indexDirection_ex[1]
    indexDirectionZ_axis[j] = indexDirection_ex[2]
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


size = int(indexX_axis.shape[0])
length1 = size/4


#getting the metacarpal direction an start position values for the index
indexMetacarpalX_axis = sum(indexX_axis[0:length1])/length1
indexMetacarpalY_axis = sum(indexY_axis[0:length1])/length1
indexMetacarpalZ_axis = sum(indexZ_axis[0:length1])/length1
indexMetaDirectionX_axis = sum(indexDirectionX_axis[0:length1])/length1
indexMetaDirectionY_axis = sum(indexDirectionY_axis[0:length1])/length1
indexMetaDirectionZ_axis = sum(indexDirectionZ_axis[0:length1])/length1
indexMetacarpal = np.hstack((indexMetacarpalX_axis,indexMetacarpalY_axis, indexMetacarpalZ_axis))
indexMetacarpalDirection = np.hstack((indexMetaDirectionX_axis,indexMetaDirectionY_axis,indexMetaDirectionZ_axis))


# Getting the Proximal Bone position and Direction Values for the index
indexProximalX_axis = sum(indexX_axis[length1:(2*length1)])/length1
indexProximalY_axis = sum(indexY_axis[length1:(2*length1)])/length1
indexProximalZ_axis = sum(indexZ_axis[length1:(2*length1)])/length1
indexProxDirectionX_axis = sum(indexDirectionX_axis[length1:(2*length1)])/length1
indexProxDirectionY_axis = sum(indexDirectionY_axis[length1:(2*length1)])/length1
indexProxDirectionZ_axis = sum(indexDirectionZ_axis[length1:(2*length1)])/length1
indexProximal = np.hstack((indexProximalX_axis,indexProximalY_axis, indexProximalZ_axis))
indexProximalDirection = np.hstack((indexProxDirectionX_axis,indexProxDirectionY_axis,indexProxDirectionZ_axis))


# Getting the Intermediate Bone Position and Direction Values for the index
indexInterX_axis = sum(indexX_axis[(2*length1):(3*length1)])/length1
indexInterY_axis = sum(indexY_axis[(2*length1):(3*length1)])/length1
indexInterZ_axis = sum(indexZ_axis[(2*length1):(3*length1)])/length1
indexInterDirectionX_axis = sum(indexDirectionX_axis[(2*length1):(3*length1)])/length1
indexInterDirectionY_axis = sum(indexDirectionY_axis[(2*length1):(3*length1)])/length1
indexInterDirectionZ_axis = sum(indexDirectionZ_axis[(2*length1):(3*length1)])/length1
indexInter = np.hstack((indexInterX_axis, indexInterY_axis, indexInterZ_axis))
indexIntermediateDirection = np.hstack((indexInterDirectionX_axis,indexInterDirectionY_axis,indexInterDirectionZ_axis))



# Getting the Distal Bone Position and Direction Values or the index
indexDistalX_axis = sum(indexX_axis[(3*length1):size])/length1
indexDistalY_axis = sum(indexY_axis[(3*length1):size])/length1
indexDistalZ_axis = sum(indexZ_axis[(3*length1):size])/length1
indexDistDirectionX_axis = sum(indexDirectionX_axis[-3:])/length1
indexDistDirectionY_axis = sum(indexDirectionY_axis[-3:])/length1
indexDistDirectionZ_axis = sum(indexDirectionZ_axis[-3:])/length1
indexDistal = np.hstack((indexDistalX_axis, indexDistalY_axis,indexDistalZ_axis))
indexDistalDirection = np.hstack((indexDistDirectionX_axis, indexDistDirectionY_axis, indexDistDirectionZ_axis))


palmPos = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\palm_position.csv")
posValue = palmPos['0'].tolist()
posLength = len(posValue)   
posValueX_axis = np.transpose(np.zeros(posLength))
posValueY_axis = np.transpose(np.zeros(posLength))
posValueZ_axis = np.transpose(np.zeros(posLength))

for k in range(posLength):
    c = posValue[k]
    c = c[1: -1]
    posValue[k] = c
    d = list(c.split(","))
    posValue_ex = list(posValue[k].split(","))
    posValueX_axis[k] = posValue_ex[0]
    posValueY_axis[k] = posValue_ex[1]
    posValueZ_axis[k] = posValue_ex[2]
    
posX_axis = sum(posValueX_axis[0:posLength])/posLength
posY_axis = sum(posValueY_axis[0:posLength])/posLength
posZ_axis = sum(posValueZ_axis[0:posLength])/posLength
pos = np.hstack((posX_axis, posY_axis, posZ_axis))

# Computing the Euclidean Distance between the Palm and the Thumb Bones
palmThumbMetadist = np.linalg.norm(thumbMetacarpal - pos)
palmThumbProxidist = np.linalg.norm(thumbProximal - pos)
palmThumbInterdist = np.linalg.norm(thumbInter - pos)
palmThumbDistdist = np.linalg.norm(thumbDistal - pos)

# Computing the Euclidean Distance between the Palm and the Index Finger Bones
palmIndexMetadist = np.linalg.norm(indexMetacarpal - pos)
palmIndexProxidist = np.linalg.norm(indexProximal - pos)
palmIndexInterdist = np.linalg.norm(indexInter - pos)
palmIndexDistdist = np.linalg.norm(indexDistal - pos)


