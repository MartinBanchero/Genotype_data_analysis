6. Hardy--Weinberg equilibrium (SNP level)
========================================================================
Violations of HWE can be an indication of the presence of population substructure or the occurrence of a genotyping error. 
While they are not always distinguishable, it is a common practice to assume a genotyping error and remove SNPs for which HWE is violated. 
If case-control status is available, this filtering should be based only on controls as a violation in cases may be an indication of association. 
Departures from HWE are generally measured at a given SNP using a 𝜒2 goodness-of-fit test between the observed and expected genotypes.


.. note::
	Check ped file : does it have phenotypes? If ped doesn't have phenotypes reformat ped to add phenotypes (code not provided).

.. code-block:: r

	# check only controls: I created separate ped only with controls
	runPLINK("--ped only_controls.ped --map file.map --hardy --out Controls_Hardy")

	system("cat Controls_Hardy.hwe | tr -s ' ' '\t' > Controls_Hardy_hwe.tab")

	PLINK_controls_HWE <- read.delim("Controls_Hardy_hwe.tab") %>%
  		select(-X) %>%
  		filter(TEST =="UNAFF")


.. note::
	 Threshold for HWE test statistic can vary. Consider p-value  \< 10e-5 or  \< 10e-6 in controls

