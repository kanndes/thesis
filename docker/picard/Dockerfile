################## BASE IMAGE ######################

FROM ei11051/base:latest

################## METADATA ######################

LABEL base_image="base:latest"
LABEL version="2"
LABEL software="Picard"
LABEL software.version="2.3.0"
LABEL about.summary="A set of Java command line tools for manipulating high-throughput sequencing (HTS) data and formats."
LABEL about.home="https://github.com/broadinstitute/picard/"
LABEL about.documentation="https://github.com/broadinstitute/picard/"
LABEL about.license_file="https://github.com/broadinstitute/picard/blob/master/LICENSE.txt"
LABEL about.license="SPDX:MIT"
LABEL extra.identifiers.biotools="picard_tools"
LABEL about.tags="Genomics"

################## MAINTAINER ######################
MAINTAINER Nelson Rafael <ei11051@fe.up.pt>

RUN conda install picard=2.3.0

WORKDIR /data/

CMD ["picard"]
