
"""this python scrip just plots a random graph and write the readme with the date"""

import numpy as np
import matplotlib.pyplot as plt

N = 5
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x, y, s=20)
plt.savefig('/share/new_figure.jpg')

with open('/share/README.md', 'w') as readme:
    readme.write('# example_update_of_readme_figures\n')
    readme.write('\n')
    readme.write('This repository is a minimal working example of an automated benchmarking')
    readme.write('workflow using Github actions.\n')
    readme.write('\n')
    readme.write('![latest results](https://github.com/Shimwell/example_update_of_readme_figures/blob/main/new_figure.jpg)')



#os.system('cp new_figure.jpg /share/new_figure.jpg')