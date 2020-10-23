
FROM ubuntu:18.04

RUN apt-get --yes update && apt-get --yes upgrade

# Install wget
RUN apt-get --yes install wget
RUN apt-get --yes install python3

RUN wget -q -O new_figure.jpg https://unsplash.it/200/300/?random


RUN ls

# Copy over the simulation scripts code
COPY run_all_simulations.py run_all_simulations.py


CMD ["/bin/bash"]
