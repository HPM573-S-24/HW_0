import numpy as np
import matplotlib.pyplot as plt
import platform

# enter your name below
YOUR_NAME = 'John Smith'

#######
# sample from a standard normal distribution
sample = np.random.normal(loc=0, scale=1, size=1000)

# draw histogram
plt.hist(sample, bins='auto')
plt.title(YOUR_NAME+'\nPython version: '+platform.python_version())
plt.savefig(YOUR_NAME+'.png')
