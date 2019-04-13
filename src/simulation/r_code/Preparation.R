setwd("C:/Users/ruche/OneDrive/Documents/sharkLarge/Simulation_study_PC_laptop")
#Preparation of the analysis
### Initialize the factors of your design:
SampSmall1 = 10
SampSmall2 = c(10, 8, 13, 5, 15, 3, 18)
SampMed1 = 60
SampMed2 = c(60, 45, 75, 30, 90, 15, 105)
SampLarge1 = 1000
SampLarge2 = c(1000, 750, 1250, 500, 1500, 250, 1750)

samp1 <- SampLarge1
samp2 <- SampLarge2
sd1 <- c(1, 0.75, 1.25, 0.50, 1.50, 0.25, 1.75, 3)
sd2 <- 1
es <- c(0, 0.2, 0.5, 0.8)
##And create the simulation design matrix (full factorial)
# Design is a data.frame with all possible combinations of the factor levels
# Each row of the design matrix represents a cell of your simulation design
Design <- expand.grid(samp1 = samp1, samp2 = samp2, es = es, sd1 = sd1, sd2 = sd2)
print(Design)

###Preparation of the analysis:
# If you use R packages that are not standard:
# Install the relevant R packages, for example:
#install.packages("haven")
#install.packages("perm")
#install.packages("xtable")
#install.packages("dplyr")
#Always use library() to activate the package
library(perm)
#NB we do not use this package for our example
### Source the relevant R functions of our example
### These functions are available from:
### https://github.com/Github-MS/Shark/tree/master/Scripts
source("MyDataGeneration.R")
source("Method_new.R")
source("Method_old.R")
source("MyEvaluationPC.R")


#TODO
#Effect size while generating data
#More efficient mean passing through function
#Make sense of how the results are written
#Put results in table
#The point?
#setWD
