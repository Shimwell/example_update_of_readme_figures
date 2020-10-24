
# sudo docker build -t auto_openmc_benchmark .
# sudo docker run -v $PWD:/share auto_openmc_benchmark python3 run_all_simulations.py

FROM ubuntu:18.04

RUN apt-get --yes update && apt-get --yes upgrade

# Install wget
RUN apt-get --yes install wget
RUN apt-get --yes install python3
RUN apt-get --yes install python3-pip
RUN pip3 install matplotlib
RUN pip3 install pytz

# Copy over the simulation scripts code
COPY run_all_simulations.py run_all_simulations.py


CMD ["/bin/bash"]
