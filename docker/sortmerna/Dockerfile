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

ENV ORG_HOME=/home/biodocker
ENV SMR_HOME=/home/biodocker/sortmerna

RUN cd $ORG_HOME && \
    git clone https://github.com/biocore/sortmerna.git && \
    cd sortmerna && \
    mkdir -p $SMR_HOME/build/Release && \
    cd build/Release && \
    cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release ../.. && \
    export PATH="$SMR_HOME/build/Release/src/indexdb:$SMR_HOME/build/Release/src/sortmerna:$PATH"

WORKDIR /data/
