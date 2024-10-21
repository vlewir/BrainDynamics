import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import sys
import os

#usage: python ewds_by_nodes_sorting_just_3_fig.py MaxAbs 30 MaxAbs_ewds_just_3.txt MaxAbs_ewds_sorting_index_ltof.txt

name = sys.argv[1]

bin_size = int(sys.argv[2])

filename = sys.argv[3]

sorting = sys.argv[4]

data = np.loadtxt(filename, skiprows=3)

vmax = np.round(np.max(data),2)

sorting_index = np.loadtxt(sorting, dtype=int)

bin_borders = np.loadtxt(filename, usecols=[0,1])

bin_borders = bin_borders[:4:]

begin = 0
end = 3570

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(30,40))	

matplotlib.rcParams.update({'font.size': 70})
matplotlib.rcParams['font.family'] = 'arial'

fig.tight_layout(rect=[0.05, 0.05, 0.88, 0.95], w_pad=3.0, h_pad=8.0)

names = ["G1\n", "G2 - tp1\n", "G2 - tp2\n"]

for i in range(3):
	
	offset = i*end

	subplt = 131+i

	ax = plt.subplot(subplt)

	ax.set_title(names[i])

	max_indices = np.argmax(data, axis=1)
	
	my_cmap = matplotlib.cm.coolwarm

	im = plt.imshow(data[begin+offset:end+offset:][sorting_index], cmap=my_cmap, aspect='auto', vmin=0.0, vmax=0.5)

	if (i == 0):

		plt.ylabel("rat 3570 edges\n")

		plt.yticks([])
	else:
		plt.yticks([])

	if (bin_size == 30):
		plt.xticks([0,29],np.around(bin_borders[i],2))

	ax.tick_params(axis='x', which='major', pad=30)

cbaxes = fig.add_axes([0.88, 0.1, 0.03, 0.8])

plt.colorbar(im, cax = cbaxes, boundaries=np.linspace(0.0, vmax, 1000), ticks=np.round(np.linspace(0.0, vmax, 10),2))

sorting_type = sorting.split(".")[0].split("_")[-1]

plt.savefig(os.path.basename(filename).split(".")[0] + "_" + sorting_type + "_fig.png")
