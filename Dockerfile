
FROM ubuntu:18.04

# Install wget
RUN apt-get --yes install wget

RUN wget -q -O new_figure.jpg https://unsplash.it/200/300/?random

RUN cp new_figure.jpg /github/workspace/new_figure.jpg

# Copy over the simulation scripts code
COPY benchmarks benchmarks/


CMD ["/bin/bash"]
