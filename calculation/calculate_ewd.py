from igraph import *
import numpy as np
import sys

#usage: python calculate_ewd.py filelist

filelist = np.loadtxt(sys.argv[1], dtype=str)

bin_size = 30

edge_size = 3570

name = ["Control","EtOH","TP1","TP2"]

all_max = 1.0
all_min = -1*all_max

all_min = np.round(all_min,2)
all_max = np.round(all_max,2)

for n in name:
	print(all_min, all_max)

# -----

for n in name:

	bins = np.linspace(all_min,all_max,bin_size+1)

	counter = 0
	
	distribution = np.zeros((edge_size,bin_size))

	for filen in filelist:
		
		if (n in filen):
			counter += 1
			
			source, target, ns = np.loadtxt(filen, unpack=True)
			
			ns = np.array(ns)
			
			for ii in range(len(ns)):
				values, bbins = np.histogram(ns[ii], bins=bins)
				
				distribution[ii] += values

	distribution = distribution/counter
	
	for ii in range(edge_size):
		print(*distribution[ii])
