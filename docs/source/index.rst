.. GenotypeDA-UMCG-GRIAC documentation master file, created by
   sphinx-quickstart on Sat Oct 14 11:00:18 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GenotypeDA-UMCG-GRIAC's documentation!
=================================================
**Genotype DA UMCG-GRIAC** Workflow to cover processing *genotype data* from intensities to imputation and *GWAS analysis*. 
The rationale is describe in the following figure:


.. note::

   This project is under active development.
      
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Genome studio
   
   Generate plink files <Processing_raw_data>
   
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Quality control
   
   Quality control overview<QC_overview>
   Check call rate per SNP and per sample <Check_call_rate_per_SNP_per_sample>
   Check MAF (SNP-level) <Check_MAF>
   Check sample heterozygosity (Sample-level) <Check_sample_heterozygosity>
   Check sex discordance (Sample-level) <Check_sex_discordance>
   Check relatedness (Sample-level) <Check_relatedness>
   Hardy--Weinberg equilibrium (SNP level) <Hardy--Weinberg_equilibrium>
   
   
   
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: GWAS
     
   GWAS steps <GWAS>
   
