#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:12:30 2024

@author: Sriram Pemmaraju
"""


from project1Phase1 import getNeighbors, makeNeighborLists, degreeDistribution, getIsolatedNodes, readWords

###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It also take a word
# called source and it performs a breadth first search of the word network starting from
# the word source. It returns a list containing two lists: (i) the parents of all words 
# reached by the search and (ii) the distances of these words from the source word.    
#
# Examples: 
# >>> L1 = ['added', 'aided', 'bided']
# >>> nL1 = makeNeighborLists(L1)
# >>> searchWordNetwork(L1, nL1, "aided")
# [['aided', '', 'aided'], [1, 0, 1]]
# >>> searchWordNetwork(L1, nL1, "added")
# [['', 'added', 'aided'], [0, 1, 2]]
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
# Two more examples: 
# >>> L2 = ["bided", "bides", "sided", "sides", "tided", "tides"]
# >>> nL2 = makeNeighborLists(L2)
# >>> searchWordNetwork(L2, nL2, "tides")
# [['bides', 'tides', 'sides', 'tides', 'tides', ''], [2, 1, 2, 1, 1, 0]]
#
###############################################################################
def searchWordNetwork(wordList, nbrsList, source):
    parents = []
    distance = []
    reached = [source]
    processed = []
    
    
    for x in range(len(wordList)):
        parents.append("")
        distance.append(0)
    
  
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
                    p = wordList.index(p)
                    distanceCount += 1
                else:
                    break
                
            distance[word] = distanceCount
                
        
    return parents, distance

###############################################################################     
#
# Specification: This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It also take a word
# called source and a word called target. The function returns a shortest path
# from the source word to the target word, if there is a path between these two
# words. Otherwise, the function returns []. This function calls searchWordNetwork
# to compute the parent list and then follows the parent pointers from target 
# to source to compute a path; this path is then reversed and returned.
#
# Examples: 
# >>> L2 = ["bided", "bides", "sided", "sides", "tided", "tides"]
# >>> nL2 = makeNeighborLists(L2)
# >>> findPath(L2, nL2, "tides", "sided")
# ['tides', 'sides', 'sided']
# >>> L3 = ["curse", "curve", "nurse", "parse", "passe", "paste", "purse", "taste"]
# >>> nL3 = makeNeighborLists(L3)
# >>> findPath(L3, nL3, "curve", "taste")
# ['curve', 'curse', 'purse', 'parse', 'passe', 'paste', 'taste']
#
###############################################################################
def findPath(wordList, nbrsList, source, target):
    
    path = []
    wordNetwork = searchWordNetwork(wordList, nbrsList, source)
    
    i = wordList.index(target)
        
    path.insert(0, wordList[i])
    while (i != wordList.index(source)):
        
        i = wordNetwork[0][i]
        if i == '':
            path = []
            break
        else:
            i = wordList.index(i)
            path.insert(0, wordList[i])
    return path
            
        
###############################################################################     
#
# Specification:  This function takes a non-empty, sorted (in increasing
# alphabetical order) list of words called wordList and the word network of wordList
# represented as the corresponding list of neighbor lists. It returns the list of
# connected components in the word network.
#
# Definition: A connected component of a network is the set of all nodes that can
# be reached from each other via paths in the network.
#
# Examples: 
# >>> L3 = ["curse", "curve", "nurse", "parse", "passe", "paste", "purse", "taste"]
# >>> nL3 = makeNeighborLists(L3)
# >>> findComponents(L3, nL3)
# [['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]   
# >>> L4 = L3 +["sided", "tided", "bided"]
# >>> L4.sort()
# >>> nL4 = makeNeighborLists(L4)
# >>> findComponents(L4, nL4)
#  [['bided', 'sided', 'tided'],
#   ['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]
# >>> L5 = ["abhor"] + L4
# >>> nL5 = makeNeighborLists(L5)
# >>> findComponents(L5, nL5)
# [['abhor'],
#  ['bided', 'sided', 'tided'],
#  ['curse', 'curve', 'nurse', 'parse', 'passe', 'paste', 'purse', 'taste']]
#
# Notes: 
# (a) The nodes in each connected component should appear in the same order
# as they appear in wordList. 
# (b) The components themselves should be sorted by the first word in the component.
#
###############################################################################            
def findComponents(wordList, nbrsList):
    L = wordList.copy()
    newNbr = nbrsList.copy()
    
    processed = []
    componentList = []
    
    while ( len(L) != 0):
        reached = []
        currentComponent = []
        currentComponent.append(L[0])
        reached.append(L[0])
        while (len(reached) != 0):
            
            c = reached[0]
            del reached[0]
            index = L.index(c)
            for i in range(len(newNbr[index])):
                currentWord = newNbr[index][i]
                if currentWord not in reached and currentWord not in processed:
                    currentComponent.append(currentWord)
                    
                    reached.append(currentWord)
              
             
                processed.append(c)
        componentList.append(currentComponent)
        
        for x in range(len(currentComponent)):
            
            if currentComponent[x] in L:
                indexComp = L.index(currentComponent[x])
                del L[indexComp]
                del newNbr[indexComp]
            
        
    return componentList
        