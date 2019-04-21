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

    # make an instance of the classes
    helpers = Helpers()
    gr = Group_ratio()
    across_samples = Across_samples()

    def round_pval(x):
        """
        Round the p_value
        """
        return f"{round(x, 3):3.3f}"

    def leading_zero_es(x):
        """
        Round the p_value
        """
        return str(x).lstrip("0")

    def remove_leading_zeroes(x):
        """
        Remove leading zero's for perm and t_test columns
        """
        return round_pval(x).lstrip("0")

    def print_latex_table(df):
        format_pval = {"pval": round_pval, "perm": remove_leading_zeroes,
                       "t_test": remove_leading_zeroes, "es": leading_zero_es}
        print(df.to_latex(index=False, float_format="%3.3f", formatters=format_pval))

    # make a df of the pooled errors to pass to other functions
    df_small = helpers.get_df(small_csv)
    df_med = helpers.get_df(med_csv)
    df_med_practice = helpers.get_df("AllResultsMedPractice.csv")
    df_large = helpers.get_df(large_csv)

    list_of_dfs = [df_small, df_med, df_large, df_med_practice]
    for i in list_of_dfs:
        print_latex_table(i)

    # make a df of the raw results to pass to other functions
    df_small_all = helpers.get_df_all_results(small_all)
    df_med_all = helpers.get_df_all_results(med_all)
    df_large_all = helpers.get_df_all_results(large_all)

    # Choose the sample size and SD
    # note add command line argument to choose sample
    samp1 = "small"
    sds = [0.25, 0.50, 0.75, 1.0, 1.25, 1.50, 1.75]
    #run the files
    for i in sds:
        Exploratory(df_small, df_med, df_large)
        if samp1 == "small":
            SD_analysis(df_small, df_small_all, i)
            Hetero(df_small, df_small_all)
        elif samp1 == "med":
            SD_analysis(df_med, df_med_all, i)
            Hetero(df_med, df_med_all)
        else:
            SD_analysis(df_large, df_large_all, i)
            Hetero(df_large, df_large_all)

if __name__ == '__main__':
    main()
