# MicrobeTaxaSARS2

### What is the problem?


### Why should we solve it?


### What is MicrobeTaxaSARS2?


### Workflow for MicrobeTaxaSARS2
Here is the workflow for the pipeline:
![Pipleline Workflow for Metagenomic Analysis of CoVID patients' microbiome](img/workflow.png)

### How to use MicrobeTaxaSARS2
Installation options:
We will provide a docker image for installing and using SARS2MicrobeTaxa.

The Docker image will contains SARS2MicrobeTaxa and it will be downloadable from the Docker Hub.

docker pull <!-- omicscodeathon/microbetaxasars2 -->: Command to pull the image from the DockerHub
docker run <!-- omicscodeathon/microbetaxasars2 -->: Run the docker image from the command line


### Methods

In this project, we analysed Whole Genome Sequences (WGS) from 5 CoVID-19 patients and the dataset used was obtained from the Sequence Read Achive (SRA). These were fecal samples from CoVID-19 patients. We used 5 control datasets to compare with the cases. For the 16S data analysis, we also analysed 16S rRNA sequences from saliva samples.

Here are the necessary steps in order to do this analysis:
- [x] Do quality control for the entire dataset and see if the data quality is good.
- [x] Do the assembly and then generate a contig .fasta file which is submitted to the [MG-RAST server](https://www.mg-rast.org) in order to compare the function results with the taxa results from the annotation using prodigal:

Here is the command line to use for annotation with prodigal (where the Accession ID is SRR12328886):
```
prodigal -a assembled/SRR12328886/contigs.aa.fasta -d assembled/SRR12328886/contigs.nuc.fasta -i assembled/SRR12328886/contigs.fasta -f gff -p meta > assembled/SRR12328886/contigs.gff
```

- [ ] Annotation using PRODIGAL (This generates a .tsv file containing the taxonomy and bacteria frequency in each sample).
- [ ] Generate plots and annotation using PROKKA or BLAST.

### Results
Results of the analysis are in the [output folder](output/).

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
