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

Plot sample call rate vs heterozygosity   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
	**Advised**: exclude samples with more than 3 standard deviations away from mean heterozygosity.Lifelines uses 4sd from the mean heterozygosity. 
   
4. Check sex discordance (Sample-level)
========================================================================
Sample mix-up is investigated by looking at sex mismatch, where sex
information of each sample is compared with genotypes at chromosomes X and Y.

.. note:: 
	**NB:** This method however does not detect same sex sample mix-ups and is not reliable when there are sex chromosome abnormalities.
	??For this step we need to use files with already excluded low call rate SNPs 

5. Check relatedness (Sample-level)
========================================================================

Population-based cohort studies are often limited to unrelated individuals, and the generalized linear modeling approach
(used in GWAS) assumes independence across individuals. Importantly, in regional cohort studies (e.g., hospital-based cohort studies) of complex
diseases, individuals from the same family can be recruited unintentionally. A common measure
of relatedness (or duplication) between pairs of samples is based on identity by descent (IBD). An
IBD kinship coefficient of greater than 0.1875 may suggest relatedness, duplicates, or sample mixture.
Typically, the individual of a related pair with lower genotype call rate is removed.

LD pruning
------------------------------------------------------------------------------
First we need to perform linkage disequilibrium (LD) pruning with a threshold value of 0.7 (this could vary, some studies use 0.2) - remove SNPs with high LD with each other (removes one from each pair). 
This eliminates a large degree of redundancy in the data. 

Calculate IBD - identity by descent (the degree of recent shared ancestry)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This dimension reduction step is commonly applied prior to both IBD analysis and PCA. 
   

6. Hardy--Weinberg equilibrium (SNP level)
========================================================================




.. note::
	Check ped file : does it have phenotypes? If ped doesn't have phenotypes reformat ped to add phenotypes (code not provided).
	

.. note::
	 Threshold for HWE test statistic can vary. Consider p-value  \< 10e-5 or  \< 10e-6 in controls











   

