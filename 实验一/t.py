import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)
plt.plot(n, np.log(n), label='In(n)')
plt.plot(n, n**(1/3), label='n^(1/3)')
plt.legend()
plt.show()
