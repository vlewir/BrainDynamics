import numpy as np
from igraph import Graph, Plot
from igraph.drawing.text import TextDrawer
import cairocffi
import matplotlib.colors

#usage: python backbone_colored_circle_just_selected.py

sorting_index = np.loadtxt('../MaxAbs_edds_sorting_index_ltof.txt', dtype=int)

chList = np.loadtxt('../ChList.txt', dtype=str)

chList_color = np.loadtxt('../ChList_colored.txt', dtype=str)

source, target = np.loadtxt('../edgelist.txt', unpack=True, dtype=int)

data = np.loadtxt('../MaxAbs_edds_just_3.txt', skiprows=3)

data = data[:3570,:]

g = Graph(n=85)

g.vs['name'] = chList
g.vs['label'] = g.vs['name']

g.vs['color'] = ['#{}33'.format(color) for color in chList_color[:,1]]

coloring = {'#ff0000': 0, '#ff9900': 0, '#ffe599': 0, '#0000ff': 0, '#9900ff': 0, '#ff00ff': 0, '#00ff00': 0, '#38761d': 0}

for i in range(3570):
	if (np.sum(data[i,][:14]) == 0):

		g.vs[source[i]-1]['color'] = g.vs[source[i]-1]['color'].replace('33', 'ff')
		g.vs[target[i]-1]['color'] = g.vs[target[i]-1]['color'].replace('33', 'ff')

		g.add_edge(source[i]-1, target[i]-1)

		# cortical
		if ( (g.vs[source[i]-1]['color'] == '#ff0000ff') and (g.vs[target[i]-1]['color'] == '#ff0000ff')):
			if (g.vs[source[i]-1]['name'][:-2] == g.vs[target[i]-1]['name'][:-2]):
				g.es[-1]['color'] = '#ff0000'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'R') and (g.vs[target[i]-1]['name'][-1] == 'L') ):
				g.es[-1]['color'] = '#ff9900'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'L') and (g.vs[target[i]-1]['name'][-1] == 'R') ):
				g.es[-1]['color'] = '#ff9900'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'R') and (g.vs[target[i]-1]['name'][-1] == 'R') ):
				g.es[-1]['color'] = '#ffe599'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'L') and (g.vs[target[i]-1]['name'][-1] == 'L') ):
				g.es[-1]['color'] = '#ffe599'
				coloring[g.es[-1]['color']] += 1

		# subcortical
		elif ( (g.vs[source[i]-1]['color'] == '#92d050ff') and (g.vs[target[i]-1]['color'] == '#92d050ff')):
			if (g.vs[source[i]-1]['name'][:-2] == g.vs[target[i]-1]['name'][:-2]):
				g.es[-1]['color'] = '#0000ff'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'R') and (g.vs[target[i]-1]['name'][-1] == 'L') ):
				g.es[-1]['color'] = '#9900ff'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'L') and (g.vs[target[i]-1]['name'][-1] == 'R') ):
				g.es[-1]['color'] = '#9900ff'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'R') and (g.vs[target[i]-1]['name'][-1] == 'R') ):
				g.es[-1]['color'] = '#ff00ff'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'L') and (g.vs[target[i]-1]['name'][-1] == 'L') ):
				g.es[-1]['color'] = '#ff00ff'
				coloring[g.es[-1]['color']] += 1

		else:
			if ( (g.vs[source[i]-1]['name'][-1] == 'R') and (g.vs[target[i]-1]['name'][-1] == 'R') ):
				g.es[-1]['color'] = '#00ff00'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'L') and (g.vs[target[i]-1]['name'][-1] == 'L') ):
				g.es[-1]['color'] = '#00ff00'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'R') and (g.vs[target[i]-1]['name'][-1] == 'L') ):
				g.es[-1]['color'] = '#38761d'
				coloring[g.es[-1]['color']] += 1
			elif ( (g.vs[source[i]-1]['name'][-1] == 'L') and (g.vs[target[i]-1]['name'][-1] == 'R') ):
				g.es[-1]['color'] = '#38761d'
				coloring[g.es[-1]['color']] += 1

		print(list(coloring.keys()).index(g.es[-1]['color']))
	else:
		print(8)
