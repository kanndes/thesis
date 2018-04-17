#!/bin/bash
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/protozoa/assembly_summary.txt
awk -F '\t' '{if($12=="Complete Genome") print $20}' assembly_summary.txt > assembly_summary_complete_genomes.txt
mkdir GbPro
for next in $(cat assembly_summary_complete_genomes.txt); do wget -P GbPro "$next"/*genomic.fna.gz; done
gunzip GbPro/*.gz
cat GbPro/*.fna > all_complete_Gb_pro.fasta
