sim_study_thesis
==============================

A simulation study comparing the performance of the Welch t-test and the permutation test under the violation of homogeneity

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- All figures produced in data analysis
    │   └── latex          <- The latex code to produce the final pdf 
    │   └── pdf            <- All versions of the thesis
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── R_data_processing   <- Code to turn csv a latex table in R
    │   │
    │   ├── features       <- Scripts for data analysis
    │   │   └── csv        <- Folder with all csv files needed
    │   │   └── python_data_analysis    <- The files used to analyze data 
    ├   |── simulation      <- Scripts used for the simulation
    │       └── r_code      <- R code for simulation 
    │       └── r_projects  <- R projects where simulations were performed 
    │       └── r_results   <- R data with results of simulation (see also src/features/csv for csv files of the results)

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
