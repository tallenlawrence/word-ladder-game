# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:29:33 2024

@author: 18159
"""

from project1Phase2 import searchWordNetwork, findPath, findComponents
from project1Phase1 import readWords, makeNeighborLists

def main():
    
    L = readWords()
    nL = makeNeighborLists(L)
    
#question a
    print("(a)")
    abodeNet = (searchWordNetwork(L, nL, "abode"))
    abodeNetMax = max(abodeNet[1])
    print(abodeNetMax)
#question b
    print("(b)")
    farWords = []
    for i in (range(len(L))):
        if abodeNet[1][i] == 24:
            farWords.append(L[i])
    print(farWords)
#question c
    print("(c)")
    print(findPath(L, nL, "abode" , "house"))
    print(findPath(L, nL, "sweet", "yucky"))
    print(findPath(L, nL, "index", "third"))
    print(findPath(L, nL, "wheel", "turns"))
    print(findPath(L, nL, "lucky", "break"))
    
#question d
    print("(d)")
    compList = findComponents(L, nL)
    print(len(compList))
#question e
    print("(e)")
    compLen = []
    for x in range(len(compList)):
        
        compLen.append(len((compList)[x]))
        
    maxCompLen = max(compLen)
    print(maxCompLen)
    
#question f
    print("(f)")
    index = compLen.index(maxCompLen)
    print((sorted(compList[index]))[:10])
    
#question g
    print("(g)")
    print(compList[compLen.index(8)])p
    pass
    

