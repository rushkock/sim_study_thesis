#Method new: Permutation test
library(perm)

Method_new<- function(SimData){
  formula <- Y~group
  res <- permTS(formula, data = SimData, alternative="two.sided")
  return <- res}
              
