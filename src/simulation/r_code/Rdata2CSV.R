save(results, file = "results.Rdata")
load("results.Rdata")
write.csv(results,
          file="pooledMeansLargeNew.csv")