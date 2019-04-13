#Evaluation Criterion: 
#to determine the power of the method: 
#is the p-value of the test significant at 0.05 level?
#if yes, then the test rejected the null-hypothesis that the difference 
#between the groups is 0: i.e., the alternative hypothesis is correctly accepted
#if no, then the null hypothesis is incorrectly not rejected.

MyEvaluationPC <- function(MyAnalysisResult, es){
  if (es == 0){
    if (MyAnalysisResult$p.value < 0.05 ){
      res = 1
    }
    else{
      res = 0
    }
  }
  else{
    if (MyAnalysisResult$p.value > 0.05 ){
      res = 1
    }
    else{
      res = 0
    }
  }
  return(res)
}