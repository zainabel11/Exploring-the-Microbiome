# MicrobeTaxaSARS2

### What is the problem?
Since the World Health Organization labeled coronavirus disease 19 a pandemic, there has been a significant public involvement from scientists and scientific groups to speed research and development. Today, we are lucky to have various tools and publically available data to support several studies and discoveries; yet, limited data on the gut microbiota of CoVID-19 patients have not been well documented. The type and abundance of bacteria in the gut may influence the severity of CoVID-19 infection as well as the magnitude of the immune system's reaction to the infection. We introduce the MicrobeTaxaSARS2 pipeline and TAXAPRO, which was created to reduce time and effort while eliminating manual mistakes, especially when dealing with large amounts of data.

### Why should we solve it?
While metagenomics has evolved as a preferred tool for examining bacterial populations, assembling metagenomic data remains difficult, impeding biological discoveries. Furthermore, increasing the number of proper gene identifications and translation start locations for each gene, as well as lowering the overall number of false positives, are all desired outcomes. To address this challenges the MicrobeTaxaSARS2, will enable for the quick use of assembly and annotation tools, Metaspades and Prodigal (PROkaryotic DYnamic programming Gene-finding ALgorithm), respectively. On the other hand, TAXAPRO is a microbiological profiling script code that delivers accurate strain-level profiling. Taxonomic classifications that are unambiguous; accurate calculation of organismal relative abundance; species-level resolution; and strain identification and tracking.


### What is MicrobeTaxaSARS2 and TAXAPRO?
MicrobeTaxaSARS2 is an automated analytic pipeline developed using python at the ASBCB Omics Codeathon in June 2021. TAXAPRO is a microbiological profiling script code that delivers accurate strain-level profiling. Taxonomic classifications that are unambiguous; accurate calculation of organismal relative abundance; species-level resolution; and strain identification and tracking. Both scipts are allowing us to determine the taxonomic diversity and the functional aspects of the gut microbiome of CoVID-19 patients.

### Overall Workflow
Here is the workflow for the pipeline:
![image](https://user-images.githubusercontent.com/85350037/121264719-e61a8480-c8b7-11eb-8846-4e0062df924c.png)

### How to use MicrobeTaxaSARS2
The most important point in the usage of MicrobeTaxaSARS2 and TAXAPRO is that the two scripts must be in the same location as all the **paired-end** Fastqs (*the reads must be paired-end sequences*) that you're looking to analyse.
Then you can cd into the Fastq directory and then use python to run the scripts from there:

```
cd <location_of_fastqs>
python meta-assembly-annotationPRODIGAL.py && python taxonomy_code.py
```

Installation options:
We will provide a docker image for installing and using SARS2MicrobeTaxa.

The Docker image will contain SARS2MicrobeTaxa and it will be downloadable from the Docker Hub.
We will be able to run this tool as a Docker or Singularity container.

- docker pull <!-- omicscodeathon/microbetaxasars2 -->: Command to pull the image from the DockerHub

- docker run <!-- omicscodeathon/microbetaxasars2 -->: Run the docker image from the command line


### Methods

In this project, we analysed Whole Genome Sequences (WGS) from 6 CoVID-19 patients and the dataset used was obtained from the Sequence Read Achive (SRA). These were fecal samples from CoVID-19 patients.
The MicrobeTaxaSARS2 and TAXAPRO pipeline implements the following steps:
- [x] After downloading the data in fastq format, we used FastQC to do quality checks to see if the data quality is good.
- [x] We ran MicrobeTaxaSARS2 where the assembly was done first, using metaspades.The output file will be a fasta file.
- [x] Next, the annotation was done using prodigal. This yields a GFF file.
- [x] Following that, we ran TAXAPRO to assign taxonomies. delivering a TSV file as an outcome.

Here is the command line to use for annotation with prodigal (where the Accession ID is SRR12328886):
```
prodigal -a assembled/SRR12328886/contigs.aa.fasta -d assembled/SRR12328886/contigs.nuc.fasta -i assembled/SRR12328886/contigs.fasta -f gff -p meta > assembled/SRR12328886/contigs.gff
```

![Copie de Organizational Charts by Slidesgo (2)](https://user-images.githubusercontent.com/85350037/121264936-43163a80-c8b8-11eb-9b9d-bfb3e92f4748.jpg)



### Results
Results of the analysis are in the [output folder](output/).

There were no significant variations in the composition of the gut microbiome of the 6 cocid-19 samples of infected patients. According to our findings and the use of the MicrobeTaxaSARS2 and TAXAPRO pipelines, Clostridia and Bacteroidia genuses were discovered in larger quantities in the fecal bacterial samples. The microbiota profiles of the six samples were rather similar. We found a rise in the relative abundance of Bacteroides fragilis, Desulfotomaculum acetoxidans, Pelotomaculum thermopropionicum, Escherichia coli, and other opportunistic bacterial strains at the strain level.
These findings add to our understanding of the alteration of the gut microbiome in covid-19 infected individuals, paving the way for a better understanding of the microbiota's effects on people's health.


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
