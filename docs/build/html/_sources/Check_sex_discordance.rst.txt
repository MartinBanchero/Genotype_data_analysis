4. Check sex discordance (Sample-level)
========================================================================
Sample mix-up is investigated by looking at sex mismatch, where sex
information of each sample is compared with genotypes at chromosomes X and Y.

.. note:: 
	**NB:** This method however does not detect same sex sample mix-ups and is not reliable when there are sex chromosome abnormalities.

.. note::
	**NB:** Fot this step check that ped file has recorded sex, otherwise consider using sex from metadata

.. code-block:: r
	:caption: For this step we need to use files with already excluded low call rate SNPs

	runPLINK("--ped file.ped --map file.map --mind 0.1 --recode --out file_SNP_filtered")

.. code-block:: r
	:caption: Now let’s check check sex discordance

	runPLINK("--ped file_SNP_filtered.ped --map file_SNP_filtered.map --check-sex --out file_SNP_filtered")
	system("cat file_SNP_filtered.sexcheck | tr -s ' ' '\t' >  file_SNP_filtered_sexcheck.tabs")

.. code-block:: r
	:caption: Plot reported sex vs F value (X heterozygosity level).

	Plink_sex_filtered <- read.delim("file_SNP_filtered_sexcheck.tabs") %>%
		select(-X)
	Plink_sex_filtered <- Plink_sex_filtered %>%
	  mutate(PEDSEX = if_else(PEDSEX == "2", "female", "male"))

	ggplot(Plink_sex_filtered, aes(x=PEDSEX, y= `F`)) +
		geom_jitter(color = ifelse((Plink_sex_filtered$PEDSEX == "female"), "red", "blue")) +
		geom_text_repel(aes(label=ifelse(((PEDSEX == "female") & ("F" > 0.2)), IID, ""),
							hjust = 0.4, vjust= 0.4))+
		xlab("Reported sex")+
		ylab("Heterozygosity rate")+
		theme_bw()

.. note:: 
	plink report marks problematic samples, this information should be available in file_SNP_filtered_sexcheck.tabs 
	**Advice** It is also important to look at the plot and asses it visually

Check Y chr counts also if there are strange samples
------------------------------------------------------------------------------

.. code-block:: r
	
	runPLINK("--ped file_SNP_filtered.ped --map file_SNP_filtered.map --check-sex ycount --out file_SNP_filtered_ycount")
	system("cat file_SNP_filtered_ycount.sexcheck | tr -s ' ' '\t' > file_SNP_filtered_ycount_sexcheck.tabs")
	Plink_sex_filtered_ycount <- read.delim("file_SNP_filtered_ycount_sexcheck.tabs") %>%
  		select(-X)

.. code-block:: r
	:caption: Plot y chromosome counts

	Plink_sex_filtered_ycount <- Plink_sex_filtered_ycount %>%
  		mutate(PEDSEX = if_else(PEDSEX == "2", "female", "male"))

	ggplot(Plink_sex_filtered_ycount, aes(x=PEDSEX, y= YCOUNT )) +
		geom_text_repel(aes(label=ifelse(((PEDSEX == "male") & (YCOUNT < 3000)), IID,""),
						hjust= 0.4, vjust= 0.4)) +
		xlab("Reported sex") +
		ylab("Y counts") +
		theme_bw()

.. note:: 
	**Advice:** Look at the plot and check that males and females samples are clearly separating on Y-axis

