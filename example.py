from scipy.stats import norm
import matplotlib.pyplot as plt

from peak_detection import *


if __name__ == '__main__':

    size = 200
    xa = np.arange(0, size, 1, dtype=np.int64)
    print(xa)

    noise = np.random.normal(0, 1, size)
    baseline = xa * 0.1
    rv1 = norm(loc=100, scale=5)
    rv2 = norm(loc=50, scale=3)
    rv3 = norm(loc=150, scale=10)
    rv4 = norm(loc=180, scale=0.1)
    rv5 = norm(loc=30, scale=1)
    x = (rv1.pdf(xa) + rv2.pdf(xa) + rv3.pdf(xa) + rv4.pdf(xa) / 10 + rv5.pdf(xa)) * 500 + noise + baseline

    print(type(x), type(x[0]))

    peak_ind, sig = peaks_detection(x, np.arange(1, 70), 3)

    plt.figure(figsize=(9, 3))
    plt.plot(xa, x, linewidth=1, color='k')
    plt.plot(xa[peak_ind], x[peak_ind], 'bv', markersize=10)
    plt.ylabel("Intensity")

    plt.show()