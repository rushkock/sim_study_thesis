library(xtable)
print(xtable(results))

save(results, file = "results.Rdata")
load("results.Rdata")
write.csv(results,
          file="pooledMeansMedNew.csv")
