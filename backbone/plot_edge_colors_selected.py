import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm

#usage: python plot_edge_colors_selected.py

edge_colors = np.loadtxt('edge_colors_selected.txt')

data = np.loadtxt('../MaxAbs_edds_just_3.txt', skiprows=3)

data = data[:3570,:]

sorting_index = np.loadtxt('../MaxAbs_edds_sorting_index_ltof.txt', dtype=int)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(30,40))

fontsize = 70

plt.rcParams.update({'font.size': fontsize})
plt.rcParams.update({'font.family': 'arial'})

my_cmap = LinearSegmentedColormap.from_list('my_cmap', ['#ff0000', '#ff9900', '#ffe599', '#0000ff', '#9900ff', '#ff00ff', '#00ff00', '#38761d', '#ffffff'], N=9)

edge_colors = np.expand_dims(edge_colors, axis=1)

im = axes[0].imshow(edge_colors[sorting_index], aspect='0.003', cmap=my_cmap)

axes[0].set_xticks([])
axes[0].set_yticks([])

cbar = plt.colorbar(im, ax=axes[0], fraction=0.06, pad=-0.8, aspect=60, ticks=[2.5, 5.2, 6.87, 8])
cbar.ax.set_yticklabels(['└─── cortical ───┘', '└── subcortical ──┘', '└─ cortico-\nsubcortical ─┘', 'bimodal'], rotation=90)

im = axes[1].imshow(data[sorting_index], aspect='auto', cmap=cm.coolwarm, vmin=0.0, vmax=0.5)

plt.title('G1\n')
plt.ylabel('rat 3570 edges', fontsize=fontsize, labelpad=30)

axes[1].set_yticks([])
plt.xticks([0,29],[-1.0,1.0], fontsize=fontsize)

plt.colorbar(im, ax=axes[1], boundaries=np.linspace(0.0, 0.84, 1000), ticks=np.round(np.linspace(0.0, 0.84, 10),2), fraction=0.06, aspect=60, pad=0.2)

plt.tight_layout()

plt.savefig('edge_colors_selected.png')
