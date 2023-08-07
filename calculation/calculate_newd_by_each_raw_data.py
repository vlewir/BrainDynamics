from igraph import *
import numpy as np
import sys

#usage: python calculate_newd_by_each_raw_data.py filelist

filelist = np.loadtxt(sys.argv[1], dtype=str)

node_to = 86

names = ["Control","EtOH","TP1","TP2"]

global_max = 1.0
global_min = -1*global_max

global_min = np.round(global_min,2)
global_max = np.round(global_max,2)

print(global_min, global_max)

# -----

for name in names:

	for file in filelist:

		if (name in file):
			
			g = Graph(n=node_to, directed=True)
			
			edges = np.loadtxt(file)
			
			weights = edges[:,2]
			edges = [(int(e[0]),int(e[1])) for e in edges[:,[0,1]]]
			
			g.add_edges(edges)
			
			g.delete_vertices(g.vs.select(_degree=0))
			
			g.vs["name"] = np.arange(1,node_to)
			g.es["weight"] = weights

			res = []

			for v in g.vs:
				eee = g.incident(v, mode=ALL)
				
				res_row = []
				
				for ee in eee:
					res_row += [g.es[ee]["weight"]]
				
				res += [res_row]

			res = np.array(res)

			for row in res:
				print(*row)
