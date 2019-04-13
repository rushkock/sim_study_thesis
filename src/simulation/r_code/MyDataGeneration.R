

#Comparison of power of Mann-Whitney U test and power of t-test
# In group 1 variable Y is from a normal distribution with mu = 0 and sigma = 1
# In group 2 variable Y is from a normal distribution with mu = 0 + es and sigma = 1
# es is "effect size", which is a factor in the simulation design (either 0.2, 0.5, or 0.8) 
# samp = sample size of group 1 = sample size of group 2
# samp = 10, 20, 40, 80
MyDataGeneration <- function(samp1, samp2, es, sd1, sd2){
  averageSD =  sqrt((sd1^2 + sd2^2)/2)
  mean1 = 0
  mean2 = averageSD * es
  var1 <- rnorm(samp1, mean1, sd1) 
  var2 <- rnorm(samp2, mean2, sd2)
  Y <- c(var1, var2)
  group <- as.factor(c(rep(1, samp1), rep(2,samp2)))
  dat <- data.frame(Y, group, mean1, mean2)
  return(dat)
}

