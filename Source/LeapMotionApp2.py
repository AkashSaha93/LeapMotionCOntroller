

################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys, thread, time
import ctypes
import os
import struct
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import numpy as np
import pickle as pl
import pandas as pd

arm_2 = pd.DataFrame()
pitch_variable = pd.DataFrame()
roll_variable = pd.DataFrame()
yaw_variable = pd.DataFrame()

pos = pd.DataFrame()
normalVariable = pd.DataFrame()
directionVariable = pd.DataFrame()
velocityVariable = pd.DataFrame()

thumb = pd.DataFrame()
index = pd.DataFrame()
middle = pd.DataFrame()
ring = pd.DataFrame()
pinky = pd.DataFrame()

leftThumbOneVariable = pd.DataFrame()
leftIndexOneVariable = pd.DataFrame()
leftMiddleOneVariable = pd.DataFrame()
leftRingOneVariable = pd.DataFrame()
leftPinkyOneVariable = pd.DataFrame()

leftThumbTwoVariable = pd.DataFrame()
leftIndexTwoVariable = pd.DataFrame()
leftMiddleTwoVariable = pd.DataFrame()
leftRingTwoVariable = pd.DataFrame()
leftPinkyTwoVariable = pd.DataFrame()

leftThumbThreeVariable = pd.DataFrame()
leftIndexThreeVariable = pd.DataFrame()
leftMiddleThreeVariable = pd.DataFrame()
leftRingThreeVariable = pd.DataFrame()
leftPinkyThreeVariable = pd.DataFrame()

leftThumbFourVariable = pd.DataFrame()
leftIndexFourVariable = pd.DataFrame()
leftMiddleFourVariable = pd.DataFrame()
leftRingFourVariable = pd.DataFrame()
leftPinkyFourVariable = pd.DataFrame()

rightThumbOneVariable = pd.DataFrame()
rightIndexOneVariable = pd.DataFrame()
rightMiddleOneVariable = pd.DataFrame()
rightRingOneVariable = pd.DataFrame()
rightPinkyOneVariable = pd.DataFrame()

rightThumbTwoVariable = pd.DataFrame()
rightIndexTwoVariable = pd.DataFrame()
rightMiddleTwoVariable = pd.DataFrame()
rightRingTwoVariable = pd.DataFrame()
rightPinkyTwoVariable = pd.DataFrame()

rightThumbThreeVariable = pd.DataFrame()
rightIndexThreeVariable = pd.DataFrame()
rightMiddleThreeVariable = pd.DataFrame()
rightRingThreeVariable = pd.DataFrame()
rightPinkyThreeVariable = pd.DataFrame()

rightThumbFourVariable = pd.DataFrame()
rightIndexFourVariable = pd.DataFrame()
rightMiddleFourVariable = pd.DataFrame()
rightRingFourVariable = pd.DataFrame()
rightPinkyFourVariable = pd.DataFrame()


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    
    
    
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
#        controller = Leap.Controller()
        frame = controller.frame()
#        timestamp = frame.timestamp
        
        
        # Get hands
        for hand in frame.hands:
#            print(timestamp)
            
            global pitch_variable, roll_variable, yaw_variable, pos, normalVariable, directionVariable, velocityVariable
            handType = "Left hand" if hand.is_left else "Right hand"

            print "  %s, id %d, position: %s" % (
                handType, hand.id, hand.palm_position)
#            
            # Get the hand's normal vector and direction
            position = pd.DataFrame([hand.palm_position])
            normal = pd.DataFrame([hand.palm_normal])
            direction = pd.DataFrame([hand.direction])
            velocity = pd.DataFrame([hand.palm_velocity])
            pos = pos.append(position, ignore_index = True)
            normalVariable = normalVariable.append(normal, ignore_index = True)
            directionVariable = directionVariable.append(direction, ignore_index = True)
            velocityVariable = velocityVariable.append(velocity, ignore_index = True)
            
            
            
