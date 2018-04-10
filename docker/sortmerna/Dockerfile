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

#ENV DST=/home/biodocker/bin

RUN git clone https://github.com/biocore/sortmerna.git && \
    cd sortmerna && \
    pwd && \
    ./configure && make && make install
    
#    mkdir -p $SMR_HOME/build/Release
#pushd $SMR_HOME/build/Release
#cmake -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release ../..

WORKDIR /data/
