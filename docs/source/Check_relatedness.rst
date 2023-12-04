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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This dimension reduction step is commonly applied prior to both IBD analysis and PCA. 

