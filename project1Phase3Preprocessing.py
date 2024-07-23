#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:12:30 2024

@author: Sriram Pemmaraju
"""

###############################################################################
#
# Specification: The function reads words from the file "words.txt" and creates and
# returns a list with these words. The words should in the same order in the list
# as they appear in the file. Each string in the list of words should be exactly
# 5 characters long.
#
# NEW: if the file word.txt is missing, this function should just return [] instead
# of causing the program to cause an exception.
#
# Examples:
# >>> L = readWords()
# >>> len(L)
# 5757
# >>> L[len(L)-1]
# 'zowie'
# >>> L[0:10]
# ['aargh',
#  'abaca',
#  'abaci',
#  'aback',
#  'abaft',
#  'abase',
#  'abash',
#  'abate',
#  'abbey',
#  'abbot']
# >>> L[1000]
# 'coney'
# >>> sorted(L)==L
# True
#
###############################################################################
def readWords():
   L = open("words.txt", "r")
   wordList = []
   for line in L:
       s = (line.strip())
       
       wordList.append(s)
   L.close()

  
   return wordList
   
    
    
###############################################################################     
#
# Specification:  This function takes a list of words and a list of file names.
# It reads from each file in the given list of file names and extracts words from
# the file. For each word in the list of words, it computes the frequency of this
# word in all the files in the given list of file names. The function returns
# the list of frequencies. The order in which frequencies appear in the frequency
# list should match the order in which words appear in the given word list. In other
# words, the frequency in slot 0 should be the frequency of smallerWordList[0],
# the frequency in slot 1 should be the frequency of smallerWordList[1], etc.
# The function should use "try and except" to gracefully deal with missing files.
# If a file is missing, it should just skip over to the next file. If all files
# are missing, then the frequency list returned should contain all 0's.
#
###############################################################################   
def computeFrequencies(smallerWordList, fileNameList):
    
    frequencyList = [0] * len(smallerWordList)
    
    for i in fileNameList:
        
        currentText = open(i, encoding="utf8")
        text = []
        for line in currentText:
            s = (line.strip())

            text.append(s)
        textWordList = extractWords(text)
        
        for x in range(len(frequencyList)):
            frequencyInText = textWordList.count(smallerWordList[x])
            frequencyList[x] += frequencyInText
    return frequencyList
        

############################################################################### 
# You can add as many other functions as you want to make your code streamlined,
# readable, and efficient
############################################################################### 
from project1Phase1 import makeNeighborLists, getIndex, binarySearch
from project1Phase2 import searchWordNetwork, findPath, findComponents
from WPS8 import createSentences

def extractWords(list):
        
        L = []
        newList = []
        
        for text in list:
            
            L = text.split(" ")
            for x in range(len(L)):
                if L[x].isalpha():
                    currentWord = L[x]
                else:
                    currentWord = ""
                    for i in range(len(L[x])):
                        if L[x][i].isalpha():
                            currentWord = currentWord + (L[x][i])
                            
                if len(currentWord) != 0:
                        newList.append(currentWord.lower())
                 
    
        return newList    

def fastMakeNeighborLists(wordList):
    
 
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  

    nbrList = []
    for x in range(len(wordList)):
        currentNeighbors = []
        for i in range(len(wordList[x])): 
            newWord = wordList[x]
            
            for z in range(len(alphabet)):
                newWord = newWord[:i] + alphabet[z] + newWord[i + 1:]
                if newWord != wordList[x]:
                     wordIndex = getIndex(wordList, newWord)
                     if wordIndex != -1:
                        currentNeighbors.append(newWord)
         
        nbrList.append(currentNeighbors)       
                   
       
    return nbrList

def sortByFrequency(wordList, fList):

   sortedList = []
   maxFreq = max(fList)
   currentFreq = 0
   
                  
   while(maxFreq >= currentFreq):
       currentList = []
       for x in range(len(wordList)):
           
           
           if fList[x] == currentFreq:
               currentList.append(wordList[x])
   
       sortedList += currentList
       currentFreq += 1
                          

   return sortedList
############################################################################### 
# main program starts here
############################################################################### 

# STEP 1: Identify the list of words in the largest connected component
# (a) Read the list of all words in words.txt. Make sure that the 
# program exits gracefully if words.txt is not available
# (b) Build the adjacency list representation of the word network of this list of 
# words
# (c) Find all connected components of this word network
# (d) Identify the largest connected component and create a list with the words 
# in the largest connected component in sorted order
#
# Code for STEP 1 goes here


wordBank = readWords()
    
compList = findComponents(wordBank, fastMakeNeighborLists(wordBank))
    
compLen = []
for x in range(len(compList)):
        
        compLen.append(len((compList)[x]))
        
maxCompLen = max(compLen) 
    
largestComp = sorted(compList[compLen.index(maxCompLen)])
    
print(len(largestComp))
    
    

# STEP 2: Compute the frequencies of all the words in the largest connected component
# and designate the p % of the words with highest frequency as "easy" words  
# (a) Create a list containing all the names of text files downloaded from Project Gutenberg
# (b) Call the function computeFrequencies to read from these files, extract words, and
# update the frequencies of the words in the largest connected component  
# (c) Read from the file parameters.txt to get the value of parameter p
# (d) Designate the most frequent  p % of these words as "easy" words and the rest
# as "hard" words 
#
# Code for STEP 2 goes here

textList = ["pg84.txt", "pg37106.txt", "pg64317.txt", "pg2701.txt","pg1342.txt", "pg2641.txt"]
    
fList = computeFrequencies(largestComp, textList)
    
paramFile = open("parameters.txt", "r")
    
for i in range(1):
        pLine = paramFile.readline()
p = int((pLine.split(" "))[2][0:2])
   
sortedWordList = sortByFrequency(largestComp, fList)
   
pRange = (len(largestComp) - int(len(largestComp) * p/100))
   
easyWordList = []
hardWordList = []
   
for i in range(pRange, len(largestComp)):
           
           easyWordList.append(sortedWordList[i])
           
for x in range(0, pRange):
       
       hardWordList.append(sortedWordList[x])
    
       

# STEP 3: Write into the file gameInformation.txt
# (a) Open the file "gameInformation.txt" for writing
# (b) Write the number of easy words, followed by the easy words themselves in alphabetical order
# (c) Write the number of hard words, followed by the hard words themselves in alphabetical order
# (d) Write the adjacency list representation of the word network of the largest connected component
# Make sure that everything is written into the file gameInformation.txt as per the specifications
# in the project 1 handout
#
# Code for STEP 3 goes here
    
adjList = fastMakeNeighborLists(largestComp)

g = open('gameInformation.txt', 'w')
if FileNotFoundError:
    print("gameInformation.txt not found")

g.write("%s\n" % str(len(easyWordList)))
for line in sorted(easyWordList):
       g.write("%s\n" % line)
g.write("%s\n" % str(len(hardWordList)))
for lineH in sorted(hardWordList):
       g.write("%s\n" % lineH)
for lineA in adjList:
       g.write("%s\n" % lineA)
g.close()

