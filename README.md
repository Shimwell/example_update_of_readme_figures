# Example Update of Readme Figures

This repository is a minimal working example of an automated
updating of the readme text and figures using Github actions.
with every push to main the Github Actions will build a
containerised Docker enviroment. Within this enviroment all
the dependencies are included (Python Matplotlib etc).
A small Python script is then run within the Docker container
the generates a new random dataset and pushes it to the repository
via the use of a shared swap space and Github tokens for authentication.
The combined result is that each time the Action is triggered
the graph and time stamp on the main readme page is updated.


simulation date 10/24/20 day month year
simulation time 11:32:09 hour minute second (UK time)
![latest results](https://github.com/Shimwell/example_update_of_readme_figures/blob/main/new_figure.jpg)