# Simulation study

This simulation study was written and run in RStudio. The code used to run the simulation study can be found in the folder r_code. The unprocessed results can be found in r_results (notes the names are slightly changed). The raw results can be found on google drive.
The Rprojects are provided in r_proj.

## Prerequisites

The libraries necessary to run the simulation can be found in requirements.txt.
They can be download using:

```
packages.install("name").
```

Alternatively the code to download them can be uncommented in Preparation.R.

## Test

To run the simulation use the following command

```
source(main.R)
```

However, this code is not directly executable as the author has working directories and paths hard coded. Moreover, the simulation has never been tested on another laptop.

## Additional information
The simulation was run 3 times each time using different sample sizes. K was always 10000.

### Running time
- The smallest sample sizes were spread around 10
this took approximately 4 hours

- The medium sample sizes spread around 60 took approximately 4 hours

- The largest sample sizes spread around 10000 took
approximately 30 hours

## Acknowledgments

* https://github.com/Github-MS/Shark
* https://github.com/karchjd/Shark
