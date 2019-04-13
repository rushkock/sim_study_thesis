#Method old: t-test

Method_old<- function(SimData){
  formula <- Y~group
  res <- t.test(formula, data = SimData, var.equal = FALSE)
  return <- res}

