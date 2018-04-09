################## BASE IMAGE ######################

FROM ei11051/base:latest

################## METADATA ######################

LABEL base_image="base:latest"
LABEL version="1"
LABEL software="rna-star"
LABEL software.version="2.5.2bdfsg-1-deb"
LABEL about.summary="ultrafast universal RNA-seq aligner"
LABEL about.home="https://github.com/alexdobin/STAR/"
LABEL about.tags="Genomics"

################## MAINTAINER ######################

MAINTAINER Nelson Rafael <ei11051@fe.up.pt>

RUN apt-get install rna-star

WORKDIR /data/

CMD ["rna-star"]
