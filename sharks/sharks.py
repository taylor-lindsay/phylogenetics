#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Monday Dec 7 10:02:10 2020

@author: Taylor Lindsay 
    
This python code uses the complete mitochondrial genome of six shark species. The alignment has been run in MUSCLE and is entitled sharks.aln. 
     
"""

# import packages 

import Bio as Bio
from Bio import AlignIO
from Bio import Phylo
import matplotlib
import matplotlib.pyplot as plt

# read the file 

with open("sharks.aln","r") as aln: 
    alignment = AlignIO.read(aln,"clustal")
#print(type(alignment)) 


# Open the distance calculator and create a distance matrix 

from Bio.Phylo.TreeConstruction import DistanceCalculator 
calculator = DistanceCalculator('identity')
distance_matrix = calculator.get_distance(alignment)
#print(distance_matrix)


# Open the tree constructor and build a tree 

from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
constructor = DistanceTreeConstructor(calculator)
shark_tree = constructor.build_tree(alignment)
shark_tree.rooted = True
#print(shark_tree)
Phylo.write(shark_tree, "shark_tree.xml", "phyloxml")


# Create the tree figure 

Phylo.draw_ascii(shark_tree)

fig = plt.figure(figsize=(13, 5), dpi=100) # create figure & set the size 
matplotlib.rc('font', size=12)             # fontsize of the leaf and node labels 
matplotlib.rc('xtick', labelsize=10)       # fontsize of the tick labels
matplotlib.rc('ytick', labelsize=10)       # fontsize of the tick labels
#turtle_tree.ladderize()		   # optional: re-order the tree 	
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(shark_tree, axes=axes)

# save the file 

plt.savefig("shark_cladogram")


