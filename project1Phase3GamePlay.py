# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:38:56 2024

@author: 18159
"""
import random
from project1Phase2 import findPath


#read in easy/hard word lists

gameInfo = open("gameInformation.txt", "r")
easyWords = []
hardWords = []
parameterInfo = []
easyWordLength = int(gameInfo.readline())
for i in range(0, easyWordLength):
    s = gameInfo.readline()
    easyWords.append(s)
    
hardWordLength = int(gameInfo.readline())
for x in range(0, hardWordLength):
    s = gameInfo.readline()
    hardWords.append(s)
p = open("parameters.txt", "r")

fullWordList = sorted(easyWords + hardWords)
#read parameter file info

for line in p:
    pLine = line
    pLineList = pLine.split(" ")
    for x in range(2, len(pLineList), 3):
       
            currentDigit = (pLineList[x])
            newDigit = ''
            for y in range(len(currentDigit)):
                if currentDigit[y].isdigit() == True or currentDigit[y] == '.':
                    newDigit += currentDigit[y]
            parameterInfo.append(newDigit)
            
#transfer weight values to variables           
ed1 = int(parameterInfo[1])
ed2 = int(parameterInfo[2])

def playGame():
    
    print("Select your difficulty:")
    print("(1) Easy")
    print("(2) Hard")
    
    choice = input("")
    
    if choice == "1":
        print(easyGame())
    elif choice == "2":
        print("hard")
    else:
        print("invalid input, enter 1 or 2 to choose difficulty")
        playGame()
        
def easyGame():
    
    targetIndex = random.randint(0, len(easyWords))
    target = easyWords[targetIndex]
    pathLen = 0
    while (pathLen < ed1 or pathLen > ed2 ):
        
        sourceIndex = random.randint(0, len(easyWords))
        source = easyWords[sourceIndex]
        pathLen = len(findPath(fullWordList, fastMakeNeighborLists(fullWordList), source, target))
    return target, source