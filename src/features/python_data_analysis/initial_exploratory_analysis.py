#!/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458
"""
This script perform initial analyses it looks at the most desirable conditions
where there is no violation at all.
It also analyses patterns to see in which conditions a lot of significant
differences are found
It also checks when the t-test outperforms the permutation test and vice versa
to try and find a pattern in there
"""
import pandas as pd
import matplotlib.pyplot as plt
from helpers import Helpers


class Exploratory(object):
    def __init__(self, df_small, df_med, df_large):
        self.helpers = Helpers()
        self.desirable_conditions(df_small, df_med, df_large)
        self.t_vs_p(df_small, "10")

    def desirable_conditions(self, df_small, df_med, df_large):
        """
        This function only looks at the most desirable conditions across
        samples (CSV). This desirable condition is when group sizes are
        equal and there is no violation of homogeneity
        """
        small = self.get_equal_conditions(df_small)
        med = self.get_equal_conditions(df_med)
        large = self.get_equal_conditions(df_large)
        frames = [small, med, large]
        results = pd.concat(frames)
        results["pval"] = results["pval"].round(decimals=2)
        print(results.to_latex())

    def get_equal_conditions(self, df):
        """
        This function returns the conditions where there is no deviation of
        standard deviation or group sizes
        """
        conditions = df.loc[(df["sd1"] == df["sd2"]) &
                            (df["samp1"] == df["samp2"])]
        return conditions

    def t_vs_p(self, df, df_type):
        """
        This function checks when the t-test outperforms the permutation test
        and vice versa
        """
        sig_dif = df.loc[(df["sig"])]
        perm_better_conditions = sig_dif.loc[(df["dif"] < 0)]
        t_test_better_conditions = sig_dif.loc[(df["dif"] > 0)]
        print(f"perm better: {len(perm_better_conditions)}")
        # prints 94 so the permutation test is significantly better than the
        # t-test 94 times
        print(f"t_test better: {len(t_test_better_conditions)}")

        # Analyze the number of significant differences without taking into
        # account the two tests and which one outperforms which.
        self.pattern_analysis(df, df_type)
        # prints 97 so the t-test is significantly better than the
        # perm 97 times

        # They seem to be equally well t-test only slightly being significantly
        # different more times
        # Is there a pattern? Lets analyze the conditions seperately
        es_perm = perm_better_conditions.groupby("es")
        dfs = self.return_list_of_dfs(es_perm, "samp2")
        value = f"The group ratios where the permutation test outperforms the t-test \n Sample size = {df_type}"
        self.make_pies(dfs, value, df_type)

        es_t_test = t_test_better_conditions.groupby("es")
        dfs = self.return_list_of_dfs(es_t_test, "samp2")
        value = f"The group ratios where the t-test outperforms the permutation test \n Sample size = {df_type}"
        self.make_pies(dfs, value, df_type)

        dfs = self.return_list_of_dfs(es_perm, "sd1")
        value = f"The standard deviations where the permutation test outperforms the t-test \n Sample size = {df_type}"
        self.make_pies(dfs, value, df_type)

        dfs = self.return_list_of_dfs(es_t_test, "sd1")
        value = f"The standard deviations where the t-test outperforms the permutation test \n Sample size = {df_type}"
        self.make_pies(dfs, value, df_type)

    def pattern_analysis(self, df, df_type):
        """
        Analyze how many times there was a significant difference in the
        deviations of group size of sd1
        """
        sig_dif = df.loc[(df["sig"])]
        es = sig_dif.groupby("es")

        value = f"Number of significant differences between Perm & T-test per group ratios \n Sample size = {df_type}"
        dfs = self.return_list_of_dfs(es, "samp2")
        self.make_pies(dfs, value, df_type)
        value = f"Number of significant differences between Perm & T-test per standard deviation \n Sample size = {df_type}"
        dfs = self.return_list_of_dfs(es, "sd1")
        self.make_pies(dfs, value, df_type)

        # what I see is that when there is no devitation the number of
        # singnificant differences
        # are small, otherwise there isnt really a pattern

    def return_list_of_dfs(self, groupby_object, column):
        """
        Returns a list of dataframes where each dataframe is groupedby column
        (e.g. standard deviation)
        The dataframe contains an index (e.g. sd1= 1.0) and
        the length of each group
        """
        dfs = []
        for key, item in groupby_object:
            group = item.groupby([column])
            dict = {}
            for key, item in group:
                dict.update({key: len(item)})
            df = pd.DataFrame.from_dict(dict, orient="index")
            df.columns = ["length"]
            dfs.append(df)
        return dfs

    def make_pies(self, dfs, value, df_type):
        """
        This function makes 4 pie charts in 1 figure
        Each pie is for one effect size
        It plots the number of significant differences
        per value(e.g. standard deviation)
        """
        fig, axs = plt.subplots(2, 2)

        def make_autopct(values):
            def my_autopct(pct):
                total = sum(values)
                val = int(round(pct*total/100.0))
                return '{p:.0f}% ({v:d})'.format(p=pct,v=val)
            return my_autopct
        colors = ["#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3",
                  "#fdb462", "#b3de69", "#fccde5", "#d9d9d9"]
        axs[0, 0].pie(dfs[0]["length"], autopct=make_autopct(dfs[0]["length"]),
                      labels=dfs[0].index.tolist(), colors=colors)
        axs[0, 0].set_title("Effect Size =  0.0")
        axs[0, 1].pie(dfs[1]["length"], autopct=make_autopct(dfs[1]["length"]),
                      labels=dfs[1].index.tolist(), colors=colors)
        axs[0, 1].set_title("Effect Size =  0.2")

        if df_type != "1000":
            axs[1, 0].pie(dfs[2]["length"], autopct=make_autopct(dfs[2]["length"]),
                          labels=dfs[2].index.tolist(), colors=colors)
            axs[1, 0].set_title("Effect Size =  0.5")
            axs[1, 1].pie(dfs[3]["length"], autopct=make_autopct(dfs[3]["length"]),
                          labels=dfs[3].index.tolist(), colors=colors)
            axs[1, 1].set_title("Effect Size =  0.8")

        fig.suptitle(value)
        plt.show()
