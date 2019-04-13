# This script is used to run the simulation study
# First it runs preparation.R to prepare the files to run
# It then runs SimulationAllCells which performs the simulation for K number of times
# SimulationAllCells saves each cell into multiple files
# collectResults collects all the multiple files into one file called resultsSimAll
# Get error calculates the typeI and typeII error for the resultsSimAll file
# It returns the results as a df
# Rdata2CSV saves the df as a rData file and transforms it into a csv
# It also creates a latex table

setwd("C:/Users/ruche/OneDrive/Documents/sharkLarge/Simulation_study_PC_laptop")
source("Preparation.R")
source("SimulationAllCells.R")
source("collectResults.R")
source("getError.R")
source("Rdata2CSV.R")
