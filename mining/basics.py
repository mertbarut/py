from math import factorial
from statistics import mean
import numpy as np
from numpy import array, dot
from scipy import linalg
import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

from pylab import *

if __name__ == "__main__":
	A = np.array([1, 2, 3, 4, 5])
	B = np.array([20, 30, 40, 50, 60])
	C = A + B
	print(C)

	M1 = np.matrix([
		[2, 3],
		[-1, 5]
	])
	
	M2 = np.matrix([
		[1, 2],
		[-10, 5.4]
	])

	M3 = M2 * M1
	print(M3)

	M3 = M3.transpose()
	print(M3)

	x = array([
		[1, 1],
		[1, 2],
		[1, 3],
		[1, 4]
	])

	y = array([
		[1],
		[2],
		[3],
		[4]
	])

	n = linalg.inv(dot(x.T, x))
	k = dot(x.T, y)

	coef = dot(n, k)
	print(coef)

	a = np.arange(10)
	print(a[2:6])
	print(a[1:9:3])

	b = np.array([
		np.arange(4),
		2 * np.arange(4)
		])
	print(b)
	print(b.shape)

	print(b[:1, :]) #rows, columns

	array1 = np.array([14.1, 15.2, 16.3])
	series1 = pd.Series(array1)
	print(series1)

	features = {
		'limbs': [0, 4, 4, 4, 8],
		'herbivore': ['No', 'No', 'Yes', 'Yes', 'No']}

	animals = ['Python', 'Iberian Lynx', 'Giant Panda', 'Field Mouse', 'Octobus']

	df = pd.DataFrame(features, index = animals)
	print(df)

	print(df['limbs'][2:5])
	print(df.loc['Python'])

	print(df['limbs'].describe())
	print(df['herbivore'].describe())

	df['class'] = ['reptile', 'mammal', 'mammal', 'mammal', 'mollusc']

	grouped = df['class'].groupby(df['herbivore'])
	print(grouped.groups)
	print(grouped.size())
	print(df['limbs'].groupby(df['herbivore']).aggregate(mean))

	x = np.linspace(1, 16, 16, dtype = int)
	print(x)
	y1 = np.linspace(1, 1, 16, dtype = int)
	y2 = log2(x)
	y3 = x
	y4 = log2(x) * x
	y5 = x**2
	y6 = 2**x

	fig, ax = plt.subplots()
	ax.plot(x, y1, 'r',		label = r"$y_1 = 1$", linewidth = 2)
	ax.plot(x, y2, 'k--',	label = r"$y_2 = log(x)$", linewidth = 2)
	ax.plot(x, y3, 'g',		label = r"$y_3 = x$", linewidth = 2)
	ax.plot(x, y4, 'b',		label = r"$y_4 = log(x) * x$", linewidth = 2)
	ax.plot(x, y5, 'c',		label = r"$y_5 = x^2$", linewidth = 2)
	#ax.plot(x, y6, 'p',		label = r"$y_6 = 2^x$", linewidth = 2)
	ax.legend(loc = 2)
	ax.set_xlabel(r"$x$", fontsize = 18)
	ax.set_xlabel(r"$y$", fontsize = 18)
	ax.set_title("O(n) plot")
	fig.savefig("../plots/o_n.png")