#            ptlbs = frame.pointables
            
            # Calculate the hand's pitch, roll, and yaw angles
            print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
                direction.pitch * Leap.RAD_TO_DEG,
                normal.roll * Leap.RAD_TO_DEG,
                direction.yaw * Leap.RAD_TO_DEG)
            
            #Saving the roll, pitch and yaw
            pitch_1 = pd.DataFrame([direction.pitch * Leap.RAD_TO_DEG])
            roll_1 = pd.DataFrame([normal.roll * Leap.RAD_TO_DEG])
            yaw_1 = pd.DataFrame([direction.yaw * Leap.RAD_TO_DEG])
            
            pitch_variable = pitch_variable.append(pitch_1, ignore_index = True)
            roll_variable = roll_variable.append(roll_1, ignore_index = True)
            yaw_variable = yaw_variable.append(yaw_1, ignore_index = True)
            
            
            # Get arm bone
            arm = hand.arm
            print "  Arm direction: %s, wrist position: %s" % (
                arm.direction,
                arm.wrist_position)
            arm_1 = pd.DataFrame([arm.wrist_position])
            global arm_2
            arm_2 = arm_2.append(arm_1, ignore_index = True)
           
            global leftThumbOneVariable, leftThumbTwoVariable, leftThumbThreeVariable, leftThumbFourVariable
            global leftIndexOneVariable, leftIndexTwoVariable, leftIndexThreeVariable, leftIndexFourVariable
            global leftMiddleOneVariable, leftMiddleTwoVariable, leftMiddleThreeVariable, leftMiddleFourVariable
            global leftRingOneVariable, leftRingTwoVariable, leftRingThreeVariable, leftRingFourVariable
            global leftPinkyOneVariable, leftPinkyTwoVariable, leftPinkyThreeVariable, leftPinkyFourVariable
        
            global rightThumbOneVariable, rightThumbTwoVariable, rightThumbThreeVariable, rightThumbFourVariable
            global rightIndexOneVariable, rightIndexTwoVariable, rightIndexThreeVariable, rightIndexFourVariable
            global rightMiddleOneVariable, rightMiddleTwoVariable, rightMiddleThreeVariable, rightMiddleFourVariable
            global rightRingOneVariable, rightRingTwoVariable, rightRingThreeVariable, rightRingFourVariable
            global rightPinkyOneVariable, rightPinkyTwoVariable, rightPinkyThreeVariable, rightPinkyFourVariable
            global thumb, index, middle, ring, pinky
            # Get fingers
            for finger in hand.fingers:

                print "    %s finger, id: %d" % (
                    self.finger_names[finger.type],
                    finger.id)
#                fingerIdValue = finger.id
                fin_name = self.finger_names[finger.type]

