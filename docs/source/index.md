# SNP/GWAS workflow documentation!

## SNP array quality control protocol

This file describes step to perform quality control for the SNP array data.
You will need genotype data in plink format (either .ped and .map or .bed file)

The .ped file contains information on each study participant including family ID,
participant ID, father ID, mother ID, sex, phenotype, and the full typed genotype. Here, each SNP
is bi-allelic (i.e., only two nucleotides are observed at any given SNP across study participants) and
coded as a pair of nucleotides (A, C, T, or G). Notably, the ordering in the pair is non-informative
in the sense that the first alleles listed for each of the two SNPs are not necessarily on the same
chromosome. The .map file contains a row for each SNP corresponding 
chromosome (chr) and coordinate (BPPos) based on the current genome build.

Most of the steps for the QC will be performed in plink1.9, so it has to be installed.  

Let's prepare the environment by uploading the libraries


```{toctree}
:hidden:
:caption: Introduction
:maxdepth: 1

setup

```

```{toctree}
:hidden:
:caption: From raw data to plink
:maxdepth: 1

genomestudio

```

```{toctree}
:hidden:
:caption: Quality control
:maxdepth: 1

qualitycontrol

```
```{toctree}
:hidden:
:caption: GWAS
:maxdepth: 1

gwide

```

