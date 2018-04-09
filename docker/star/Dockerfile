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

ENV STAR_VERSION=2.5.4b

RUN STAR_URL="https://github.com/alexdobin/STAR/archive/${STAR_VERSION}.tar.gz" &&\
    wget -P $SRC $STAR_URL &&\
    tar -xvf $SRC/${STAR_VERSION}.tar.gz -C $SRC && \
mv $SRC/STAR-${STAR_VERSION}/bin/Linux_x86_64_static/STAR /usr/local/bin

WORKDIR /data/

CMD ["STAR"]
