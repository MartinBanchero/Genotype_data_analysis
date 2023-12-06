
2. Check MAF (SNP-level)
========================================================================
Minor allele frequency (MAF). A large degree of homogeneity at a given SNP
across study participants generally results in inadequate power to infer a statistically significant
relationship between the SNP and the trait under study. This can occur when we have a very small
MAF so that the large majority of individuals have two copies of the major allele.

.. code-block:: r

   runPLINK("--ped file.ped --map file.map --freq --out file_maf")
   system("cat file_maf.frq | tr -s ' ' '\t' > file_maf_frq.tabs")

.. note::

   Threshold for MAF can vary between 1% and 5% (for small sample settings)

Plot MAF histogram
---------------------------------------------------------------------------
.. code-block:: r
   
   MAF_check <- read.delim("file_maf_frq.tabs") %>%
     select(-X)
   maf_01 = sum(MAF_check$MAF<0.01) # threshold at 1%
   maf_05 = sum(MAF_check$MAF<0.05) # threshold at 5%

   ggplot(MAF_check, aes(MAF)) +
      geom_histogram() +
      theme_bw() +
      ylab ("# of occurences") +
      xlab ("Minor allele frequency") +
      geom_vline(xintercept = 0.01, color = 'grey', linetype="dashed") +
      annotate(geom="text", x=-0.02, y=100000, label=paste0("maf = 0.01    ",maf_01, ' SNPs'),
               angle = 90, color="red", size = 3) +
      geom_vline(xintercept = 0.05, color = 'grey', linetype="dashed") +
      annotate(geom="text", x=0.043, y=100000, label=paste0("maf= 0.05    ", maf_05, ' SNPs'),
               angle = 90, color="red", size = 3)

.. note::
	**Advice** For small sample size it is recommended to exclude SNPs with MAF \< 0.05.
