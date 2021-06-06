# MicrobeTaxaSARS2

### What is the problem?
Since the World Health Organization labeled coronavirus disease 19 a pandemic, there has been a significant public involvement from scientists and scientific groups to speed research and development. Today, we are lucky to have various tools and publically available data to support several studies and discoveries; yet, limited data on the gut microbiota of CoVID-19 patients have not been well documented. The type and abundance of bacteria in the gut may influence the severity of CoVID-19 infection as well as the magnitude of the immune system's reaction to the infection.

### Why should we solve it?
While metagenomics has evolved as a preferred tool for examining bacterial populations, assembling metagenomic data remains difficult, impeding biological discoveries. Furthermore, increasing the number of proper gene identifications and translation start locations for each gene, as well as lowering the overall number of false positives, are all desired outcomes. To address this challenges the MicrobeTaxaSARS2, will enable for the quick use of assembly and annotation tools, Metaspades and Prodigal (PROkaryotic DYnamic programming Gene-finding ALgorithm), respectively. 

### What is MicrobeTaxaSARS2?
MicrobeTaxaSARS2 is an automated analytic pipeline developed using python and R at the ASBCB Omics Codeathon in June 2021, allowing us to determine the taxonomic diversity and the functional aspects of the gut microbiome of CoVID-19 patients.

### Workflow for MicrobeTaxaSARS2
Here is the workflow for the pipeline:

![Pipleline Workflow for Metagenomic Analysis of CoVID patients' microbiome](img/workflow.png)

### How to use MicrobeTaxaSARS2
Installation options:
We will provide a docker image for installing and using SARS2MicrobeTaxa.

The Docker image will contain SARS2MicrobeTaxa and it will be downloadable from the Docker Hub.
We will be able to run this tool as a Docker or Singularity container.

- docker pull <!-- omicscodeathon/microbetaxasars2 -->: Command to pull the image from the DockerHub

- docker run <!-- omicscodeathon/microbetaxasars2 -->: Run the docker image from the command line


### Methods

In this project, we analysed Whole Genome Sequences (WGS) from 6 CoVID-19 patients and the dataset used was obtained from the Sequence Read Achive (SRA). These were fecal samples from CoVID-19 patients. For the 16S data analysis, we also analysed 16S rRNA sequences from saliva samples.

The MicrobeTaxaSARS2 pipeline implements the following steps:
- [x] After downloading the data in fastq format, we use FastQC to do quality checks, to see if the data quality is good.
- [x] We run the files for assembly using metaspades, which allows just a single short-read library that must be paired-end, although lengthy reads can be provided but optimal performance is not guaranteed. The output file will be a fasta file.
- [x] Next the annotation is done using prodigal, a fast and efficient protein-coding gene prediction tool for prokaryotic genomes. Yields a tsv file.
Here is the command line to use for annotation with prodigal (where the Accession ID is SRR12328886):
```
prodigal -a assembled/SRR12328886/contigs.aa.fasta -d assembled/SRR12328886/contigs.nuc.fasta -i assembled/SRR12328886/contigs.fasta -f gff -p meta > assembled/SRR12328886/contigs.gff
```
- [x] Following that, we run MetaPhlAn to assign taxonomies. Metagenomic Phylogenetic Analysis (MetaPhlAn) is a computational technique for analyzing the composition of metagenomic shotgun sequencing data.

![Copie de Organizational Charts by Slidesgo (1)](https://user-images.githubusercontent.com/85350037/120919592-ae92b900-c6ba-11eb-81ce-9aba41acd7e8.jpg)


- [ ] Generate plots and annotation using PROKKA or BLAST.

### Results
Results of the analysis are in the [output folder](output/).

We also got a result graph of the phylum level taxonomic characterization, but the genus-level characterization gives a graph that is complicated as a result of the huge number of taxa in the datasets. We're trying to find a solution to getting a better graph in order to interpret it.

The species diversity and indices graph still need interpretation.

### Team
- Sophia Sei (sofiasehli00@gmail.com)
- Casey Eddington (eddin022@umn.edu)
- Zainab El Ouafi (zainab.elouafi@gmail.com)
- Soumaya JBARA (soumaya.jbara@um5r.ac.ma)
- Kasambula Arthur Shem (arthurshem86@gmail.com)
- Islam El Jaddaoui (is.eljaddaoui@gmail.com)
- Ayorinde Afolayan (afolayanayorinde@gmail.com)
- Olaitan I. Awe (laitanawe@gmail.com)

### References
