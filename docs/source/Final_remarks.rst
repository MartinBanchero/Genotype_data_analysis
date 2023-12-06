Final remarks
========================================================================

1. You might consider extra QC: Check for swapped samples by comparing SNPs from array vs SNPs from RNA-seq.
2. For the imputation take care of the reference genome build used for the creation of the plink files.
3. For the imputation on michigan imputation server vcf files are needed. plink function can be used for the that:
--recode vcf
4. Consider performing after imputation QC: bcftools view -i 'R2>0.3 & MAF >.05' -Oz [input_file] > [output_file] 

These steps are planned to be updated in the current document

