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

ENV TAR=2.5.4b.tar.gz
ENV URL=https://github.com/alexdobin/STAR/archive/
ENV FOLDER=STAR-2.5.4b
ENV DST=/home/biodocker/bin

RUN git clone https://github.com/biocore/sortmerna.git && \
    cd sortmerna && \
    bash ./build.sh

WORKDIR /data/
