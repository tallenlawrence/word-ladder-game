#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 07:23:03 2024

@author: sriram
"""


import random
from project1Phase2 import searchWordNetwork, findPath


def binarySearch(L, w, first, last):
    if (first > last):
        return -1
    
    mid = (first + last) // 2
    if (w == L[mid]):
        return mid
    elif (w < L[mid]):
        return binarySearch(L, w, first, mid-1)
    else:
        return binarySearch(L, w, mid+1, last)
    
def getIndex(L, w):
    return binarySearch(L, w, 0, len(L)-1)

###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList. It takes the 
# word network of all the words in wordList, represented as the corresponding 
# list of neighbor lists. It also takes a word called source in wordList and 
# it performs a breadth first search of the word network starting from
# the word source. In addition, it takes a list of words called easyWordList,
# all of which belong to wordList. These words have weight 0, whereas the remaining
# words have weight given by the non-negative integer parameter w.
# It returns a list containing two lists: (i) the parents of all words 
# reached by the search and (ii) the distances of these words from the source word.    
#
# Definition: The length of a path is the sum of the number of edges in the path
# plus the sum of the weights of all the nodes in the path.
#
# Definition: The distance between a pair of nodes u and v is the length of the
# shortest path betwwen them.
#
# Notes: 
# (a) If the length of wordList is n, then the returned list contains two lists,
# each of length n.
# (b) If the returned list is [L1, L2] and a word w has index i in wordList, then
# the parent information of w is stored in L1[i] and the distance information of
# w is stored in L2[i].
# (c) The parent information of a word is "" if it is the source word or if it
# is not reachable from the source word.
# (d) The distance information for any word that is not reachable from the source
# word is -1.
#
###############################################################################
def searchWeightedWordNetwork(wordList, nbrsList, source, easyWordList, w):
   
        parents = []
        weightedDistance = []
        reached = [source]
        processed = []
        
        
        for x in range(len(wordList)):
            parents.append("")
            weightedDistance.append(0)
        
      
        while len(reached) != 0:
            
           
            c = reached[0]
            del reached[0]
            
        
            
            index = wordList.index(c)
            for i in range(len(nbrsList[index])):
                currentWord = nbrsList[index][i]
                if currentWord not in reached and currentWord not in processed:
                    reached.append(currentWord)
                    indexNbr = wordList.index(currentWord)
                    parents[indexNbr] = c
            
                
            processed.append(c)
            
        for word in range(len(wordList)):
                distanceCount = 0
                p = word
                while (p != wordList.index(source)):
                    p = parents[p]
                    
                    if(p != ''):
                        pathWeight = 0
                        distanceCount += 1
                        if getIndex(easyWordList, p) == -1:
                            pathWeight += w
                        p = wordList.index(p)
                    else:
                        break
                    
                weightedDistance[word] = distanceCount + pathWeight
                    
            
        return parents, weightedDistance
 
###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList. It also takes a word 
# called source in wordList and a list of distances of all nodes in wordList
# from this network. It returns a list of words, in aphabetical order,
# that are between distance d1 and d2 from source (inclusive of d1 and d2).
# You can assume that d1 and d2 are non-negative integers and d1 <= d2. 
#
# You can assume that distanceList has been produced by a call to searchWordNetwork
# or searchWeightedWordNetwork. 
#
###############################################################################
def wordsAtDistanceRange(wordList, source, distanceList, d1, d2):
    withinRange = []
    for i in range(len(wordList)):
        if distanceList[i] >= d1 and distanceList[i] <= d2:
            withinRange.append(wordList[i])
            
    return sorted(withinRange)

###############################################################################
# Main program

# Read parameters.txt; use default values if parameters.txt is missing
# The paremeters.txt file has the format:
#   p = value1
#   w = value2
#   ed1 = value3, ed2 = value4
#   hd1 = value5, hd2 = value6
#   eh = value7, hh = value8
#   r = value9
# ADD CODE HERE. Ideally, this should be a fuction call
p = open("parameters.txt", "r")
parameterInfo = []
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
w = int(parameterInfo[1])        
ed1 = int(parameterInfo[2])
ed2 = int(parameterInfo[3])
hd1 = int(parameterInfo[4])
hd2 = int(parameterInfo[5])
eh = int(parameterInfo[6])
hh = int(parameterInfo[7])
r = float(parameterInfo[8])

# Read gameInformation.txt 

gameInfo = open("gameInformation.txt", "r")
easyWordList = []
hardWordList = []
nbrsList = []
easyWordLength = int(gameInfo.readline())
for i in range(0, easyWordLength):
    s = gameInfo.readline()
    s = s[0:5]
    easyWordList.append(s)
    
hardWordLength = int(gameInfo.readline())
for x in range(0, hardWordLength):
    s = gameInfo.readline()
    s = s[0:5]
    hardWordList.append(s)  

wordList = sorted(easyWordList + hardWordList)

for y in range(0, len(wordList)):
    s = gameInfo.readline()
    currentList = []
    currentWord = ''
    for h in range(len(s)):
        if (s[h]).isalpha():
            currentWord += s[h]
        elif (s[h]).isalpha() == False and currentWord != '':
            currentList.append(currentWord)
            currentWord = ''
            
    nbrsList.append(currentList)
    
    
gameInfo.close()
    

# Start initial user interaction
# Welcome them to the game and ask them to pick game playing mode.
# E for "easy mode" and H for "hard mode"
# ADD CODE HERE

print("Welcome to word ladder!")
print("Select your difficulty:")
print("(E) Easy")
print("(H) Hard")

#selecting difficulty
 
difficulty = 0
while(difficulty == 0):
  
   choice = input("")
   
   if choice == "E":
       difficulty = 1
       break
   elif choice == "H":
       difficulty = 2
      
       break
   else:
       print("invalid input, enter E or H to choose difficulty")

#difficulty setup

if (difficulty == 1):
    parameters = [ed1, ed2]
    numWordHints = eh
    targetIndex = random.randint(0, len(easyWordList))
    target = easyWordList[targetIndex]
    parentList, distanceList = searchWeightedWordNetwork(wordList, nbrsList, target, easyWordList, w)
    validWordList = wordsAtDistanceRange(wordList, target, distanceList, ed1, ed2)
    sourceIndex = random.randint(0, len(validWordList))
    source = validWordList[sourceIndex]
 
if (difficulty == 2):
    parameters = [hd1, hd2]
    numWordHints= hh
    targetIndex = random.randint(0, len(wordList))
    target = wordList[targetIndex]
    parentList, distanceList = searchWordNetwork(wordList, nbrsList, target)
    validWordList = wordsAtDistanceRange(wordList, target, distanceList, hd1, hd2)
    sourceIndex = random.randint(0, len(validWordList))
    source = validWordList[sourceIndex]
 
  
#distance hint function
  
distanceHintRate = r

def flipCoin():
    land = False
    flip = random.randint(0, 10)
    if (flip <= distanceHintRate * 10):
        land = True
    return land
    
#game interface

print('Source:', source, " Target:", target)
print('Enter (Q) anytime to quit or (H) for a hint. (You have' ,numWordHints, 'hint(s))')

#main game code   

currentNode = source
while (currentNode != target):
    
    
    prevNode = currentNode
    nodeIndex = getIndex(wordList, currentNode)
    
    currentNode = input("Input: ")
    if currentNode == 'Q':
        print("Thank you for playing!")
        break
    elif currentNode == 'H':
        if (numWordHints != 0):
            
            path = findPath(wordList, nbrsList, prevNode, target)
            print("Try" , path[1])
            numWordHints += -1
            print(numWordHints, "hint(s) remaining")
        else:
            print("Sorry! You're out of hints")
        currentNode = prevNode
    elif currentNode in nbrsList[nodeIndex] and currentNode == target:
        print("Congratulations! You reached the target word!")
        break
    elif currentNode in nbrsList[nodeIndex]:
        print("Good!")
        if flipCoin() == True:
            path = findPath(wordList, nbrsList, prevNode, target)
            print ("You are", (len(path)-2), "nodes away!")
    elif currentNode not in nbrsList[nodeIndex] and currentNode in wordList:
        print(currentNode, "is not a neighbor of" ,prevNode, "! Try again!")
        currentNode = prevNode
    
    else:
        print(currentNode, "is not a valid word! Try again")
        currentNode = prevNode

