library(dplyr)
groups <- group_by_at(ResultsSimAll, names(Design))
pVal <- function(Method1,Method2){
  return(mcnemar.test(factor(Method1,levels=c(0,1)),factor(Method2,levels=c(0,1)))$p.value)
}
results <- as.data.frame(summarise(groups, mean(Method1), mean(Method2),pVal(Method1,Method2)))
results$typeI <- results$es==0

#add significance tests
results$`pVal(Method1, Method2)` <- results$`pVal(Method1, Method2)`* nrow(results)
results$`pVal(Method1, Method2)`[results$`mean(Method1)`==results$`mean(Method2)`] <- 1
results$`pVal(Method1, Method2)`[results$`pVal(Method1, Method2)`>1] <- 1
results$sig <- rep(FALSE,nrow(results))
results$sig[results$`pVal(Method1, Method2)`<0.05] <- TRUE

#merge
results <- merge(Design,results,by=names(Design),sort=FALSE)
save(results, file = "results.Rdata")