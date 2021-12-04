#!/usr/bin/env python3

import sys

orList = []
sigList = []
lineCount = 0
gammaR = ''
epsilonR = ''

def stringToInt(binaryString):
    significand = 0
    decimal = 0
    for sig in reversed(binaryString):
        decimal += int(sig)*pow(2,significand)
        significand += 1
    return decimal

def findSig(stringList):
    elementCount = 0
    sigFigSum = 0
    newStringList = []
    for val in stringList:
        elementCount += 1
        sigFigSum += int(val[0])
    if sigFigSum > elementCount/2:
        sigFig = 1
    else:
        sigFig = 0
    for val in stringList:
        if val[0] == sigFig:
            newStringList.append(val)
    return newStringList

with open(sys.argv[1],'r') as fi:
    for line in fi:
        lineCount += 1
        line = line.strip()
        orList.append(line)
        charPos = 0
        for char in line:
            if len(sigList) > charPos:
                sigList[charPos] += int(char)
            else:
                sigList.append(int(char))
            charPos += 1

# Part 1
for sig in sigList:
    if int(sig) < (lineCount/2):
        gammaR += '0'
        epsilonR += '1'
    elif int(sig) > (lineCount/2):
        gammaR += '1'
        epsilonR += '0'

gammaRdec = stringToInt(gammaR)
epsilonRdec = stringToInt(epsilonR)

print(gammaR)
print(epsilonR)
print(gammaRdec)
print(epsilonRdec)
print(gammaRdec*epsilonRdec)
