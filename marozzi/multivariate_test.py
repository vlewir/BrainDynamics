import numpy as np
from scipy.stats import mannwhitneyu
from math import factorial
from scipy.spatial import distance
import sys

#usage: python multivariate_test.py 0

X = np.loadtxt("EtOH_ndds.txt")
Y = np.loadtxt("Control_ndds.txt")

Z = np.concatenate((X, Y))

m = len(X)
n = len(Y)
N = m+n

# -----

euclidean_distance = np.zeros((N,N))

for i in range(N):
	for j in range(N):
		euclidean_distance[i][j] = distance.euclidean(Z[i], Z[j])

selected_index = int(sys.argv[1])

to_m = list(set(range(m))-set([selected_index]))
lik_m = euclidean_distance[selected_index][to_m]

to_N = range(m,N)
lik_N = euclidean_distance[selected_index][to_N]

ssum, pvalue = mannwhitneyu(lik_m, lik_N, alternative="less")
PJK_0 = pvalue

print(0, PJK_0)

PJK_permutation = []

# -----

B = 1000000

permutations = np.loadtxt("permutations.txt", dtype=int)

for b in range(int(B)):
	perm = permutations[b]

	lik_m = euclidean_distance[ perm[selected_index] ][ perm[to_m] ]
	lik_N = euclidean_distance[ perm[selected_index] ][ perm[to_N] ]

	ssum, pvalue = mannwhitneyu(lik_m, lik_N, alternative="less")

	PJK_permutation += [pvalue]
	print(b+1, pvalue)

# -----
