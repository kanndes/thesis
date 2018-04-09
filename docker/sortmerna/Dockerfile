################## BASE IMAGE ######################

FROM ei11051/base:latest

################## METADATA ######################

LABEL base_image="base:latest"
LABEL version="1"
LABEL software="MEGAN"
LABEL software.version="6.11.1"
LABEL about.summary="microbiome data analyzer"
LABEL about.home="http://ab.inf.uni-tuebingen.de/software/megan6/"
LABEL about.tags="Taxonomy"

################## MAINTAINER ######################

MAINTAINER Nelson Rafael <ei11051@fe.up.pt>

ENV URL=http://ab.inf.uni-tuebingen.de/data/software/megan6/download/MEGAN_Community_unix_6_11_1.sh

RUN wget $URL && \
    chmod +x MEGAN_Community_unix_6_11_1.sh && \
    ./MEGAN_Community_unix_6_11_1.sh

#ENV PATH ${PATH}:${DST}/STAR-2.5.4b/bin/Linux_x86_64

WORKDIR /data/

#CMD ["STAR"]
