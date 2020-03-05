import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
	plt.rcParams["figure.figsize"] = (9, 9)
	LAMBDA = 1
	ax1 = plt.subplot()
	# No Decay
	w1 = np.linspace(-2.5, 2.5, 100)
	w2 = -2 * w1 + 2
	ax1.scatter(
		4/5, 2/5, s=3,
		linewidth=10, marker="x", color="red",
		label="Solution to Gradient Descent without Weight Decay"
	)
	ax1.plot(w1, w2, linewidth=1, label="Solution Space without Weight Decay")
	# With decay
	w1_decay = 4 / (LAMBDA + 5)
	w2_decay = 2 / (LAMBDA + 5)
	ax1.scatter(
		w1_decay, w2_decay,
		linewidth=10, marker="x", color="green",
		label="Solution to Gradient Descent with Weight Decay"
	)
	# Plot contour
	delta = 0.025
	x = np.arange(-2., 2., delta)
	y = np.arange(-2., 2., delta)
	X, Y = np.meshgrid(x, y)
	Z = LAMBDA / 2 * (X ** 2 + Y ** 2)
	CS = ax1.contour(X, Y, Z, 30)
	# ax1.clabel(CS, inline=1, fontsize=10)
	plt.grid(True)
	plt.legend()
	ax1.set_xlim([-1, 2])
	ax1.set_ylim([-1, 2])
	ax1.set_xlabel("$w_1$")
	ax1.set_ylabel("$w_2$")
	plt.title(f"$\lambda$={LAMBDA}")
	plt.savefig("./plot_q1.png", dpi=300)
	plt.show()
