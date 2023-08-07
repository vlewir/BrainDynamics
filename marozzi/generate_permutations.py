import numpy as np
import sys

#usage: python generate_permutation.py 36 100000

N = int(sys.argv[1])

B = int(sys.argv[2])

for i in range(B):
	perm = np.random.permutation(N)
	
	print(*perm)
