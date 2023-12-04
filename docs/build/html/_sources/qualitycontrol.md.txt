(qualitycontrol-page)=

## 1. Check call rate per SNP and per sample (both SNP and Sample-level)

The call rate for a given SNP is defined as the proportion of individuals
in the study for which the corresponding SNP information is not missing

The call rate for a given sample is defined as the proportion of SNPs
that is missing for the sample.

### Call rate per sample (imiss) and per SNP (lmiss)

```r
runPLINK("--ped file.ped --map file.map --missing --out file_call_rate")
```

:::{tip}

- Change format to make it easier for R data frame imiss:

```r
   system("cat file_call_rate.imiss | tr -s ' ' '\t' > call_rate_sample.tabs")
```

- Change format lmiss

```r
system("cat file_call_rate.lmiss | tr -s ' ' '\t' > call_rate_SNP.tabs")
```
:::


### Plot histograms of call rate per sample
Load call rate SNP and sample.

```r
	call_rate_SNP <- read.delim("call_rate_SNP.tabs") %>%
  				select (-X)
	call_rate_samples <- read.delim("call_rate_sample.tabs") %>%
  				select (-X)
```


### Plot histograms of call rate per snp

```r
#calculate n of filtered our samples with missing rate < 0.1
n_filtered_out <- sum(call_rate_SNP$F_MISS >=0.1)

ggplot(call_rate_SNP, aes((1-F_MISS)*100)) +
  geom_histogram(bins = 50) +
  theme_bw() +
  ylab ('SNP number') +
  xlab ('Call Rate(%)') +
  geom_vline(xintercept = 90, color = 'red', linetype="dashed") +
  annotate(geom = "text", x = 70, y = 100000, label = paste0("Number of SNPs to exclude = ",
                                                     n_filtered_out),
           color="red", size = 4)
```


Exclude SNPs with call rate \< 90% and check again sample call rate

```r
runPLINK("--ped file.ped --map file.map --geno 0.1 --recode --out file_filtered_snps")

# check again sample call rate: 
runPLINK("--ped file_filtered_snps.ped --map file_filtered_snps.map --missing --out file_call_rate_filtered_snps")

system("cat file_call_rate_filtered_snps.imiss | tr -s ' ' '\t' > file_call_rate_filtered_snps_imiss.tabs")

call_rate_samples_after_filter <- read.delim("file_call_rate_filtered_snps_imiss.tabs")%>%
  select (-X)
```

### Plot histograms of call rate per sample after filtered SNPs

:::{tip}
This iteration can help you decide which threshold to choose to exclude low quality samples and SNPs.
The threshold depends on the sample size, usually it varies from 95% to 98%.
:::

```r 
n_filtered_out <- sum(call_rate_samples_after_filter$F_MISS >0.1)

ggplot(call_rate_samples_after_filter, aes((1-F_MISS)*100)) +
  geom_histogram(bins = 50) +
  theme_bw() +
  ylab ('Sample number') +
  xlab ('Call Rate(%)') +
  geom_vline(xintercept = 90, color = 'red', linetype="dashed") +
  annotate(geom="text", x = 70, y = 200, label = paste0("Number of samples to exclude = ", 
                                                  n_filtered_out),
           color="red", size = 4)
```

(checkMAF-page)=

## 2. Check MAF (SNP-level)

Minor allele frequency (MAF). A large degree of homogeneity at a given SNP
across study participants generally results in inadequate power to infer a statistically significant
relationship between the SNP and the trait under study. This can occur when we have a very small
MAF so that the large majority of individuals have two copies of the major allele.

:::{tip}
Threshold for MAF can vary between 1% and 5% (for small sample settings)

```r
runPLINK("--ped file.ped --map file.map --freq --out file_maf")

system("cat file_maf.frq | tr -s ' ' '\t' > file_maf_frq.tabs")
```
:::

### Plot MAF histogram

:::{tip}
 For small sample size it is recommended to exclude SNPs with MAF \< 0.05.
::: 

```r
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
  geom_vline(xintercept = 0.05, color = 'grey', linetype="dashed")+
  annotate(geom="text", x=0.043, y=100000, label=paste0("maf= 0.05    ", maf_05, ' SNPs'),
           angle = 90, color="red", size = 3)
```

(checkheterozygo-page)=

## 3. Check sample heterozygosity (Sample-level)

Heterozygosity refers to the presence of each of the two alleles
at a given SNP within an individual.  
Outliers showing excess or depletion in heterozygotes
genotypes may be due to contamination or issues during genotyping process.

should we do it already only with high call rate SNPs? 

