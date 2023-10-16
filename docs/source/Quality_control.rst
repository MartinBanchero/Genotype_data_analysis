Quality control
#################################################

**SNP array quality control protocol** 
*************************************************

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

Let's prepare the environment by uploading the libraries and creating the function to run PLINK from the directory where the exe file is:

.. note::

   You might need to change this function depending on the way you plan to run plink


1. Check call rate per SNP and per sample (both SNP and Sample-level)
=========================================================================

The call rate for a given SNP is defined as the proportion of individuals
in the study for which the corresponding SNP information is not missing

The call rate for a given sample is defined as the proportion of SNPs
that is missing for the sample.

Calculate call rate per sample (imiss) and per SNP (lmiss)
------------------------------------------------------------------------


Plot histograms of call rate per sample
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Plot histograms of call rate per snp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2. Check MAF (SNP-level)
========================================================================
Minor allele frequency (MAF). A large degree of homogeneity at a given SNP
across study participants generally results in inadequate power to infer a statistically significant
relationship between the SNP and the trait under study. This can occur when we have a very small
MAF so that the large majority of individuals have two copies of the major allele.

.. note::

   Threshold for MAF can vary between 1% and 5% (for small sample settings)

Plot MAF histogram
---------------------------------------------------------------------------

.. note::
	**Advice** For small sample size it is recommended to exclude SNPs with MAF \< 0.05.
	
3. Check sample heterozygosity (Sample-level)
==========================================================================

Heterozygosity refers to the presence of each of the two alleles
at a given SNP within an individual.  
Outliers showing excess or depletion in heterozygotes
genotypes may be due to contamination or issues during genotyping process.

?? should we do it already only with high call rate SNPs? 

   
   
   
   
   
   

