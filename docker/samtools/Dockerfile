################## BASE IMAGE ######################

FROM ei11051/base:latest

################## METADATA ######################
LABEL base_image="base:latest"
LABEL version="2"
LABEL software="Samtools"
LABEL software.version="1.3.1"
LABEL about.summary="Tools for manipulating next-generation sequencing data"
LABEL about.home="https://github.com/samtools/samtools"
LABEL about.documentation="https://github.com/samtools/samtools"
LABEL about.license_file="https://github.com/samtools/samtools"
LABEL about.license_file="https://github.com/samtools/samtools/blob/develop/LICENSE"
LABEL about.license="SPDX:MIT"
LABEL about.tags="Genomics"
LABEL extra.identifiers.biotools="SAM"

################## MAINTAINER ######################
MAINTAINER Nelson Rafael <ei11051@fe.up.pt>

RUN conda install samtools=1.3.1

WORKDIR /data/

CMD ["samtools"]
