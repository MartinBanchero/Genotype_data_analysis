5. Check relatedness (Sample-level)
========================================================================

Population-based cohort studies are often limited to unrelated individuals, and the generalized linear modeling approach
(used in GWAS) assumes independence across individuals. Importantly, in regional cohort studies (e.g., hospital-based cohort studies) of complex
diseases, individuals from the same family can be recruited unintentionally. A common measure
of relatedness (or duplication) between pairs of samples is based on identity by descent (IBD). An
IBD kinship coefficient of greater than 0.1875 may suggest relatedness, duplicates, or sample mixture.
Typically, the individual of a related pair with lower genotype call rate is removed.

LD pruning
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
First we need to perform linkage disequilibrium (LD) pruning with a threshold value of 0.7 (this could vary, some studies use 0.2) - remove SNPs with high LD with each other (removes one from each pair). 
This eliminates a large degree of redundancy in the data. This dimension reduction step is commonly applied prior to both IBD analysis and PCA.

.. code-block:: r
    
    runPLINK("--ped file.ped --map file.map --indep-pairwise 50 5 0.7 --out file")
    # keep only selected snps for your data
    runPLINK("--ped file.ped --map file.map --exclude file.prune.out --recode --out prunedSet")

Calculate IBD - identity by descent (the degree of recent shared ancestry)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: r

    runPLINK('--ped prunedSet.ped --map prunedSet.map --Z-genome --out Pruned_IBD')
    #change format 
    system("zcat Pruned_IBD.genome.gz | tr -s ' ' '\t' > Pruned_IBD.tabs")

.. code-block:: r

    # Let’s check samples with IBD > 0.1875 (PI_HAT column in the plink output)
    IBD_high_relat <- IBD %>%
        filter(PI_HAT> 0.1875)
    print(IBD_high_relat)

.. note:: 
    **Advice** Check the table and exclude one from the pair with the lower call rate (code not provided)


