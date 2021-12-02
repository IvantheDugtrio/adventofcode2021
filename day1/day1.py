#!/usr/bin/env python3
import sys

slidingWindow = []
windowCount=0
lineCount=0
depthSum=0
prevDepthSum=0
decCount=0
incCount=0
sameCount=0
with open(sys.argv[1],'r') as file:
    for line in file:
        lineCount+=1
        for depth in slidingWindow:
            depthSum+=depth
        if len(slidingWindow)==3:
            windowCount+=1
            if depthSum < prevDepthSum:
                decCount+=1
            elif depthSum > prevDepthSum:
                incCount+=1
            else:
                sameCount+=1
            slidingWindow.pop(0)
        # Prepare for next window iteration
        prevDepthSum=depthSum # save sum
        depthSum=0 # initialize counter
        slidingWindow.append(int(line))
print("There are: "+str(windowCount)+" sliding windows total")
print("There are: "+str(incCount)+" measurements > than prev")
print("There are: "+str(decCount)+" measurements < than prev")
print("There are: "+str(sameCount)+" measurements = to prev")
