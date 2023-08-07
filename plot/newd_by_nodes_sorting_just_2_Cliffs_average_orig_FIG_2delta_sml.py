import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import sys
import os

#usage: python newd_by_nodes_sorting_just_2_Cliffs_average_orig_FIG_2delta_sml.py MaxAbs 30 MaxAbs_newds.txt ChList.txt MaxAbs_newds_sorting_index_ltof.txt MaxAbs_Cliffs_average_newds_Control_EtOH.txt

name = sys.argv[1]

bin_size = int(sys.argv[2])

filename = sys.argv[3]

cl = sys.argv[4]

sorting = sys.argv[5]

ED_average = sys.argv[6]

ED_values = np.loadtxt(ED_average)

ED_values *= -1.0 # switch order

data = np.loadtxt(filename, skiprows=4)

vmax = np.round(np.max(data),2)

ticks = np.loadtxt(cl, dtype=str)

sorting_index = np.loadtxt(sorting, dtype=int)

bin_borders = np.loadtxt(filename, usecols=[0,1])

bin_borders = bin_borders[:4:]

begin = 0
end = 85

title = name

fontsize = 80

matplotlib.rcParams.update({"font.size" : fontsize})
matplotlib.rcParams['font.family'] = 'arial'

if (bin_size == 30):
	fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(40,50))
	title += " : 30 bins"


if ("ftol" in sorting):
	title += " : first to last"
else:
	title += " : last to first"


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

ax.set_position([0.89, 0.0925, 0.06, 0.839])

plt.title("$\delta_n \delta_p$\n")

tmp = ED_values.copy()

tmp = np.abs(tmp)

for tip in range(len(tmp)):
	if (tmp[tip][0] >= 0.43):
		tmp[tip][0] = 3
	elif (tmp[tip][0] >= 0.28):
		tmp[tip][0] = 2
	elif (tmp[tip][0] >= 0.11):
		tmp[tip][0] = 1
	else:
		tmp[tip][0] = 0

	if (tmp[tip][1] >= 0.43):
		tmp[tip][1] = 3
	elif (tmp[tip][1] >= 0.28):
		tmp[tip][1] = 2
	elif (tmp[tip][1] >= 0.11):
		tmp[tip][1] = 1
	else:
		tmp[tip][1] = 0

cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ['#ffffff', '#ff7f0e', '#2ca02c', '#d62728'])

plt.imshow(tmp[sorting_index], cmap=cmap, interpolation='nearest', aspect='auto', vmin=0.0, vmax=3.0)

plt.yticks([])

plt.xticks([])

plt.text(1.9, 53, 'small', color='#ff7f0e', rotation=90, weight='bold')
plt.text(1.9, 45, 'medium', color='#2ca02c', rotation=90, weight='bold')
plt.text(1.9, 35, 'large', color='#d62728', rotation=90, weight='bold')

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

plt.savefig(os.path.basename(filename).split(".")[0] + "_" + sorting_type + "_just_2_Cliffs_average_FIG_sml.png")
