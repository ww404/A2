import numpy as np 
import math
import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3, 4]
y1 = [15.35, 15.68, 15.63, 16.93]
y2 = [2.24, 2.2, 2.17, 2.23]
y3 = [1.04, 1.04, 1.10, 1.14]
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.xlabel("loading type")
plt.ylabel("eogenvalues")
plt.show()