1. Check call rate per SNP and per sample (both SNP and Sample-level)
======================================================================================

The call rate for a given SNP is defined as the proportion of individuals
in the study for which the corresponding SNP information is not missing

The call rate for a given sample is defined as the proportion of SNPs
that is missing for the sample.


.. code-block:: r
	:caption: Call rate per sample (imiss) and per SNP (lmiss)
	
	runPLINK("--ped file.ped --map file.map --missing --out file_call_rate")
	

.. code-block:: r
	:caption: Change format to make it easier for R data frame imiss
	
	system("cat file_call_rate.imiss | tr -s ' ' '\t' > call_rate_sample.tabs")

.. code-block:: r
	:caption: Change format lmiss

	system("cat file_call_rate.lmiss | tr -s ' ' '\t' > call_rate_SNP.tabs")


Plot histograms of call rate per sample
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: r
	:caption: Load call rate SNP and sample.
	
	call_rate_SNP <- read.delim("call_rate_SNP.tabs") %>%
  				select (-X)
	call_rate_samples <- read.delim("call_rate_sample.tabs") %>%
  				select (-X)
.. code-block:: r
	:caption: Calculate n of filtered out samples with missing rate < 0.1

	n_filtered_out <- sum(call_rate_samples$F_MISS > 0.1)

	ggplot(call_rate_samples, aes((1-F_MISS)*100)) +
		geom_histogram(bins = 50) +
		theme_bw() +
		ylab ('Sample number') +
		xlab ('Call Rate(%)') +
		geom_vline(xintercept = 90, color = 'red', linetype="dashed") +
		annotate(geom="text", x=70, y=200, label=paste0("Number of samples to exclude = ", n_filtered_out),
			color="red", size = 4)

Plot histograms of call rate per snp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: r
	:caption: Calculate n of filtered out SNPs with missing rate < 0.1

	n_filtered_out <- sum(call_rate_SNP$F_MISS >=0.1)

	ggplot(call_rate_SNP, aes((1-F_MISS)*100)) +
		geom_histogram(bins = 50) +
		theme_bw() +
		ylab ('SNP number') +
		xlab ('Call Rate(%)') +
		geom_vline(xintercept = 90, color = 'red', linetype="dashed") +
		annotate(geom = "text", x = 70, y = 100000, label = paste0("Number of SNPs to exclude = ", n_filtered_out),
					color="red", size = 4)

Exclude SNPs with call rate < 90% and check again sample call rate
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: r

	runPLINK("--ped file.ped --map file.map --geno 0.1 --recode --out file_filtered_snps")

.. code-block:: r
	:caption: Check again sample call rate

	runPLINK("--ped file_filtered_snps.ped --map file_filtered_snps.map --missing --out file_call_rate_filtered_snps")
	system("cat file_call_rate_filtered_snps.imiss | tr -s ' ' '\t' > file_call_rate_filtered_snps_imiss.tabs")
	call_rate_samples_after_filter <- read.delim("file_call_rate_filtered_snps_imiss.tabs") %>%
		select (-X)

.. code-block:: r
	:caption: Plot histograms of call rate per sample after filtered SNPs

	n_filtered_out <- sum(call_rate_samples_after_filter$F_MISS >0.1)

	ggplot(call_rate_samples_after_filter, aes((1-F_MISS)*100)) +
	geom_histogram(bins = 50) +
	theme_bw() +
	ylab ('Sample number') +
	xlab ('Call Rate(%)') +
	geom_vline(xintercept = 90, color = 'red', linetype="dashed") +
	annotate(geom="text", x = 70, y = 200, label = paste0("Number of samples to exclude = ", n_filtered_out),
				color="red", size = 4)

.. note::
	This iteration can help you decide which threshold to choose to exclude low quality samples and SNPs. 
	The threshold depends on the sample size, usually it varies from 95% to 98%.
