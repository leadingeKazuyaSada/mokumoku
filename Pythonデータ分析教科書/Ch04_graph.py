#%%
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)
mu = 100
sigma = 15
x = np.random.normal(mu, sigma, 1000)

fig, ax = plt.subplots()

n, bins, patches = ax.hist(x)

plt.show()


# %%
