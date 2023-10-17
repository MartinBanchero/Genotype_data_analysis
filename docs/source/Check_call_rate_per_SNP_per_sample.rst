1. Check call rate per SNP and per sample (both SNP and Sample-level)
=========================================================================

The call rate for a given SNP is defined as the proportion of individuals
in the study for which the corresponding SNP information is not missing

The call rate for a given sample is defined as the proportion of SNPs
that is missing for the sample.


.. code-block:: r
	:caption: Call rate per sample (imiss) and per SNP (lmiss)
	
	runPLINK("--ped file.ped --map file.map --missing --out file_call_rate")
	

.. code-block:: r
	:caption:Change format to make it easier for R data frame imiss
	
	system("cat file_call_rate.imiss | tr -s ' ' '\t' > call_rate_sample.tabs")

.. code-block:: r
	:caption: Change format lmiss

	system("cat file_call_rate.lmiss | tr -s ' ' '\t' > call_rate_SNP.tabs")


Plot histograms of call rate per sample
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: r
	:caption: Load call rate SNP and sample.
	
	call_rate_SNP <- read.delim("call_rate_SNP.tabs") %>%
  				select (-X)
	call_rate_samples <- read.delim("call_rate_sample.tabs") %>%
  				select (-X)


Plot histograms of call rate per snp
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

