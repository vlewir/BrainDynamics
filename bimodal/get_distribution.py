import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sys

#usage: python get_distribution.py

filelist = np.loadtxt("Control_filelist.txt", dtype=str)

source, target, ew = np.loadtxt("P02_SCAMaxAbs-IRQK0.0-1-Control-91-ValAtTimeOffset_weighted.txt", unpack=True)

distribution = {}

edge_number = 3570

matplotlib.rcParams.update({'font.size': 80})
matplotlib.rcParams['font.family'] = 'arial'

fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(30,16))

fig.tight_layout(rect=[0, -0.1, 1, 0.93])

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

	distribution[i] += [negative]
	distribution[i] += [size]
	distribution[i] += [negative/float(size)]

	# print(distribution[i])

# -----


count = []

for i in range(edge_number):
	count += [distribution[i][-1:][0]]

positive = np.sum(np.array(count) == 0.0)
negative = np.sum(np.array(count) == 1.0)
bimodal = np.sum((np.array(count) != 0.0) & (np.array(count) != 1.0))

print("positive: ", positive, " -- ", positive/float(edge_number))
print("negative: ", negative, " -- ", negative/float(edge_number))
print("bimodal:  ", bimodal, " -- ", bimodal/float(edge_number))
print()

a = []
a += [positive/float(edge_number)]
a += [negative/float(edge_number)]
a += [bimodal/float(edge_number)]

plt.subplot(121)
plt.title("proportion\nof links\n", y=0.9)
plt.pie(a, colors=[(0.705673,0.015556,0.150233), (0.234377,0.305542,0.759680), "white"], startangle=90, wedgeprops={"edgecolor":"0",'linewidth': 1,'linestyle': 'dashed', 'antialiased': True})

labels = ["positive:  10.6%", "negative: 0%", "bimodal:  89.4%"]
plt.legend(labels=labels, bbox_to_anchor=(0.4, -0.08, 0.5, 0.5))

bimodal_positive = 0
bimodal_negative = 0
bimodal_all = 0

for i in range(edge_number):
	act = distribution[i] 
	if ((act[-1:][0] != 0.0) and (act[-1:][0] != 1.0)):
		bimodal_negative += act[-3:-2][0]
		bimodal_all += act[-2:-1][0]

bimodal_positive = bimodal_all - bimodal_negative

bimodal_positive /= loop
bimodal_all /= loop
bimodal_negative /= loop

print("bimodal all:      ", bimodal_all)
print("bimodal positive: ", bimodal_positive, " -- ", bimodal_positive/float(bimodal_all))
print("bimodal negative: ", bimodal_negative, " -- ", bimodal_negative/float(bimodal_all))

b = []
b += [bimodal_positive/float(bimodal_all)]
b += [bimodal_negative/float(bimodal_all)]

plt.subplot(122)
plt.title("proportion of time\nfor bimodal links\n", y=0.9)
plt.pie(b, colors=[(0.705673,0.015556,0.150233), (0.234377,0.305542,0.759680)], startangle=90, wedgeprops={"edgecolor":"0",'linewidth': 1,'linestyle': 'dashed', 'antialiased': True})

labels = ["positive:  89.5%", "negative: 10.5%"]
plt.legend(labels=labels, bbox_to_anchor=(0.6, -0.205, 0.5, 0.5))

plt.subplots_adjust(wspace=0, hspace=0)

plt.savefig("individual.png")