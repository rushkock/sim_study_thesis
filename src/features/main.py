#!/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458

from helpers import Helpers
from individual_sd1_analysis import SD_analysis
from hetero import Hetero
from group_ratio import Group_ratio
from across_samples import Across_samples
from initial_exploratory_analysis import Exploratory


def main():
    # name the files that need to be loaded
    # small_csv has performed the simulation for sample size group1 = 10
    # and group2 deviates 25%,50%,75% up and down from group1
    small_csv = "pooledMeansSmallNew.csv"
    small_all = "AllResultsSmall.csv"
    # med_csv has performed the simulation for sample size group1 = 60
    # and group2 deviates 25%,50%,75% up and down from group1
    med_csv = "pooledMeansMedNew.csv"
    med_all = "AllResultsMed.csv"
    # large_csv has performed the simulation for sample size group1 = 1000
    # and group2 deviates 25%,50%,75% up and down from group1
    large_csv = "pooledMeansLargeNew.csv"
    large_all = "AllResultsLarge.csv"

    helpers = Helpers()
    gr = Group_ratio()
    across_samples = Across_samples()


    # make a df of the pooled errors to pass to other functions
    df_small = helpers.get_df(small_csv)
    df_med = helpers.get_df(med_csv)
    df_large = helpers.get_df(large_csv)

    # make a df of the raw results to pass to other functions
    df_small_all = helpers.get_df_all_results(small_all)
    df_med_all = helpers.get_df_all_results(med_all)
    df_large_all = helpers.get_df_all_results(large_all)

    # Choose the sample size and SD
    samp1 = "small"
    sd = 0.25
    # run the files
    #Exploratory(df_small, df_med, df_large)
    if samp1 == "small":
        SD_analysis(df_small, df_small_all, sd)
        #Hetero(df_small, df_small_all)
    elif samp1 == "med":
        SD_analysis(df_med, df_med_all, sd)
        #Hetero(df_med, df_med_all)
    else:
        SD_analysis(df_large, df_large_all, sd)
        #Hetero(df_large, df_large_all)

    #across_samples.across_sample_es(small_csv, med_csv, large_csv)

if __name__ == '__main__':
    main()
