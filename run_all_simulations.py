
"""this python scrip just plots a random graph and write the readme with the date"""

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
tz_London = pytz.timezone('Europe/London')

# plots graph with 5 random data points
x = np.random.rand(5)
y = np.random.rand(5)
plt.scatter(x, y, s=30)
plt.savefig('/share/new_figure.jpg')

# gets th time stamp information
tz_London = pytz.timezone('Europe/London') 
datetime_London = datetime.now(tz_London)    
date = datetime_London.strftime("%D day month year")
time = datetime_London.strftime("%H:%M:%S hour minute second (UK time)")

with open('/share/README.md', 'w') as readme:
    readme.write('# example_update_of_readme_figures\n')
    readme.write('\n')
    readme.write('This repository is a minimal working example of an automated benchmarking')
    readme.write('workflow using Github actions.\n')
    readme.write('\n')
    readme.write('simulation date ' + date)
    readme.write('simulation time ' + time)
    readme.write('![latest results](https://github.com/Shimwell/example_update_of_readme_figures/blob/main/new_figure.jpg)')


#os.system('cp new_figure.jpg /share/new_figure.jpg')