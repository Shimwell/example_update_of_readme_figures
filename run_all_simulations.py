
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
    readme.write('# Example Update of Readme Figures\n')
    readme.write('\n')
    readme.write('This repository is a minimal working example of an automated\n')
    readme.write('updating of the readme text and figures using Github actions.\n')
    readme.write('with every push to main the Github Actions will build a\n')
    readme.write('containerised Docker enviroment. Within this enviroment all\n')
    readme.write('the dependencies are included (Python Matplotlib etc).\n')
    readme.write('A small Python script is then run within the Docker container\n')
    readme.write('the generates a new random dataset and pushes it to the repository\n')
    readme.write('via the use of a shared swap space and Github tokens for authentication.\n')
    readme.write('The combined result is that each time the Action is triggered\n')
    readme.write('the graph and time stamp on the main readme page is updated.\n')
    readme.write('\n')

    readme.write('\n')
    readme.write('simulation date ' + date + '\n')
    readme.write('simulation time ' + time + '\n')
    readme.write('![latest results](https://github.com/Shimwell/example_update_of_readme_figures/blob/main/new_figure.jpg)')
