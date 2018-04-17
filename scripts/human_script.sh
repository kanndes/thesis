#!/bin/bash
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/vertebrate_mammalian/Homo_sapiens/assembly_summary.txt
mkdir GbHum
for next in $(cat assembly_summary.txt); do wget -P GbHum "$next"/*genomic.fna.gz; done
gunzip GbHum/*.gz
cat GbHum/*.fna > all_complete_Gb_hum.fasta
