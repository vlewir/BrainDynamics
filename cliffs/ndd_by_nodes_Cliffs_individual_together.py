import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import sys
import os

#usage: python ndd_by_nodes_Cliffs_individual_together.py MaxAbs ChList.txt MaxAbs_ndds_ln_by_each_raw_data.txt

def ED(A,B):

	ret = []

	for i in range(A.shape[0]):

		nnn = A.shape[1]

		S = 0
		for d1 in A[i]:
			S += np.sum(np.sign(d1 - B[i]))
		S /= (nnn*nnn)

		ret += [S]

	ret = np.asarray(ret)

	return ret

name = sys.argv[1]

cl = sys.argv[2]

bins = sys.argv[3]

ticks = np.loadtxt(cl, dtype=str)

lines = [line.rstrip('\n') for line in open(bins)]

bin_min, bin_max = lines[0].split(" ")

bin_min = np.round(float(bin_min),2)
bin_max = np.round(float(bin_max),2)

fontsize = 36

matplotlib.rcParams.update({'font.size': fontsize})

names = ["Control", "EtOH"]
tnames = {}
tnames["Control"] = "G1 - control"
tnames["EtOH"] = "G1 - EtOH"

#names = ["TP1", "TP2"]
#tnames = {}
#tnames["TP1"] = "G2 - tp1"
#tnames["TP2"] = "G2 - tp2"

# -----

for i in range(1,19):

	subplot_index = 0

	for n in names:
		data = np.loadtxt("../" + name + "/" + n + "/" + str(i) + ".txt")

		if (subplot_index == 0):
			A = data
			plt.subplots_adjust(right=0.9)
		else:
			B = data

		subplot_index += 3

	if i==1:
		all_A = A
		all_B = B
	else:
		all_A = np.append(all_A,A,1)
		all_B = np.append(all_B,B,1)

ress = ED(all_A,all_B)

for i in ress:
	print(i)
