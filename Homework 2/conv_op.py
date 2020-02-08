import numpy as np
from scipy import signal
from pprint import pprint

if __name__ == "__main__":
	I = np.array([
		[0, 1, 1, 0, 0],
		[0, 1, 1, 1, 0],
		[1, 1, 1, 1, 0],
		[0, 1, 1, 1, 0],
		[0, 0, 1, 0, 0]
	])

	J = np.array([
		[0, -1, 0],
		[-1, 4, -1],
		[0, -1, 0]
	])

	print("I = ")
	pprint(I)
	print("J = ")
	pprint(J)
	print("I * J = ")
	IconvJ = signal.convolve2d(
		I, J,
		mode="same",
		boundary="fill", fillvalue=0)
	pprint(IconvJ)
