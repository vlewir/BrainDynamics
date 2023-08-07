import numpy as np

#usage: python calculate_over_all_ROI.py

to = 18
ROIs = 85

string = "log_ROI_"

for k in range(ROIs):

	i = 0
	columns = np.loadtxt(string + str(i) + ".txt")
	matrix = columns[:,k:k+1]

	size = float(len(columns[:,k:k+1]))

	for i in range(1,to):
		columns = np.loadtxt(string + str(i) + ".txt")
		matrix = np.column_stack((matrix, columns[:,k:k+1]))

	median = []
	Tippett = []

	for i in range(int(size)):
		median += [np.median(matrix[i])]
		Tippett += [np.amin(matrix[i])]

	first_median = median[0]
	first_Tippett = Tippett[0]

	print('{:.10f} {:.10f}'.format(np.size(np.where(median[1:] <= first_median))/(size-1), np.size(np.where(Tippett[1:] <= first_Tippett))/(size-1)))
