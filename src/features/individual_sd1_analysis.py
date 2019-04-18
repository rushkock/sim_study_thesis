#!/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458
"""
!!!!!!!!!!!!!!! Rename !!!!!!!!!!!!!!!!!!!!!!!!!!
This script aims to explore the subquestion:
How does the permutation test compare to Welch t-test under no violation
of the assumption of homogeneity of variances?
Variance is equal if standard deviations are equal
therefore we only look at these cases
"""
from helpers import Helpers


class SD_analysis(object):
    def __init__(self, df, df_all, sd1):
        # make an instance of the class
        self.helpers = Helpers()
        # may delete later if not needed
        self.df = df
        self.all = df_all

        # groups where homogeneity is not violated
        self.group = df.groupby("sd1").get_group(sd1)
        self.group_all = df_all.groupby("sd1").get_group(sd1)

        # Call the functions in this file
        self.analyze_based_es()
        self.analyze_group_ratio(sd1)

    def analyze_based_es(self):
        # groupby effect sizes
        es = self.group.groupby("es")

        # get dataframe wtith pooled means per effect size for each test
        # when homogeneity was not violated
        means = self.helpers.get_mean_df(es, False)

        # Here we analyze the raw file with 0 and 1's to test significance
        # for the conditions when homogeneity was not violated
        es_all = self.group_all.groupby("es")

        # perform the mcnemar test for each effect size combine it with the
        # means table
        means = self.helpers.means_and_pval(means, es_all)
        print(means)
        print(means.to_latex())

        # If we print df we see that for the effect size 0.0 and 0.2 there is a
        # significant difference between the tests
        # in effect size 0.0 the t_test(typeI error = 0.052586) has more errors
        # than the permutation test(typeI error = 0.048571) with a difference
        # of 0.004014 between the two tests
        # in effect size 0.2 the permutation test(typeII error = 0.932886) has
        # more error than the t_test(typeII error = 0.929886) with a difference
        # of 0.003000

        # I decided not to make a plot because the table is already very clear

        ######################################################################
        ##################### Analyze group ratios ###########################
        ######################################################################

    def analyze_group_ratio(self, sd1):
        # groupby effect sizes .. because this is only one group
        # (with only 1 sd1) it means that if we want to analyze group ratios
        # we need to analyze the whole df because the only changes are the
        # group ratios and effect sizes. We seperate by es and then check which
        # rows are significantly different
        es = self.group.groupby(["es"])
        dict = {"xlabel": 'Group size', "ylabel": "TypeI error",
                 "title": f"SD1 = {sd1}, SD2 = 1",
                 "xtickslabels": es.get_group(0.0)["samp2"]}
        for key, item in es:
            item["pval"] = item["pval"].round(decimals=4)
            print(item)
        self.helpers.multiple_bars(es, 2, 2, dict)
