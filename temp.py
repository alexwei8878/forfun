# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#just plot a lineplot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set_style("whitegrid")


a = np.array([3,4])
a = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

plt.plot(a[0], a[2])