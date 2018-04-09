################## BASE IMAGE ######################

FROM ei11051/base:latest

################## METADATA ######################

LABEL base_image="base:latest"
LABEL version="1"
LABEL software="STAR"
LABEL software.version="2.5.4b"
LABEL about.summary="ultrafast universal RNA-seq aligner"
LABEL about.home="https://github.com/alexdobin/STAR/"
LABEL about.tags="Genomics"

################## MAINTAINER ######################

MAINTAINER Nelson Rafael <ei11051@fe.up.pt>

ENV TAR=2.5.4b.tar.gz
ENV URL=https://github.com/alexdobin/STAR/archive/
ENV FOLDER=STAR-2.5.4b
ENV DST=/home/biodocker/bin

RUN wget $URL/$TAR -O $DST/$TAR && \
    tar xzfv $DST/$TAR && \
    rm $DST/$TAR && \
    cd $FOLDER/source && \
    make
    #mv $FOLDER $DST
    
WORKDIR /data/

CMD ["STAR"]
