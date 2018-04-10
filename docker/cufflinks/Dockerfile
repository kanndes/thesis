################## BASE IMAGE ######################

FROM ei11051/base:latest

################## METADATA ######################

LABEL base_image="base:latest"
LABEL version="1"
LABEL software="cufflinks"
LABEL software.version="2.2.1"
LABEL about.summary="assembles transcripts, estimates their abundances, and tests for differential expression and regulation in RNA-Seq samples"
LABEL about.home="http://cole-trapnell-lab.github.io/cufflinks/"
LABEL about.tags="Genomics"

################## MAINTAINER ######################

MAINTAINER Nelson Rafael <ei11051@fe.up.pt>

ENV HOME /home/biodocker/bin

RUN cd $HOME && \
    wget http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz && tar -xzvf cufflinks-2.2.1.Linux_x86_64.tar.gz
    
    
ENV PATH ${PATH}:${HOME}/bin/cufflinks-2.2.1.Linux_x86_64/

RUN wget http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/test_data.sam && \
    cufflinks ./test_data.sam

WORKDIR /data/

CMD ["cufflinks"]
