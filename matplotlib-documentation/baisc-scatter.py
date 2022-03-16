import numpy as np
import matplotlib.pyplot as plt

# general grafic configuration
plt.style.use('ggplot')


# setting the random data 

x = np.random.normal(0,1.5,150)
y = np.random.normal(0,1.5,len(x))

sizes = np.random.uniform(20, 50, len(x))
colors = np.random.uniform(500, 1009, len(x)) 

# plotting
fig, ax = plt.subplots()
ax.scatter(x , y , s = sizes , c = colors)

ax.set(xlim=(-6, 6), xticks=np.arange(-6, 6),
      ylim=(-6, 6), yticks=np.arange(-6, 6))