```r 
runPLINK("--ped file.ped --map file.map --het --out file")

system("cat file.het | tr -s ' ' '\t' > file_het.tabs")

het_level <- read.delim ("file_het.tabs")%>%
  select (-X)
```

### Plot sample call rate vs heterozygosity

:::{tip}
Exclude samples with more than 3 standard deviations away from mean heterozygosity. 
Lifelines uses 4sd from the mean heterozygosity. 
:::


```r
sample_missing_rate_het <- call_rate_samples_after_filter %>%
  left_join(het_level, by = c("IID" = "IID")) %>%
  rename(heter_rate = "F")
std = sd(sample_missing_rate_het$heter_rate) ## calculate standard deviation
std_list = c(std, -std, 2*std, -2*std, 3*std, -3*std)

ggplot(sample_missing_rate_het, aes(x= F_MISS, y= heter_rate)) +
  geom_point() +
  geom_vline(xintercept = 0.1, linetype="dashed", color = "blue") +
  geom_hline(yintercept = std_list[1:4], col = 'grey', linetype = "dashed") +
  geom_hline(yintercept = std_list[5:6], col = 'red', linetype = "dashed") + 
  ggtitle("Heterozygosity vs Missingness across samples") + 
  theme_bw() +
  xlab("Proportion of missing SNPs")+
  ylab("Heterozygosity rate(+- 3 sd)")
```
(checksex-page)=
## 4. Check sex discordance (Sample-level)

Sample mix-up is investigated by looking at sex mismatch, where sex
information of each sample is compared with genotypes at chromosomes X and Y.

*NB: This method however does not detect same sex sample mix-ups and is not reliable
when there are sex chromosome abnormalities.*

??For this step we need to use files with already excluded low call rate SNPs 

```r
runPLINK("--ped file.ped --map file.map --mind 0.1 --recode --out file_SNP_filtered")
```

Now let's check check sex discordance

```r
runPLINK("--ped file_SNP_filtered.ped --map file_SNP_filtered.map --check-sex --out file_SNP_filtered")

system("cat file_SNP_filtered.sexcheck | tr -s ' ' '\t' >  file_SNP_filtered_sexcheck.tabs")
```

### Plot reported sex vs F value (X heterozygosity level). 
Reported sex will is taken from .ped file by plink 

```r
Plink_sex_filtered <- read.delim("file_SNP_filtered_sexcheck.tabs")%>%
  select(-X)
Plink_sex_filtered <- Plink_sex_filtered%>%
  mutate(PEDSEX = if_else(PEDSEX == "2", "female", "male"))

ggplot(Plink_sex_filtered, aes(x=PEDSEX, y= `F`)) +
  geom_jitter(color = ifelse((Plink_sex_filtered$PEDSEX == "female"), "red", "blue"))+
  geom_text_repel(aes(label=ifelse(((PEDSEX == "female") & ("F" > 0.2)), IID, ""),
                      hjust = 0.4, vjust= 0.4))+
  xlab("Reported sex")+
  ylab("Heterozygosity rate")+
  theme_bw()
```

:::{tip}
plink report marks problematic samples, this information should be available in *file_SNP_filtered_sexcheck.tabs*

**Advised:** It is also important to look at the plot and asses it visually 
:::

(checkheterozygo-page)=

### Check Y chr counts also if there are strange samples

```r
runPLINK("--ped file_SNP_filtered.ped --map file_SNP_filtered.map --check-sex ycount --out file_SNP_filtered_ycount")
system("cat file_SNP_filtered_ycount.sexcheck | tr -s ' ' '\t' > file_SNP_filtered_ycount_sexcheck.tabs")
Plink_sex_filtered_ycount <- read.delim("file_SNP_filtered_ycount_sexcheck.tabs") %>%
  select(-X)
```

### Plot y chromosome counts

**Advised** Look at the plot and check that males and females samples are clearly separating on Y-axis 

```r
Plink_sex_filtered_ycount <- Plink_sex_filtered_ycount%>%
  mutate(PEDSEX = if_else(PEDSEX == "2", "female", "male"))

ggplot(Plink_sex_filtered_ycount, aes(x=PEDSEX, y= YCOUNT )) +
  geom_text_repel(aes(label=ifelse(((PEDSEX == "male") & (YCOUNT < 3000)), IID,""),
                      hjust= 0.4, vjust= 0.4)) +
  xlab("Reported sex") +
  ylab("Y counts") +
  theme_bw()

```

(checkrelatedness-page)=

## 5. Check relatedness (Sample-level)

