#!/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458
"""
This script gets all condition for a given standard deviation and analyses all
the conditions in these groups seperately.
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
        #self.analyze_based_es()
        self.analyze_group_ratio(sd1)
        #self.typeI_error(sd1)

    def typeI_error(self, sd1):
        """
        This function looks at how often the typeI error of the t-test
        is around 0.05. It does this also for the permutation test
        """
        es = self.group.groupby("es").get_group(0.0).groupby("samp2")
        counter_t = 0
        counter_p = 0
        for key, item in es:
            if item.iloc[0]["t_test"] <= 0.06 and item.iloc[0]["t_test"] >= 0.04:
                counter_t = counter_t + 1

            if item.iloc[0]["perm"] <= 0.06 and item.iloc[0]["perm"] >= 0.04:
                counter_p = counter_p + 1
        print(f"{sd1} : t = {counter_t}, p = {counter_p}")


    def analyze_based_es(self):
        """
        This function analyzes the mean effect sizes
        """
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
        means.to_latex()


    def analyze_group_ratio(self, sd1):
        """
        This function analyzes the groups seperated per effect size
        It calls the multiple bars function
        """
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
