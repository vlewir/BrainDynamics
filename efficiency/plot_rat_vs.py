import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#usage: python plot_rat_vs.py

matplotlib.rcParams.update({'font.size': 50})
matplotlib.rcParams['font.family'] = 'arial'
matplotlib.rcParams['axes.linewidth'] = 2
matplotlib.rcParams['xtick.major.size'] = 10
matplotlib.rcParams['xtick.major.width'] = 2
matplotlib.rcParams['ytick.major.size'] = 10
matplotlib.rcParams['ytick.major.width'] = 2

plt.figure(figsize=(30,20))

ax = plt.gca()

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

colors = ['black', 'red', 'green', 'blue', 'black', 'red', 'green', 'blue']

names = ['strong $E_g$', 'strong $E_l$', 'weak $E_g$', 'weak $E_l$']

files = ['control_strong_global.txt', 'control_strong_local.txt', 'control_weak_global.txt', 'control_weak_local.txt', 'etoh_strong_global.txt', 'etoh_strong_local.txt', 'etoh_weak_global.txt', 'etoh_weak_local.txt']

for i in range(8):
	
	mean, std = np.loadtxt(files[i], unpack=True)

	x = range(len(mean))

	if ('control' in files[i]):
		plt.plot(x, mean, color=colors[i], label=names[i], lw=4)
	else:
		plt.plot(x, mean, '--', color=colors[i], lw=4)
	plt.fill_between(x, mean-std, mean+std, color=colors[i], alpha=0.2)

plt.xticks(np.linspace(0,len(mean)-1,5), [0, 0.25, 0.5, 0.75, 1])

plt.xlabel('density', labelpad=30)
plt.ylabel('efficiencies $E_g$, $E_l$', labelpad=30)

plt.title('rat', y=0.9)

lines = ax.get_lines()
legend1 = plt.legend([lines[i] for i in [0,1,2,3]], names, bbox_to_anchor=[0.7,0.77], loc='center', ncol=2, fontsize=60)
legend2 = plt.legend([lines[i] for i in [0,4]], ['Control', 'EtOH'], loc='upper right', fontsize=40)
ax.add_artist(legend1)
ax.add_artist(legend2)

plt.ylim(0,6.5)

plt.tight_layout()

plt.savefig('rat_control_etoh.png')
