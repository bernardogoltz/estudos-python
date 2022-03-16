import numpy as np 
import matplotlib.pyplot as plt


# Using style sheets
plt.style.use('ggplot')

'''
'Solarize_Light2', '_classic_test_patch', #'_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale','seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10'
'''

x = np.linspace(0,10,100)
  # linspace: linear space => 
  # start , stop , tamanho do array
  
y = 0.5*np.sin(2 * x)

# plotando a figura
figure , ax = plt.subplots()
ax.plot(x , y , linewidth = 4)

ax.set(xlim = (0,4))
ax.set(ylim = (-0.6,0.6))

# show
plt.show()
