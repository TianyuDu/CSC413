import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
	ax1 = plt.subplot()
	w1 = np.linspace(-0.25, 1.25, 100)
	w2 = -2 * w1 + 2
	ax1.plot(w1, w2, linewidth=1, label="$w_2 = -2 w_1 + 2$")
	for i in np.linspace(0, 0.4, 10):
		ax1.arrow(0, 0, 2 * i, i,
			head_width=0.05,
			head_length=0.1,
			fc="b",
			ec="b",
			alpha=0.2
		)
	for i in np.linspace(0, 0.4, 10):
		ax1.scatter(2 * i, i,
			marker="x",
			s=100,
			alpha=1.0
		)
	plt.grid(True)
	plt.legend()
	ax1.set_xlim([-1, 2])
	ax1.set_ylim([-1, 2])
	plt.savefig("./grad_desc.png", dpi=300)
	# plt.show()