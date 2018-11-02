# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:22:03 2018

@author: as7933
"""

import pandas as pd
import numpy as np

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













    
###############################################################################################
# THUMB FINGER
###############################################################################################

# Getting the csv dataread for Thumb
dataThumb = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\thumb.csv")
thumbData = dataThumb['Data'].tolist()
thumbDirection = dataThumb['Direction'].tolist()

length = len(thumbData)
lenDir = len(thumbDirection)

# thumb Finger Position and Direction Axes Initialization
thumbX_axis = np.transpose(np.zeros(length))
thumbY_axis = np.transpose(np.zeros(length))
thumbZ_axis = np.transpose(np.zeros(length))
thumbDirectionX_axis = np.transpose(np.zeros(length))
thumbDirectionY_axis = np.transpose(np.zeros(length))
thumbDirectionZ_axis = np.transpose(np.zeros(length))

# Separating the values from the str to array of separate X,Y,Z values for THUMB
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

# Computing the Euclidean Distance between the Palm and the Thumb Bones
palmThumbMetadist = np.linalg.norm(thumbMetacarpal - pos)
palmThumbProxidist = np.linalg.norm(thumbProximal - pos)
palmThumbInterdist = np.linalg.norm(thumbInter - pos)
palmThumbDistdist = np.linalg.norm(thumbDistal - pos)




###############################################################################################
# INDEX FINGER
###############################################################################################

# Reading csv Data for Index Finger
dataindex = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\index.csv")
indexData = dataindex['Data'].tolist()
indexDirection = dataindex['Direction'].tolist()

# Index Finger Position and Direction Axes Initialization
indexX_axis = np.transpose(np.zeros(length))
indexY_axis = np.transpose(np.zeros(length))
indexZ_axis = np.transpose(np.zeros(length))
indexDirectionX_axis = np.transpose(np.zeros(length))
indexDirectionY_axis = np.transpose(np.zeros(length))
indexDirectionZ_axis = np.transpose(np.zeros(length))

# Separating the values from the str to array of separate X,Y,Z values for INDEX
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

# Computing the Euclidean Distance between the Palm and the Index Finger Bones
palmIndexMetadist = np.linalg.norm(indexMetacarpal - pos)
palmIndexProxidist = np.linalg.norm(indexProximal - pos)
palmIndexInterdist = np.linalg.norm(indexInter - pos)
palmIndexDistdist = np.linalg.norm(indexDistal - pos)




###############################################################################################
# MIDDLE FINGER
###############################################################################################

# Reading csv Data for Middle Finger
datamiddle = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\middle.csv")
middleData = datamiddle['Data'].tolist()
middleDirection = datamiddle['Direction'].tolist()

# Middle Finger Position and Direction Axes Initialization
middleX_axis = np.transpose(np.zeros(length))
middleY_axis = np.transpose(np.zeros(length))
middleZ_axis = np.transpose(np.zeros(length))
middleDirectionX_axis = np.transpose(np.zeros(length))
middleDirectionY_axis = np.transpose(np.zeros(length))
middleDirectionZ_axis = np.transpose(np.zeros(length))

# Separating the values from the str to array of separate X,Y,Z values for MIDDLE
for i in range(length):
    a = middleData[i]
    a = a[1: -1]
    middleData[i] = a
    b = list(a.split(","))
    middleData_ex = list(middleData[i].split(","))
    middleX_axis[i] = middleData_ex[0]
    middleY_axis[i] = middleData_ex[1]
    middleZ_axis[i] = middleData_ex[2]
   
for j in range(lenDir):
    c = middleDirection[j]
    c = c[1: -1]
    middleDirection[j] = c
    d = list(c.split(","))
    middleDirection_ex = list(middleDirection[j].split(","))
    middleDirectionX_axis[j] = middleDirection_ex[0]
    middleDirectionY_axis[j] = middleDirection_ex[1]
    middleDirectionZ_axis[j] = middleDirection_ex[2]


size = int(middleX_axis.shape[0])
length1 = size/4

# getting the metacarpal direction an start position values for the middle
middleMetacarpalX_axis = sum(middleX_axis[0:length1])/length1
middleMetacarpalY_axis = sum(middleY_axis[0:length1])/length1
middleMetacarpalZ_axis = sum(middleZ_axis[0:length1])/length1
middleMetaDirectionX_axis = sum(middleDirectionX_axis[0:length1])/length1
middleMetaDirectionY_axis = sum(middleDirectionY_axis[0:length1])/length1
middleMetaDirectionZ_axis = sum(middleDirectionZ_axis[0:length1])/length1
middleMetacarpal = np.hstack((middleMetacarpalX_axis,middleMetacarpalY_axis, middleMetacarpalZ_axis))
middleMetacarpalDirection = np.hstack((middleMetaDirectionX_axis,middleMetaDirectionY_axis,middleMetaDirectionZ_axis))

# Getting the Proximal Bone position and Direction Values for the middle
middleProximalX_axis = sum(middleX_axis[length1:(2*length1)])/length1
middleProximalY_axis = sum(middleY_axis[length1:(2*length1)])/length1
middleProximalZ_axis = sum(middleZ_axis[length1:(2*length1)])/length1
middleProxDirectionX_axis = sum(middleDirectionX_axis[length1:(2*length1)])/length1
middleProxDirectionY_axis = sum(middleDirectionY_axis[length1:(2*length1)])/length1
middleProxDirectionZ_axis = sum(middleDirectionZ_axis[length1:(2*length1)])/length1
middleProximal = np.hstack((middleProximalX_axis,middleProximalY_axis, middleProximalZ_axis))
middleProximalDirection = np.hstack((middleProxDirectionX_axis,middleProxDirectionY_axis,middleProxDirectionZ_axis))

# Getting the Intermediate Bone Position and Direction Values for the middle
middleInterX_axis = sum(middleX_axis[(2*length1):(3*length1)])/length1
middleInterY_axis = sum(middleY_axis[(2*length1):(3*length1)])/length1
middleInterZ_axis = sum(middleZ_axis[(2*length1):(3*length1)])/length1
middleInterDirectionX_axis = sum(middleDirectionX_axis[(2*length1):(3*length1)])/length1
middleInterDirectionY_axis = sum(middleDirectionY_axis[(2*length1):(3*length1)])/length1
middleInterDirectionZ_axis = sum(middleDirectionZ_axis[(2*length1):(3*length1)])/length1
middleInter = np.hstack((middleInterX_axis, middleInterY_axis, middleInterZ_axis))
middleIntermediateDirection = np.hstack((middleInterDirectionX_axis,middleInterDirectionY_axis,middleInterDirectionZ_axis))

# Getting the Distal Bone Position and Direction Values for the middle
middleDistalX_axis = sum(middleX_axis[(3*length1):size])/length1
middleDistalY_axis = sum(middleY_axis[(3*length1):size])/length1
middleDistalZ_axis = sum(middleZ_axis[(3*length1):size])/length1
middleDistDirectionX_axis = sum(middleDirectionX_axis[-3:])/length1
middleDistDirectionY_axis = sum(middleDirectionY_axis[-3:])/length1
middleDistDirectionZ_axis = sum(middleDirectionZ_axis[-3:])/length1
middleDistal = np.hstack((middleDistalX_axis, middleDistalY_axis,middleDistalZ_axis))
middleDistalDirection = np.hstack((middleDistDirectionX_axis, middleDistDirectionY_axis, middleDistDirectionZ_axis))

# Computing the Euclidean Distance between the Palm and the middle Finger Bones
palmMiddleMetadist = np.linalg.norm(middleMetacarpal - pos)
palmMiddleProxidist = np.linalg.norm(middleProximal - pos)
palmMiddleInterdist = np.linalg.norm(middleInter - pos)
palmMiddleDistdist = np.linalg.norm(middleDistal - pos)



###############################################################################################
# RING FINGER
###############################################################################################

# Reading csv Data for Ring Finger
dataring = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\ring.csv")
ringData = dataring['Data'].tolist()
ringDirection = dataring['Direction'].tolist()

# ring Finger Position and Direction Axes Initialization
ringX_axis = np.transpose(np.zeros(length))
ringY_axis = np.transpose(np.zeros(length))
ringZ_axis = np.transpose(np.zeros(length))
ringDirectionX_axis = np.transpose(np.zeros(length))
ringDirectionY_axis = np.transpose(np.zeros(length))
ringDirectionZ_axis = np.transpose(np.zeros(length))


# Separating the values from the str to array of separate X,Y,Z values for ring
for i in range(length):
    a = ringData[i]
    a = a[1: -1]
    ringData[i] = a
    b = list(a.split(","))
    ringData_ex = list(ringData[i].split(","))
    ringX_axis[i] = ringData_ex[0]
    ringY_axis[i] = ringData_ex[1]
    ringZ_axis[i] = ringData_ex[2]
   
for j in range(lenDir):
    c = ringDirection[j]
    c = c[1: -1]
    ringDirection[j] = c
    d = list(c.split(","))
    ringDirection_ex = list(ringDirection[j].split(","))
    ringDirectionX_axis[j] = ringDirection_ex[0]
    ringDirectionY_axis[j] = ringDirection_ex[1]
    ringDirectionZ_axis[j] = ringDirection_ex[2]
size = int(ringX_axis.shape[0])
length1 = size/4


# getting the metacarpal direction an start position values for the ring
ringMetacarpalX_axis = sum(ringX_axis[0:length1])/length1
ringMetacarpalY_axis = sum(ringY_axis[0:length1])/length1
ringMetacarpalZ_axis = sum(ringZ_axis[0:length1])/length1
ringMetaDirectionX_axis = sum(ringDirectionX_axis[0:length1])/length1
ringMetaDirectionY_axis = sum(ringDirectionY_axis[0:length1])/length1
ringMetaDirectionZ_axis = sum(ringDirectionZ_axis[0:length1])/length1
ringMetacarpal = np.hstack((ringMetacarpalX_axis,ringMetacarpalY_axis, ringMetacarpalZ_axis))
ringMetacarpalDirection = np.hstack((ringMetaDirectionX_axis,ringMetaDirectionY_axis,ringMetaDirectionZ_axis))


# Getting the Proximal Bone position and Direction Values for the ring
ringProximalX_axis = sum(ringX_axis[length1:(2*length1)])/length1
ringProximalY_axis = sum(ringY_axis[length1:(2*length1)])/length1
ringProximalZ_axis = sum(ringZ_axis[length1:(2*length1)])/length1
ringProxDirectionX_axis = sum(ringDirectionX_axis[length1:(2*length1)])/length1
ringProxDirectionY_axis = sum(ringDirectionY_axis[length1:(2*length1)])/length1
ringProxDirectionZ_axis = sum(ringDirectionZ_axis[length1:(2*length1)])/length1
ringProximal = np.hstack((ringProximalX_axis,ringProximalY_axis, ringProximalZ_axis))
ringProximalDirection = np.hstack((ringProxDirectionX_axis,ringProxDirectionY_axis,ringProxDirectionZ_axis))


# Getting the Intermediate Bone Position and Direction Values for the ring
ringInterX_axis = sum(ringX_axis[(2*length1):(3*length1)])/length1
ringInterY_axis = sum(ringY_axis[(2*length1):(3*length1)])/length1
ringInterZ_axis = sum(ringZ_axis[(2*length1):(3*length1)])/length1
ringInterDirectionX_axis = sum(ringDirectionX_axis[(2*length1):(3*length1)])/length1
ringInterDirectionY_axis = sum(ringDirectionY_axis[(2*length1):(3*length1)])/length1
ringInterDirectionZ_axis = sum(ringDirectionZ_axis[(2*length1):(3*length1)])/length1
ringInter = np.hstack((ringInterX_axis, ringInterY_axis, ringInterZ_axis))
ringIntermediateDirection = np.hstack((ringInterDirectionX_axis,ringInterDirectionY_axis,ringInterDirectionZ_axis))



# Getting the Distal Bone Position and Direction Values for the ring
ringDistalX_axis = sum(ringX_axis[(3*length1):size])/length1
ringDistalY_axis = sum(ringY_axis[(3*length1):size])/length1
ringDistalZ_axis = sum(ringZ_axis[(3*length1):size])/length1
ringDistDirectionX_axis = sum(ringDirectionX_axis[-3:])/length1
ringDistDirectionY_axis = sum(ringDirectionY_axis[-3:])/length1
ringDistDirectionZ_axis = sum(ringDirectionZ_axis[-3:])/length1
ringDistal = np.hstack((ringDistalX_axis, ringDistalY_axis,ringDistalZ_axis))
ringDistalDirection = np.hstack((ringDistDirectionX_axis, ringDistDirectionY_axis, ringDistDirectionZ_axis))

# Computing the Euclidean Distance between the Palm and the ring Finger Bones
palmringMetadist = np.linalg.norm(ringMetacarpal - pos)
palmringProxidist = np.linalg.norm(ringProximal - pos)
palmringInterdist = np.linalg.norm(ringInter - pos)
palmringDistdist = np.linalg.norm(ringDistal - pos)

###############################################################################################
# PINKY FINGER
###############################################################################################

datapinky = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\pinky.csv")
pinkyData = datapinky['Data'].tolist()
pinkyDirection = datapinky['Direction'].tolist()

# pinky Finger Position and Direction Axes Initialization
pinkyX_axis = np.transpose(np.zeros(length))
pinkyY_axis = np.transpose(np.zeros(length))
pinkyZ_axis = np.transpose(np.zeros(length))
pinkyDirectionX_axis = np.transpose(np.zeros(length))
pinkyDirectionY_axis = np.transpose(np.zeros(length))
pinkyDirectionZ_axis = np.transpose(np.zeros(length))

# Separating the values from the str to array of separate X,Y,Z values for pinky
for i in range(length):
    a = pinkyData[i]
    a = a[1: -1]
    pinkyData[i] = a
    b = list(a.split(","))
    pinkyData_ex = list(pinkyData[i].split(","))
    pinkyX_axis[i] = pinkyData_ex[0]
    pinkyY_axis[i] = pinkyData_ex[1]
    pinkyZ_axis[i] = pinkyData_ex[2]
   
for j in range(lenDir):
    c = pinkyDirection[j]
    c = c[1: -1]
    pinkyDirection[j] = c
    d = list(c.split(","))
    pinkyDirection_ex = list(pinkyDirection[j].split(","))
    pinkyDirectionX_axis[j] = pinkyDirection_ex[0]
    pinkyDirectionY_axis[j] = pinkyDirection_ex[1]
    pinkyDirectionZ_axis[j] = pinkyDirection_ex[2]

size = int(pinkyX_axis.shape[0])
length1 = size/4

# getting the metacarpal direction an start position values for the pinky
pinkyMetacarpalX_axis = sum(pinkyX_axis[0:length1])/length1
pinkyMetacarpalY_axis = sum(pinkyY_axis[0:length1])/length1
pinkyMetacarpalZ_axis = sum(pinkyZ_axis[0:length1])/length1
pinkyMetaDirectionX_axis = sum(pinkyDirectionX_axis[0:length1])/length1
pinkyMetaDirectionY_axis = sum(pinkyDirectionY_axis[0:length1])/length1
pinkyMetaDirectionZ_axis = sum(pinkyDirectionZ_axis[0:length1])/length1
pinkyMetacarpal = np.hstack((pinkyMetacarpalX_axis,pinkyMetacarpalY_axis, pinkyMetacarpalZ_axis))
pinkyMetacarpalDirection = np.hstack((pinkyMetaDirectionX_axis,pinkyMetaDirectionY_axis,pinkyMetaDirectionZ_axis))

# Getting the Proximal Bone position and Direction Values for the pinky
pinkyProximalX_axis = sum(pinkyX_axis[length1:(2*length1)])/length1
pinkyProximalY_axis = sum(pinkyY_axis[length1:(2*length1)])/length1
pinkyProximalZ_axis = sum(pinkyZ_axis[length1:(2*length1)])/length1
pinkyProxDirectionX_axis = sum(pinkyDirectionX_axis[length1:(2*length1)])/length1
pinkyProxDirectionY_axis = sum(pinkyDirectionY_axis[length1:(2*length1)])/length1
pinkyProxDirectionZ_axis = sum(pinkyDirectionZ_axis[length1:(2*length1)])/length1
pinkyProximal = np.hstack((pinkyProximalX_axis,pinkyProximalY_axis, pinkyProximalZ_axis))
pinkyProximalDirection = np.hstack((pinkyProxDirectionX_axis,pinkyProxDirectionY_axis,pinkyProxDirectionZ_axis))

# Getting the Intermediate Bone Position and Direction Values for the pinky
pinkyInterX_axis = sum(pinkyX_axis[(2*length1):(3*length1)])/length1
pinkyInterY_axis = sum(pinkyY_axis[(2*length1):(3*length1)])/length1
pinkyInterZ_axis = sum(pinkyZ_axis[(2*length1):(3*length1)])/length1
pinkyInterDirectionX_axis = sum(pinkyDirectionX_axis[(2*length1):(3*length1)])/length1
pinkyInterDirectionY_axis = sum(pinkyDirectionY_axis[(2*length1):(3*length1)])/length1
pinkyInterDirectionZ_axis = sum(pinkyDirectionZ_axis[(2*length1):(3*length1)])/length1
pinkyInter = np.hstack((pinkyInterX_axis, pinkyInterY_axis, pinkyInterZ_axis))
pinkyIntermediateDirection = np.hstack((pinkyInterDirectionX_axis,pinkyInterDirectionY_axis,pinkyInterDirectionZ_axis))

# Getting the Distal Bone Position and Direction Values for the pinky
pinkyDistalX_axis = sum(pinkyX_axis[(3*length1):size])/length1
pinkyDistalY_axis = sum(pinkyY_axis[(3*length1):size])/length1
pinkyDistalZ_axis = sum(pinkyZ_axis[(3*length1):size])/length1
pinkyDistDirectionX_axis = sum(pinkyDirectionX_axis[-3:])/length1
pinkyDistDirectionY_axis = sum(pinkyDirectionY_axis[-3:])/length1
pinkyDistDirectionZ_axis = sum(pinkyDirectionZ_axis[-3:])/length1
pinkyDistal = np.hstack((pinkyDistalX_axis, pinkyDistalY_axis,pinkyDistalZ_axis))
pinkyDistalDirection = np.hstack((pinkyDistDirectionX_axis, pinkyDistDirectionY_axis, pinkyDistDirectionZ_axis))

# Computing the Euclidean Distance between the Palm and the pinky Finger Bones
palmPinkyMetadist = np.linalg.norm(pinkyMetacarpal - pos)
palmPinkyProxidist = np.linalg.norm(pinkyProximal - pos)
palmPinkyInterdist = np.linalg.norm(pinkyInter - pos)
palmPinkyDistdist = np.linalg.norm(pinkyDistal - pos)











