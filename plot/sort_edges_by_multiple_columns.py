import numpy as np
import operator
import sys

#usage: python sort_edges_by_multiple_columns.py 30 MaxAbs_ewds.txt

bin_size = int(sys.argv[1])

filename = sys.argv[2]

data = np.loadtxt(filename, skiprows=4)

act_data = data[0:3570:]

indexed_data = np.zeros((3570,bin_size+1))

for i in range(len(act_data)):
	indexed_data[i] = np.append(act_data[i],i)

sorted_data = sorted(indexed_data, key=operator.itemgetter(*range(bin_size)), reverse=True)

out = open(filename.split(".")[0] + "_sorting_index_ftol.txt", "w")

for row in sorted_data:
	out.write(str(int(row[bin_size])) + "\n")

out.close()

sorted_data = sorted(indexed_data, key=operator.itemgetter(*range(bin_size-1,-1,-1)), reverse=True)

out = open(filename.split(".")[0] + "_sorting_index_ltof.txt", "w")

for row in sorted_data:
	out.write(str(int(row[bin_size])) + "\n")

out.close()
