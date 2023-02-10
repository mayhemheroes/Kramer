# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

ADD . /src
WORKDIR /src
WORKDIR /src/mayhem
RUN python3 -m pip install pystyle==0.6
ENV MAYHEM_FUZZ=1
CMD ["/src/mayhem/fuzz_kramer.py"]
