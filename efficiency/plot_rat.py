import numpy as np
import matplotlib.pyplot as plt
import matplotlib

#usage: python plot_rat.py

matplotlib.rcParams.update({'font.size': 80})
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

colors = ['black', 'red', 'green', 'blue']

names = ['strong $E_g$', 'strong $E_l$', 'weak $E_g$', 'weak $E_l$']

files = ['control_strong_global.txt', 'control_strong_local.txt', 'control_weak_global.txt', 'control_weak_local.txt']

for i in range(4):
	
	mean, std = np.loadtxt(files[i], unpack=True)

	x = range(len(mean))

	plt.plot(x, mean, color=colors[i], label=names[i], lw=4)
	plt.fill_between(x, mean-std, mean+std, color=colors[i], alpha=0.2)

plt.xticks(np.linspace(0,len(mean)-1,5), [0, 0.25, 0.5, 0.75, 1])

plt.xlabel('density', labelpad=30)
plt.ylabel('efficiencies $E_g$, $E_l$', labelpad=30)

plt.title('rat', y=0.9)

plt.ylim(0,7)

plt.tight_layout()

plt.savefig('rat_control.png')
