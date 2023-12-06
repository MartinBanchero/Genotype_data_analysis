Final remarks
========================================================================

* You might consider extra QC: Check for swapped samples by comparing SNPs from array vs SNPs from RNA-seq.
* For the imputation take care of the reference genome build used for the creation of the plink files.
* For the imputation on michigan imputation server vcf files are needed. plink function can be used for the that:

    .. code-block:: bash

        --recode vcf

* Consider performing after imputation QC

    .. code-block:: bash

        bcftools view -i 'R2>0.3 & MAF >.05' -Oz [input_file] > [output_file] 

These steps are planned to be updated in the current document

