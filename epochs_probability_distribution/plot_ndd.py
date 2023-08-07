import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#usage: python plot_ndd.py

# node_name = 'PrL_L'
node_name = 'CPu_R'

data = np.loadtxt('ndds_ED_' + node_name + ".txt")

name = ["epoch 1","epoch 2","epoch 3","epoch 4","epoch 5","G1"]

markers = ["s", "o", "^", "D", "p", "d"]

matplotlib.rcParams.update({'font.size': 110})
matplotlib.rcParams['font.family'] = 'arial'
matplotlib.rcParams['axes.linewidth'] = 2
matplotlib.rcParams['xtick.major.size'] = 10
matplotlib.rcParams['xtick.major.width'] = 2
matplotlib.rcParams['ytick.major.size'] = 10
matplotlib.rcParams['ytick.major.width'] = 2

plt.figure(figsize=(40,20))

ax = plt.gca()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.tight_layout(rect=[0.05, 0.03, 1.05, 0.98])

for i in range(len(data)):
	if (i == 5):
		plt.plot(data[i][14:], ".-", color="#d62728", label=name[i], marker=markers[i], markersize=20, linewidth=10)
	elif (i == 3):
		plt.plot(data[i][14:], ".-", color="#9467bd", label=name[i], marker=markers[i], markersize=15, linewidth=4)
	elif (i == 4):
		plt.plot(data[i][14:], ".-", color="#8c564b", label=name[i], marker=markers[i], markersize=15, linewidth=4)
	else:
		plt.plot(data[i][14:], ".-", label=name[i], marker=markers[i], markersize=15, linewidth=4)

plt.title('rat ' + node_name + "\n", y=0.92)

plt.ylim([0,0.45])

plt.ylabel("probability distribution\n", labelpad=-50)

if (node_name == 'PrL_L'):
	plt.xlabel("\ndistance between node pairs", labelpad=-70)
	plt.xticks([0,15],[0.0, 1.54])
else:
	plt.xlabel("\ndistance between node pairs", labelpad=-70, color='white')
	plt.xticks([0,15],[0.0, 1.54], color='white')
plt.legend()

plt.savefig('ndds_ED_' + node_name + ".png")
