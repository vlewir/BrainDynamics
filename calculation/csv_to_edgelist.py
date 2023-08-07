import csv
import sys
import numpy as np

#usage: python csv_to_edgelist.py csv_file

data = list(csv.reader(open(sys.argv[1])))

data = np.array(data, dtype=float)

size = len(data)

for i in range(size):
	for j in range(size):
		if (i < j):
			print(i+1, j+1, -np.log(abs(data[i][j])))
			#print(i+1, j+1, data[i][j])
