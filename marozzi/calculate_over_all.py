import numpy as np

#usage: python calculate_over_all.py

to = 18

string = "log_"

i = 0
counter, column = np.loadtxt(string + str(i) + ".txt", unpack=True)
matrix = column

size = float(len(column))

for i in range(1,to):
	counter, column = np.loadtxt(string + str(i) + ".txt", unpack=True)
	matrix = np.column_stack((matrix, column))

median = []
Tippett = []

for i in range(int(size)):
	median += [np.median(matrix[i])]
	Tippett += [np.amin(matrix[i])]

first_median = median[0]
first_Tippett = Tippett[0]

print("median:  %.10f" % (np.size(np.where(median[1:] <= first_median))/(size-1)))
print("Tippett: %.10f" % (np.size(np.where(Tippett[1:] <= first_Tippett))/(size-1)))
