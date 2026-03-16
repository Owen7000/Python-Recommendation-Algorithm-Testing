print("Running graph generator. Please wait")

import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('output.csv', delimiter=',', names=True)

header_names = data.dtype.names

x_axis = data[header_names[0]]

for name in header_names[1:]:
    plt.plot(x_axis, data[name], label=name)

plt.ylabel("Weighted Category Scores")
plt.xlabel("Training Run")
plt.legend(loc='best')
plt.title("Starting weights = 1")
plt.show()