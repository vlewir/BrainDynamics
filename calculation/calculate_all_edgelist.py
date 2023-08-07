import numpy as np
import sys
import os

#usage: python calculate_all_edgelist.py filelist

filelist = np.loadtxt(sys.argv[1], dtype=str)

for f in filelist:
	os.system("python csv_to_edgelist.py " + f + " > " + f[:-4] + "_ln_weighted.txt")
	#os.system("python csv_to_edgelist.py " + f + " > " + f[:-4] + "_weighted.txt")
