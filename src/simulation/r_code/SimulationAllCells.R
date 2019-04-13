source("SimulationOneCell.R")
start.time = Sys.time()

#Total number of cells
TotalCells <- nrow(Design)
for (i in 1:TotalCells){
  Row <- i
  MyResult <- MySimulationCell(Design = Design, RowOfDesign = Row, K = 10000)
  # Write output of one cell of the design
  save(MyResult, file =paste("./Results/MyResult", "Row", Row,".Rdata" , sep =""))
}

end.time = Sys.time()
time.take = end.time - start.time 
print(time.take)