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

