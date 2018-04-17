#!/bin/bash
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/viral/assembly_summary.txt
awk -F '\t' '{if($12=="Complete Genome") print $20}' assembly_summary.txt > assembly_summary_complete_genomes.txt
mkdir GbVir
for next in $(cat assembly_summary_complete_genomes.txt); do wget -P GbVir "$next"/*genomic.fna.gz; done
gunzip GbVir/*.gz
cat GbVir/*.fna > all_complete_Gb_vir.fasta
