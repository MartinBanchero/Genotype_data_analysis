(setup-page)=

# Set-up

Most of the steps for the QC will be performed in plink1.9, so it has to be installed.  
Let's prepare the environment by uploading the libraries
Will need gnomestudio, plink1.9, R

(setup-software)=

## Software


Let's prepare the environment by uploading the libraries

```r
library(dplyr)
library(ggplot2)
library(ggrepel)
```
creating the function to run PLINK from the directory where the exe file is:
:::{tip}
You might need to change this function depending on the way you plan to run plink.

```r
runPLINK <- function(PLINKoptions = ''){
  	system(paste("~/Packages/PLINK/plink1.9/plink", PLINKoptions))

```


