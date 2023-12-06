3. Check sample heterozygosity (Sample-level)
==========================================================================

Heterozygosity refers to the presence of each of the two alleles
at a given SNP within an individual.  
Outliers showing excess or depletion in heterozygotes
genotypes may be due to contamination or issues during genotyping process.

.. note::
	Consider doing it already only with high call rate SNPs?

.. code-block:: r

	runPLINK("--ped file.ped --map file.map --het --out file")
	system("cat file.het | tr -s ' ' '\t' > file_het.tabs")
	het_level <- read.delim ("file_het.tabs") %>%
	  select (-X)

Plot sample call rate vs heterozygosity   
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: r

	sample_missing_rate_het <- call_rate_samples_after_filter %>%
  		left_join(het_level, by = c("IID" = "IID")) %>%
  		rename(heter_rate = "F")
	std = sd(sample_missing_rate_het$heter_rate) ## calculate standard deviation
	std_list = c(std, -std, 2*std, -2*std, 3*std, -3*std)

	ggplot(sample_missing_rate_het, aes(x= F_MISS, y= heter_rate)) +
		geom_point() +
		geom_vline(xintercept = 0.1, linetype="dashed", color = "blue") +
		geom_hline(yintercept = std_list[1:4], col = "grey", linetype = "dashed") +
		geom_hline(yintercept = std_list[5:6], col = "red", linetype = "dashed") + 
		ggtitle("Heterozygosity vs Missingness across samples") + 
		theme_bw() +
		xlab("Proportion of missing SNPs") +
		ylab("Heterozygosity rate(+- 3 sd)")
		
.. note::
	**Advice** 	Exclude samples with more than 3 standard deviations away from mean heterozygosity.
				Lifelines uses 4sd from the mean heterozygosity. 

