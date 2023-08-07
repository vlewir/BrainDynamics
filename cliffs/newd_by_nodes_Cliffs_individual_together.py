import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import sys
import os

#usage: python newd_by_nodes_Cliffs_individual_together.py MaxAbs ChList.txt MaxAbs_newds_by_each_raw_data.txt

def ED(A,B):

	ret_p = []
	ret_n = []

	for i in range(A.shape[0]):

		neg_a = A[i][A[i] < 0]
		nneg_a = len(neg_a)

		pos_a = A[i][A[i] >= 0]
		npos_a = len(pos_a)

		S_neg = 0
		for d1 in neg_a:
			neg_b = B[i][B[i] < 0]
			nneg_b = len(neg_b)
			S_neg += np.sum(np.sign(d1 - neg_b))
		
		if ((nneg_a*nneg_b) == 0):
			S_neg = 0.0
		else:
			S_neg /= (nneg_a*nneg_b)

		S_pos = 0
		for d1 in pos_a:
			pos_b = B[i][B[i] >= 0]
			npos_b = len(pos_b)
			S_pos += np.sum(np.sign(d1 - pos_b))
		
		if ((npos_a*npos_b) == 0):
			S_pos = 0.0
		else:
			S_pos /= (npos_a*npos_b)

		ret_p += [S_pos]
		ret_n += [S_neg]

	ret_p = np.asarray(ret_p)
	ret_n = np.asarray(ret_n)

	return ret_p, ret_n

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

# names = ["TP1", "TP2"]
# tnames = {}
# tnames["TP1"] = "G2 - tp1"
# tnames["TP2"] = "G2 - tp2"


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

ress_p, ress_n = ED(all_A,all_B)

for i in range(len(ress_p)):
	print(ress_n[i], ress_p[i])