#                # Get bones
                for b in range(0, 4):
                    bone = finger.bone(b)
                    print "      Bone: %s, start: %s, end: %s, direction: %s" % (
                        self.bone_names[bone.type],
                        bone.prev_joint,
                        bone.next_joint,
                        bone.direction)
                    bName = self.bone_names[bone.type]
                    
                    
                    if(handType == "Left hand"):
                    
                        if (fin_name == 'Thumb' and bName == 'Metacarpal'):
                            leftThumbOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                              'Direction' : [bone.direction] })
                            leftThumbOneVariable = leftThumbOneVariable.append(leftThumbOne, ignore_index = True)
                            #print ("bokachoda ", ptlbs.tip_velocity
                        
                        elif (fin_name == 'Thumb' and bName == 'Proximal'):
                            leftThumbTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                              'Direction' : [bone.direction] })
                            leftThumbTwoVariable = leftThumbTwoVariable.append(leftThumbTwo, ignore_index = True)
                        
                        
                        elif (fin_name == 'Thumb' and bName == 'Intermediate'):
                            leftThumbThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftThumbThreeVariable = leftThumbThreeVariable.append(leftThumbThree, ignore_index = True)
                            
                        elif (fin_name == 'Thumb' and bName == 'Distal'):
                            leftThumbFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftThumbFourVariable = leftThumbFourVariable.append(leftThumbFour, ignore_index = True)
                            
                        elif (fin_name == 'Index' and bName == 'Metacarpal'):
                            leftIndexOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftIndexOneVariable = leftIndexOneVariable.append(leftIndexOne, ignore_index = True)
                            
                        elif (fin_name == 'Index' and bName == 'Proximal'):
                            leftIndexTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftIndexTwoVariable = leftIndexTwoVariable.append(leftIndexTwo, ignore_index = True)
                            
                        elif (fin_name == 'Index' and bName == 'Intermediate'):
                            leftIndexThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftIndexThreeVariable = leftIndexThreeVariable.append(leftIndexThree, ignore_index = True)
                            
                        elif (fin_name == 'Index' and bName == 'Distal'):
                            leftIndexFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftIndexFourVariable = leftIndexFourVariable.append(leftIndexFour, ignore_index = True)
                            
                        elif (fin_name == 'Middle' and bName == 'Metacarpal'):
                            leftMiddleOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftMiddleOneVariable = leftMiddleOneVariable.append(leftMiddleOne, ignore_index = True)
                            
                        elif (fin_name == 'Middle' and bName == 'Proximal'):
                            leftMiddleTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftMiddleTwoVariable = leftMiddleTwoVariable.append(leftMiddleTwo, ignore_index = True)
                            
                        elif (fin_name == 'Middle' and bName == 'Intermediate'):
                            leftMiddleThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftMiddleThreeVariable = leftMiddleThreeVariable.append(leftMiddleThree, ignore_index = True)
                            
                        elif (fin_name == 'Middle' and bName == 'Distal'):
                            leftMiddleFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftMiddleFourVariable = leftMiddleFourVariable.append(leftMiddleFour, ignore_index = True)
                            
                        elif (fin_name == 'Ring' and bName == 'Metacarpal'):
                            leftRingOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftRingOneVariable = leftRingOneVariable.append(leftRingOne, ignore_index = True)
                            
                        
                        elif (fin_name == 'Ring' and bName == 'Proximal'):
                            leftRingTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftRingTwoVariable = leftRingTwoVariable.append(leftRingTwo, ignore_index = True)
                            
                        elif (fin_name == 'Ring' and bName == 'Intermediate'):
                            leftRingThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftRingThreeVariable = leftRingThreeVariable.append(leftRingThree, ignore_index = True)
                            
                        elif (fin_name == 'Ring' and bName == 'Distal'):
                            leftRingFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftRingFourVariable = leftRingFourVariable.append(leftRingFour, ignore_index = True)
                            
                        elif (fin_name == 'Pinky' and bName == 'Metacarpal'):
                            leftPinkyOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftPinkyOneVariable = leftPinkyOneVariable.append(leftPinkyOne, ignore_index = True)
                            
                        elif (fin_name == 'Pinky' and bName == 'Proximal'):
                            leftPinkyTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftPinkyTwoVariable = leftPinkyTwoVariable.append(leftPinkyTwo, ignore_index = True)
                            
                        elif (fin_name == 'Pinky' and bName == 'Intermediate'):
                            leftPinkyThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftPinkyThreeVariable = leftPinkyThreeVariable.append(leftPinkyThree, ignore_index = True)
                            
                        else:
                            leftPinkyFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            leftPinkyFourVariable = leftPinkyFourVariable.append(leftPinkyFour, ignore_index = True)
                        
                        leftThumb = [leftThumbOneVariable, leftThumbTwoVariable, leftThumbThreeVariable, leftThumbFourVariable ]
                        leftThumbVariable = pd.concat(leftThumb, ignore_index = True)
                        leftThumbVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Left\\thumb.csv', sep = ',')
                        
                        leftIndex = [leftIndexOneVariable, leftIndexTwoVariable, leftIndexThreeVariable, leftIndexFourVariable ]
                        leftIndexVariable = pd.concat(leftIndex, ignore_index = True)
                        leftIndexVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Left\\index.csv', sep = ',')
                        
                        leftMiddle = [leftMiddleOneVariable, leftMiddleTwoVariable, leftMiddleThreeVariable, leftMiddleFourVariable ]
                        leftMiddleVariable = pd.concat(leftMiddle, ignore_index = True)
                        leftMiddleVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Left\\middle.csv', sep = ',')
                        
                        leftRing = [leftRingOneVariable, leftRingTwoVariable, leftRingThreeVariable, leftRingFourVariable ]
                        leftRingVariable = pd.concat(leftRing, ignore_index = True)
                        leftRingVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Left\\ring.csv', sep = ',')
                        
                        leftPinky = [leftPinkyOneVariable, leftPinkyTwoVariable, leftPinkyThreeVariable, leftPinkyFourVariable ]
                        leftPinkyVariable = pd.concat(leftPinky, ignore_index = True)
                        leftPinkyVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Left\\pinky.csv', sep = ',')
                        
                        
                
                    elif (handType == "Right hand"):
                        
                        if (fin_name == 'Thumb' and bName == 'Metacarpal'):
                                rightThumbOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                                      'Direction' : [bone.direction] })
                                rightThumbOneVariable = rightThumbOneVariable.append(rightThumbOne, ignore_index = True)
                                
                        elif (fin_name == 'Thumb' and bName == 'Proximal'):
                            rightThumbTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightThumbTwoVariable = rightThumbTwoVariable.append(rightThumbTwo, ignore_index = True)
                            
                            
                        elif (fin_name == 'Thumb' and bName == 'Intermediate'):
                            rightThumbThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightThumbThreeVariable = rightThumbThreeVariable.append(rightThumbThree, ignore_index = True)
                            
                        elif (fin_name == 'Thumb' and bName == 'Distal'):
                            rightThumbFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightThumbFourVariable = rightThumbFourVariable.append(rightThumbFour, ignore_index = True)
                            
                        elif (fin_name == 'Index' and bName == 'Metacarpal'):
                            rightIndexOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightIndexOneVariable = rightIndexOneVariable.append(rightIndexOne, ignore_index = True)
                            
                        elif (fin_name == 'Index' and bName == 'Proximal'):
                            rightIndexTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightIndexTwoVariable = rightIndexTwoVariable.append(rightIndexTwo, ignore_index = True)
                            
                        elif (fin_name == 'Index' and bName == 'Intermediate'):
                            rightIndexThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightIndexThreeVariable = rightIndexThreeVariable.append(rightIndexThree, ignore_index = True)
                            
                        elif (fin_name == 'Index' and bName == 'Distal'):
                            rightIndexFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightIndexFourVariable = rightIndexFourVariable.append(rightIndexFour, ignore_index = True)
                            
                        elif (fin_name == 'Middle' and bName == 'Metacarpal'):
                            rightMiddleOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightMiddleOneVariable = rightMiddleOneVariable.append(rightMiddleOne, ignore_index = True)
                            
                        elif (fin_name == 'Middle' and bName == 'Proximal'):
                            rightMiddleTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightMiddleTwoVariable = rightMiddleTwoVariable.append(rightMiddleTwo, ignore_index = True)
                            
                        elif (fin_name == 'Middle' and bName == 'Intermediate'):
                            rightMiddleThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightMiddleThreeVariable = rightMiddleThreeVariable.append(rightMiddleThree, ignore_index = True)
                            
                        elif (fin_name == 'Middle' and bName == 'Distal'):
                            rightMiddleFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightMiddleFourVariable = rightMiddleFourVariable.append(rightMiddleFour, ignore_index = True)
                            
                        elif (fin_name == 'Ring' and bName == 'Metacarpal'):
                            rightRingOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightRingOneVariable = rightRingOneVariable.append(rightRingOne, ignore_index = True)
                            
                        
                        elif (fin_name == 'Ring' and bName == 'Proximal'):
                            rightRingTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightRingTwoVariable = rightRingTwoVariable.append(rightRingTwo, ignore_index = True)
                            
                        elif (fin_name == 'Ring' and bName == 'Intermediate'):
                            rightRingThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightRingThreeVariable = rightRingThreeVariable.append(rightRingThree, ignore_index = True)
                            
                        elif (fin_name == 'Ring' and bName == 'Distal'):
                            rightRingFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightRingFourVariable = rightRingFourVariable.append(rightRingFour, ignore_index = True)
                            
                        elif (fin_name == 'Pinky' and bName == 'Metacarpal'):
                            rightPinkyOne = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightPinkyOneVariable = rightPinkyOneVariable.append(rightPinkyOne, ignore_index = True)
                            
                        elif (fin_name == 'Pinky' and bName == 'Proximal'):
                            rightPinkyTwo = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightPinkyTwoVariable = rightPinkyTwoVariable.append(rightPinkyTwo, ignore_index = True)
                            
                        elif (fin_name == 'Pinky' and bName == 'Intermediate'):
                            rightPinkyThree = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightPinkyThreeVariable = rightPinkyThreeVariable.append(rightPinkyThree, ignore_index = True)
                                
                        else:
                            rightPinkyFour = pd.DataFrame({'Data' : [bone.prev_joint],
                                                  'Direction' : [bone.direction] })
                            rightPinkyFourVariable = rightPinkyFourVariable.append(rightPinkyFour, ignore_index = True)
                        
                        rightThumb = [rightThumbOneVariable, rightThumbTwoVariable, rightThumbThreeVariable, rightThumbFourVariable ]
                        rightIndex = [rightIndexOneVariable, rightIndexTwoVariable, rightIndexThreeVariable, rightIndexFourVariable ]
                        rightMiddle = [rightMiddleOneVariable, rightMiddleTwoVariable, rightMiddleThreeVariable, rightMiddleFourVariable ]
                        rightRing = [rightRingOneVariable, rightRingTwoVariable, rightRingThreeVariable, rightRingFourVariable ]
                        rightPinky = [rightPinkyOneVariable, rightPinkyTwoVariable, rightPinkyThreeVariable, rightPinkyFourVariable ]
                        
                        rightThumbVariable = pd.concat(rightThumb, ignore_index = True)
                        rightIndexVariable = pd.concat(rightIndex, ignore_index = True)
                        rightMiddleVariable = pd.concat(rightMiddle, ignore_index = True)
                        rightRingVariable = pd.concat(rightRing, ignore_index = True)
                        rightPinkyVariable = pd.concat(rightPinky, ignore_index = True )
                                            
                        rightThumbVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\thumb.csv', sep = ',')
                        rightIndexVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\index.csv', sep = ',')
                        rightMiddleVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\middle.csv', sep = ',')
                        rightRingVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\ring.csv', sep = ',')
                        rightPinkyVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\pinky.csv', sep = ',')
                        
                    else:
                        print()
                    
           
            arm_2.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\arm_data.csv', sep = ',')   
            pitch_variable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\pitch_data.csv', sep = ',')
            roll_variable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\roll_data.csv', sep = ',')
            yaw_variable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\yaw_data.csv', sep = ',')
            
            pos.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\palm_position.csv', sep = ',')
            normalVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\palm_normal.csv', sep = ',')
            directionVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\palm_direction.csv', sep = ',')
            velocityVariable.to_csv('C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\palm_velocity.csv', sep = ',')
#            
            
            
        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ""
#        dataThumb = pd.read_csv("C:\\Users\\as7933\\Desktop\\Grad_Project\\Source\\Data\\Right\\thumb.csv")
#        thumbDataSet = dataThumb.Data
        
        
        
        # remove the start and ending brackets and save each point as a separate point
#        length = thumbDataSet.shape[0]
#        thumbMetacarpalX_axis = np.transpose(np.zeros(length))
#        thumbMetacarpalY_axis = np.transpose(np.zeros(length))
#        thumbMetacarpalZ_axis = np.transpose(np.zeros(length))
#        for i in range(0,length):
#           a = thumbDataSet[i]
#           a = a[1:-1]
#           b = list(a.split(","))
#           thumbDataSet[i] = b
#           thumbMetacarpalX_axis[i] = thumbDataSet[i][0]
#           thumbMetacarpalY_axis[i] = thumbDataSet[i][1]
#           thumbMetacarpalZ_axis[i] = thumbDataSet[i][2]
#   

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    
    try:
        
        
        print "Perform Gesture in 3..2..1 "
#        time.sleep(4)
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
