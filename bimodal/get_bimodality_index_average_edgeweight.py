import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys

#usage: python get_bimodality_index_average_edgeweight.py

filelist = np.loadtxt("Control_filelist.txt", dtype=str)

source, target, ew = np.loadtxt("P02_SCAMaxAbs-IRQK0.0-1-Control-91-ValAtTimeOffset_weighted.txt", unpack=True)

distribution = {}

edge_number = 3570

matplotlib.rcParams.update({'font.size': 110})
matplotlib.rcParams['font.family'] = 'arial'
matplotlib.rcParams['axes.linewidth'] = 2
matplotlib.rcParams['xtick.major.size'] = 10
matplotlib.rcParams['xtick.major.width'] = 2
matplotlib.rcParams['ytick.major.size'] = 10
matplotlib.rcParams['ytick.major.width'] = 2

plt.figure(figsize=(40,30))

ax = plt.gca()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout(rect=[0.05, 0.03, 1.05, 1.07])

for i in range(edge_number):
	distribution[i] = [(source[i], target[i])]

# -----

loop = 0

for file in filelist:
	if ("Control" in file):
		
		loop += 1

		source, target, ew = np.loadtxt(file, unpack=True)
		
		for i in range(edge_number):
			distribution[i] += [ew[i]]

# -----

for i in range(edge_number):
	negative = np.sum(np.array(distribution[i][1:]) < 0)
	size = len(distribution[i][1:])

	distribution[i] += [negative/float(size-negative)]

	# print(distribution[i])

# -----

bimodality_index = []
average_edgeweight = []

for i in range(edge_number):
	bimodality_index += [distribution[i][-1]]
	average_edgeweight +=[np.mean(distribution[i][1:-1])]

bimodality_index = np.array(bimodality_index)
average_edgeweight = np.array(average_edgeweight)

from scipy.optimize import curve_fit
from scipy import stats

rho, _ = stats.spearmanr(bimodality_index, average_edgeweight)

for ii in range(len(bimodality_index)):
	print(bimodality_index[ii], average_edgeweight[ii])

plt.plot(bimodality_index, average_edgeweight, '.', markersize=30, label='Spearman correlation: {:.2f}'.format(rho))

plt.xticks(color='white')

plt.xlabel("bimodality index (negative/positive)", labelpad=30, color='white')
plt.ylabel("average edge weight", labelpad=70)

plt.legend()

plt.savefig("bimodality_index_average_edgeweight.png")
