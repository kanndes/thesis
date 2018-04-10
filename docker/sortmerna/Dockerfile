################## BASE IMAGE ######################

FROM ei11051/base:latest

################## METADATA ######################

LABEL base_image="base:latest"
LABEL version="1"
LABEL software="sortmerna"
LABEL software.version="1"
LABEL about.summary="local sequence alignment tool for filtering, mapping and clustering"
LABEL about.home="https://github.com/biocore/sortmerna"
LABEL about.tags="Genomics"

################## MAINTAINER ######################

MAINTAINER Nelson Rafael <ei11051@fe.up.pt>

RUN git clone https://github.com/biocore/sortmerna.git && \
    cd sortmerna && \
    ./configure && make && make install

WORKDIR /data/
