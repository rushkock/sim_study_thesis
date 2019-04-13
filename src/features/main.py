#!/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458

from helpers import Helpers
from es import ES
from hetero import Hetero
from group_ratio import Group_ratio
from across_samples import Across_samples


def main():
    # name the files that need to be loaded
    # small_csv has performed the simulation for sample size group1 = 10
    # and group2 deviates 25%,50%,75% up and down from group1
    small_csv = "pooledMeansSmall.csv"
    # med_csv has performed the simulation for sample size group1 = 60
    # and group2 deviates 25%,50%,75% up and down from group1
    med_csv = "pooledMeansMed.csv"
    # large_csv has performed the simulation for sample size group1 = 1000
    # and group2 deviates 25%,50%,75% up and down from group1
    large_csv = "pooledMeansLarge.csv"

    helpers = Helpers()
    es = ES()
    gr = Group_ratio()
    across_samples = Across_samples()
    hetero = Hetero()

    # make a df to pass to other functions
    df = helpers.get_df(small_csv)

    es.analyze_based_es(df)
    gr.group_ratio_analyses(df)
    hetero.within_sd_analysis_es(df)
    hetero.within_sd_analysis_sd(df)
    #across_samples.across_sample_es(small_csv, med_csv, large_csv)


if __name__ == '__main__':
    main()
