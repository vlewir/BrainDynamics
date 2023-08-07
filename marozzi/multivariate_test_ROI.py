import numpy as np
from scipy.stats import mannwhitneyu
from math import factorial
from scipy.spatial import distance
import sys

#usage: python multivariate_test_ROI.py 0

X = np.loadtxt("EtOH_ndds.txt")
Y = np.loadtxt("Control_ndds.txt")

Z = np.concatenate((X, Y))

m = len(X)
n = len(Y)
N = m+n

bins = 30
ROIs = 85 

# -----

euclidean_distance = np.zeros((ROIs,N,N))

for k in range(ROIs):
	for i in range(N):
		for j in range(N):
			begin = k*bins
			end = (k+1)*bins
			euclidean_distance[k][i][j] = distance.euclidean(Z[i][begin:end], Z[j][begin:end])

selected_index = int(sys.argv[1])

to_m = list(set(range(m))-set([selected_index]))
to_N = range(m,N)

for k in range(ROIs):
	lik_m = euclidean_distance[k][selected_index][to_m]
	lik_N = euclidean_distance[k][selected_index][to_N]

	ssum, pvalue = mannwhitneyu(lik_m, lik_N, alternative="less")
	
	print(*pvalue)

# -----

B = 100000

permutations = np.loadtxt("permutations.txt", dtype=int)

for b in range(int(B)):
	perm = permutations[b]

	for k in range(ROIs):
		lik_m = euclidean_distance[k][ perm[selected_index] ][ perm[to_m] ]
		lik_N = euclidean_distance[k][ perm[selected_index] ][ perm[to_N] ]
		
		ssum, pvalue = mannwhitneyu(lik_m, lik_N, alternative="less")
		
		print(*pvalue)

# -----
