(setup-page)=

# Set-up

Will need gnomestudio, plink1.9, R

(setup-software)=

## Software
We can list the software we are going to use. 

:::{tip}
We can define plink function inside R like this

```r
runPLINK <- function(PLINKoptions = ''){
  	system(paste("~/Packages/PLINK/plink1.9/plink", PLINKoptions))

```
