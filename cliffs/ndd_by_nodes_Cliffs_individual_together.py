import numpy as np
import sys

#usage: python ndd_by_nodes_Cliffs_individual_together.py MaxAbs

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

names = ["Control", "EtOH"]

#names = ["TP1", "TP2"]

# -----

for i in range(1,19):

	subplot_index = 0

	for n in names:
		data = np.loadtxt("../" + name + "/" + n + "/" + str(i) + ".txt")

		if (subplot_index == 0):
			A = data
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
