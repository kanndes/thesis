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

RUN apt-get update && apt-get install -y rna-star && apt-get clean && apt-get purge && rm -rf /var/lib/apt/lists/* /tmp/*

WORKDIR /data/

CMD ["STAR"]
