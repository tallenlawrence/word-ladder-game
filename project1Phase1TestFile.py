#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 16:13:40 2023

@author: Sriram Pemmaraju
"""

#-------------------------------------------------------
from project1Phase1 import *
#-------------------------------------------------------

# main program
words = readWords()


tests = []

########################################################
## areNeighbors
########################################################
# Test 1
tests.append(areNeighbors("Hello", "Hello")==False)

# Test 2
tests.append(areNeighbors("Hello", "hello")==True)

# Test 3
tests.append(areNeighbors("Helloe", "coffee")==False)

# Test 4
tests.append(areNeighbors("a", "a")==False)

# Test 5
tests.append(areNeighbors("ab", "ac")==True)
########################################################


########################################################
## readWords
########################################################
# Test 6
tests.append(len(words)==5757)

# Test 7
tests.append(len(words[53])==5)

# Test 8
tests.append(sorted(words)==words)

# Test 9
tests.append(words[6]=='abash')

# Test 10
tests.append(words[len(words)-1]=='zowie')
########################################################


########################################################
## makeNeighborLists
########################################################
# Test 11
L11 = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided', 'sided', 'tided']
tests.append(makeNeighborLists(L11))==[['anded'],['aides'], ['aider'],['aimed', 'aired'],['ailed', 'aired'],['ailed', 'aimed'],['added'],['sided', 'tided'],['bided', 'tided'],['bided', 'sided']]

# Test 12
L12 = ['joked', 'poked', 'toked', 'yokel', 'yokes', 'yodel','yoked', 'cokes', 'jokes', 'pokes', 'tokes', 'yikes', 'yores', 'folks', 'yolky', 'folky', 'yolks']
tests.append(makeNeighborLists(L12) == [['poked', 'toked', 'yoked', 'jokes'],
 ['joked', 'toked', 'yoked', 'pokes'],
 ['joked', 'poked', 'yoked', 'tokes'],
 ['yokes', 'yodel', 'yoked'],
 ['yokel', 'yoked', 'cokes', 'jokes', 'pokes', 'tokes', 'yikes', 'yores'],
 ['yokel'],
 ['joked', 'poked', 'toked', 'yokel', 'yokes'],
 ['yokes', 'jokes', 'pokes', 'tokes'],
 ['joked', 'yokes', 'cokes', 'pokes', 'tokes'],
 ['poked', 'yokes', 'cokes', 'jokes', 'tokes'],
 ['toked', 'yokes', 'cokes', 'jokes', 'pokes'],
 ['yokes'],
 ['yokes'],
 ['folky', 'yolks'],
 ['folky', 'yolks'],
 ['folks', 'yolky'],
 ['folks', 'yolky']])


# Test 13
L13 = ['a','b','c','d']
tests.append(makeNeighborLists(L13) == [ ['b','c','d'], ['a','c','d'], ['a','b','d'], ['a','b','c'] ])
########################################################


########################################################
## getNeighbors
########################################################
# Test 14
L14 = ['added', 'aided', 'bided']
nL14 = makeNeighborLists(L14)
tests.append(getNeighbors(L14, nL14, 'aided')==['added', 'bided'])

# Test 15
L15 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
nL15 = makeNeighborLists(L15)
tests.append(getNeighbors(L15, nL15, 'joked')==['jokes'])

# Test 16
L16 = ['at', 'so']
nL16 = [[],[]]
tests.append([getNeighbors(L16, nL16, 'at'),getNeighbors(L16, nL16, 'so')]==[[],[]])
########################################################


########################################################
## getIsolatedNodes
########################################################
# Test 17
L17 = ['abbey', 'added', 'aided', 'audio', 'audit', 'bided', 'young']
nL17 = makeNeighborLists(L17)
tests.append(getIsolatedNodes(L17, nL17)==['abbey', 'young'])

# Test 18
L18 = ['aargh',
          'abaft',
          'abbey',
          'abbot',
          'abeam',
          'abhor',
          'absit',
          'abuzz',
          'abyss',
          'achoo',
          'acids',
          'acrid',
          'actin',
          'actor',
          'acute',
          'adage',
          'addle',
          'adieu',
          'adios',
          'adlib']
nL18 = makeNeighborLists(L18)
tests.append(getIsolatedNodes(L18, nL18)== ['aargh',
  'abaft',
  'abbey',
  'abbot',
  'abeam',
  'abhor',
  'absit',
  'abuzz',
  'abyss',
  'achoo',
  'acids',
  'acrid',
  'actin',
  'actor',
  'acute',
  'adage',
  'addle',
  'adieu',
  'adios',
  'adlib']  )

# Test 19
L19 = ['added', 'aided', 'audio', 'audit', 'bided', 'count', 'mount']
nL19 = makeNeighborLists(L19)
tests.append(getIsolatedNodes(L19, nL19)==[])
########################################################


########################################################
## getIsolatedEdges  
########################################################
# Test 20
L20 = ['aided', 'bided', 'sided', 'tided']
nL20 = makeNeighborLists(L20)
tests.append(getIsolatedEdges(L20, nL20)==[])


# Test 20
L20 = ['abbey', 'added', 'aided', 'audio', 'audit', 'bided', 'young']
nL20 = makeNeighborLists(L20)
tests.append(getIsolatedEdges(L20, nL20)==[['audio', 'audit']])

# Test 21
L21 = ['audio', 'audit', 'count', 'mount', 'pound','sound']
nL21 = makeNeighborLists(L21)
tests.append(getIsolatedEdges(L21, nL21)==[['audio', 'audit'],['count','mount'],['pound','sound']])
########################################################


########################################################
## sortByDegree  
########################################################
# Test 22
L22 = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided', 'sided', 'tided']
tests.append(sortByDegree(L22, makeNeighborLists(L22))== ['added',
  'aider',
  'aides',
  'anded',
  'ailed',
  'aimed',
  'aired',
  'bided',
  'sided',
  'tided']
)

# Test 23
L23 = ['added', 'aided', 'bided']
tests.append(sortByDegree(L23, makeNeighborLists(L23))== ['added', 'bided', 'aided']
)

# Test 24
L24 = ['added', 'bided', 'clean', 'cream']
tests.append(sortByDegree(L24, makeNeighborLists(L24))== ['added', 'bided', 'clean', 'cream']
)

# Test 25
L25 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
tests.append(sortByDegree(L25, makeNeighborLists(L25))== ['joked', 'yikes', 'yokel', 'jokes', 'yokes']
)
########################################################



########################################################
## degreeDistribution  
########################################################
# Test 26
L26 = ['joked', 'jokes', 'yikes', 'yokel', 'yokes']
tests.append(degreeDistribution(L26, makeNeighborLists(L26))==[0, 3, 1, 1] 
)

# Test 27
L27 = ['added', 'aided', 'bided']
tests.append(degreeDistribution(L27, makeNeighborLists(L27))==[0, 2, 1] 
)

# Test 28
L28 = ['added', 'aider', 'aides', 'ailed', 'aimed', 'aired', 'anded', 'bided', 'sided', 'tided']
tests.append(degreeDistribution(L28, makeNeighborLists(L28))==[0, 4, 6] 
)

# Test 29
L29 = ['apple', 'books', 'table', 'chive', 'video', 'audio', 'grape']
tests.append(degreeDistribution(L29, makeNeighborLists(L29))==[7] 
)
########################################################


# Output the test results
i = 0
for result in tests:
    if not result:
        print("Test", i + 1, "failed")
    i = i + 1

print("Testing complete")
    
