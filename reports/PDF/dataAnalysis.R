#How does the permutation test compare to Welch t-test under no violation of the assumption of homogeneity of variances?
#What is the effect of sample size on the performance of the permutation test under violation of the assumption of homogeneity of variances?
#What is the effect of sample size on the performance of the Welch t-test under violation of the assumption of homogeneity of variances?
#What is the effect of unequal group sizes on the performance of the permutation test under violation of the assumption of homogeneity of variances?
#What is the effect of unequal group sizes on the performance of the Welch t-test under violation of the assumption of homogeneity of variances?

# No violation t-test vs permtest -> when sd1 and sd2 is equal 
library(dplyr)
#groups = group_by_at(pooledMeans, vars(sd1))
#print(groups)
#pooledMeans$dif = pooledMeans$mean(Method1) - pooledMeans$mean(Method2)
print(colnames(pooledMeans))
names(pooledMeans)[names(pooledMeans) == "mean(Method1)"] <- "method1"
names(pooledMeans)[names(pooledMeans) == "mean(Method2)"] <- "method2"

pooledMeans["dif"] <- NA
for (i in 1:nrow(pooledMeans)){
  resultsDesignRowI <- pooledMeans[i,]
  pooledMeans$dif[i] <- (resultsDesignRowI$method1 - resultsDesignRowI$method2)
}

homo <- data.frame("samp1" = integer(), "samp2" = integer(), "es" = integer(), "sd1" = integer(), "sd2" = integer(),
                   "method1" = integer(), "method2" = integer(), "Type1" = integer(), "diff" = integer())
names(homo) = c("samp1", "samp2","es" , "sd1", "sd2", "method1", "method2","Type1", "diff")

for (i in 1:nrow(pooledMeans)){
  resultsDesignRowI <- pooledMeans[i,]
  if (resultsDesignRowI$sd1==1){
    newRow = data.frame(samp1 = resultsDesignRowI$samp1, samp2 = resultsDesignRowI$samp2, es = resultsDesignRowI$es
                     , sd1 = resultsDesignRowI$sd1, sd2 = resultsDesignRowI$sd2, method1 = resultsDesignRowI$method1,
                     method2 = resultsDesignRowI$method2,Type1 = resultsDesignRowI$Type1, 
                     diff =  resultsDesignRowI$diff)
    rbind(homo, newRow)
  }
  
}