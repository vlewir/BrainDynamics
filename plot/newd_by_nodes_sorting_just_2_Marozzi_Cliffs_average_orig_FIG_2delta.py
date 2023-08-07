import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import sys
import os

#usage: python newd_by_nodes_sorting_just_2_Marozzi_Cliffs_average_orig_FIG_2delta.py MaxAbs 30 MaxAbs_newds.txt ChList.txt MaxAbs_newds_sorting_index_ltof.txt MaxAbs_Cliffs_average_newds_Control_EtOH.txt MaxAbs_newds_Marozzi_EtOH_Control.txt

name = sys.argv[1]

bin_size = int(sys.argv[2])

filename = sys.argv[3]

cl = sys.argv[4]

sorting = sys.argv[5]

ED_average = sys.argv[6]

Marozzi = sys.argv[7]

ED_values = np.loadtxt(ED_average)

ED_values *= -1.0 # switch order

pvalues = np.loadtxt(Marozzi)

data = np.loadtxt(filename, skiprows=4)

vmax = np.round(np.max(data),2)

ticks = np.loadtxt(cl, dtype=str)

sorting_index = np.loadtxt(sorting, dtype=int)

bin_borders = np.loadtxt(filename, usecols=[0,1])

bin_borders = bin_borders[:4:]

begin = 0
end = 85

title = name

if (bin_size == 30):
	fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(40,50))
	title += " : 30 bins"


if ("ftol" in sorting):
	title += " : first to last"
else:
	title += " : last to first"

fontsize = 80

matplotlib.rcParams.update({"font.size" : fontsize})
matplotlib.rcParams['font.family'] = 'arial'


fig.tight_layout(rect=[0.13, 0.07, 0.88, 0.95], w_pad=3, h_pad=8.0)

# names = ["G1 - control - part 1\n", "G1 - EtOH - part 2\n"]

names = ["G1 - control\n", "G1 - EtOH\n"]

# names = ["G2 - tp1\n", "G2 - tp2\n"]

# names = ["G1 - control\n", "G2 - tp1\n"]

# names = ["G2 - tp2\n", "G1 - EtOH\n"]

# names = ["G1 - control\n", "G2 - tp2\n"]

# names = ["G1 - EtOH\n", "G1 - control\n"]

# names = ["G1 - EtOH\n", "G2 - tp1\n"]

# names = ["G1 - EtOH\n", "G2 - tp2\n"]

# names = ["G2 - tp1\n", "G1 - control\n"]

# names = ["G2 - tp1\n", "G1 - EtOH\n"]

# names = ["G2 - tp2\n", "G1 - control\n"]

# names = ["G2 - tp2\n", "G2 - tp1\n"]

ax = plt.subplot(144)

ax.set_position([0.89, 0.0925, 0.04, 0.839])

plt.title("$p$\n")

tmp = pvalues[:,1]

for tip in range(len(tmp)):
	if (tmp[tip] < 0.05):
		tmp[tip] = 1
	else:
		tmp[tip] = 0

Tippet = np.expand_dims(tmp, axis=1)

plt.imshow(Tippet[sorting_index], cmap=cm.binary, interpolation='nearest', aspect='auto', vmin=0.0, vmax=1.0)

plt.yticks([])

plt.xticks([])

ax = plt.subplot(143)

ax.set_position([0.8, 0.0925, 0.06, 0.839])

plt.title("$\delta_n \delta_p$\n")

print(np.amin(ED_values), np.amax(ED_values))

im = plt.imshow(ED_values[sorting_index], cmap=cm.coolwarm, interpolation='nearest', aspect='auto', vmin=-0.5, vmax=0.5)

plt.yticks([])

plt.xticks([])

cbaxes = fig.add_axes([0.7822, 0.03, 0.17, 0.03])

cbar = plt.colorbar(im, cax = cbaxes, orientation='horizontal', ticks=np.round(np.linspace(-0.5, 0.5, 2),2))

cbar.ax.set_xticklabels(['-0.5', '0.5 $\delta$'])

for i in range(1,-1,-1):
	
	offset = i*end

	subplt = 141+i

	ax = plt.subplot(subplt)

	if (subplt == 142):
		ax.set_position([0.55, 0.0925, 0.2, 0.839])

	ax.set_title(names[i])
	
	im = plt.imshow(data[begin+offset:end+offset:][sorting_index], interpolation='nearest', aspect="auto", cmap=cm.coolwarm, vmin=0.0, vmax=vmax)

	if (i == 0):
		plt.ylabel("rat 85 nodes")

		plt.yticks(np.arange(begin,end,2),ticks[sorting_index][::2])

		ax2 = ax.twinx()

		ax2.set_position([0.18, 0.0925, 0.2, 0.839])

		plt.ylim(0,85)

		plt.yticks(np.arange(1.5,85,2),ticks[sorting_index][1::2][::-1])

	else:
		plt.yticks([])

	if (bin_size == 30):
		plt.xticks([0,29],np.around(bin_borders[i],2))

	ax.tick_params(axis='x', which='major', pad=30)

cbaxes = fig.add_axes([0.19, 0.03, 0.49, 0.03])

cbar = plt.colorbar(im, cax = cbaxes, orientation='horizontal', ticks=np.round(np.linspace(0.0, vmax, 2),2))

cbar.ax.set_xticklabels(['0', '0.25'])

sorting_type = sorting.split(".")[0].split("_")[-1]

plt.savefig(os.path.basename(filename).split(".")[0] + "_" + sorting_type + "_just_2_Marozzi_Cliffs_average_FIG.png")
