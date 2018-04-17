#!/bin/bash
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/assembly_summary.txt
awk -F '\t' '{if($12=="Complete Genome") print $20}' assembly_summary.txt > assembly_summary_complete_genomes.txt
mkdir GbBac
for next in $(cat assembly_summary_complete_genomes.txt); do wget -P GbBac "$next"/*genomic.fna.gz; done
gunzip GbBac/*.gz
cat GbBac/*.fna > all_complete_Gb_bac.fasta