Population-based cohort studies are often limited to unrelated individuals, and the generalized linear modeling approach
(used in GWAS) assumes independence across individuals. Importantly, in regional cohort studies (e.g., hospital-based cohort studies) of complex
diseases, individuals from the same family can be recruited unintentionally. A common measure
of relatedness (or duplication) between pairs of samples is based on identity by descent (IBD). An
IBD kinship coefficient of greater than 0.1875 may suggest relatedness, duplicates, or sample mixture.
Typically, the individual of a related pair with lower genotype call rate is removed.

### LD pruning
First we need to perform linkage disequilibrium (LD) pruning with a threshold value of 0.7 (this could vary, some studies use 0.2) - remove SNPs with high LD with each other (removes one from each pair). 
This eliminates a large degree of redundancy in the data. 
This dimension reduction step is commonly applied prior to both IBD analysis and PCA. 

```r
runPLINK("--ped file.ped --map file.map --indep-pairwise 50 5 0.7 --out file")
```

Keep only selected snps for your data

```r
runPLINK("--ped file.ped --map file.map --exclude file.prune.out --recode --out prunedSet")

```

### Calculate IBD - identity by descent 
Defined as the degree of recent shared ancestry.

```r
runPLINK('--ped prunedSet.ped --map prunedSet.map --Z-genome --out Pruned_IBD')
```

Change format 
```r
system("zcat Pruned_IBD.genome.gz | tr -s ' ' '\t' > Pruned_IBD.tabs")

```

Let's check samples with IBD \> 0.1875 (PI_HAT column in the plink output)

:::{tip}
Check the table and exclude one from the pair with the lower call rate (code not provided)
:::

```r
IBD_high_relat <- IBD%>%
  filter(PI_HAT> 0.1875)
print(IBD_high_relat)
```

(checkHW-page)=

## 6. Hardy--Weinberg equilibrium (SNP level)

Violations of HWE can be an indication of the presence of population
substructure or the occurrence of a genotyping error. While they are not always distinguishable, it is
a common practice to assume a genotyping error and remove SNPs for which HWE is violated. 
If case-control status is available, this filtering should be based only on controls as a violation in cases
may be an indication of association. 
Departures from HWE are generally measured at a given SNP
using a 𝜒2 goodness-of-fit test between the observed and expected genotypes. 


Check ped file : does it have phenotypes? If ped doesn't have phenotypes reformat ped to add phenotypes (code not provided).
Check only controls: I created separate ped only with controls.
:::{tip}
Threshold for HWE test statistic can vary. 
Consider to exclude SNPs with p-value  \< 10e-5 or  \< 10e-6 in controls
:::

```r

runPLINK("--ped only_controls.ped --map file.map --hardy --out Controls_Hardy")

system("cat Controls_Hardy.hwe | tr -s ' ' '\t' > Controls_Hardy_hwe.tab")

PLINK_controls_HWE <- read.delim("Controls_Hardy_hwe.tab") %>%
  select(-X) %>%
  filter(TEST =="UNAFF")
```

(checkPCA-page)=

## 7. Sample QC: PCA 

Identification of individuals of divergent ancestry.
This step requires reference dataset with diverse ethnicities (HGDP / HapMap).
Exclusion of the individuals might depend on the research questions.

#### Last step:
Create a list of all the SNPs and samples you need to exclude.

Create filterd bed file (output format could be different)
```r
runPLINK("--ped file.ped --map file.map --remove to.be.deleted.ind --exclude fail-snp-qc.txt --make-bed --out file.QCed")
```

(Finalremarks-page)=
## Final remarks 
1. You might consider extra QC: Check for swapped samples by comparing SNPs from array vs SNPs from RNA-seq.
2. For the imputation take care of the reference genome build used for the creation of the plink files.
3. For the imputation on michigan imputation server vcf files are needed. plink function can be used for the that:  
`--recode vcf`
4. Consider performing after imputation QC: 
```bash
bcftools view -i 'R2>0.3 & MAF >.05' -Oz [input_file] > [output_file]
```
These steps are planned to be updated in the current document.

## Author
Tatiana Karp

(references-page)=
## References
1. Turner, Stephen, et al. "Quality control procedures for genome‐wide association studies." Current protocols in human genetics 68.1 (2011): 1-19.
2. Reed, Eric, et al. "A guide to genome‐wide association analysis and post‐analytic interrogation." Statistics in medicine 34.28 (2015): 3769-3792.
3. Anderson, Carl A., et al. "Data quality control in genetic case-control association studies." Nature protocols 5.9 (2010): 1564-1573.






