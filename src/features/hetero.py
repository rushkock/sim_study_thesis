# !/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458
"""
This script aims to explore the subquestion:
How does the permutation test compare to Welch t-test under no violation
of the assumption of homogeneity of variances?
Variance is equal if standard deviations are equal
therefore we only look at these cases
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from helpers import Helpers
from group_ratio import Group_ratio


class Hetero(object):
    """
    This script compares the typeI and typeII error when the homogeneity
    assumption is violated
    """
    def __init__(self, df, all_df):
        self.helpers = Helpers()
        self.df = df
        self.all = all_df
        # call the functions in this file
        self.all_conditions_visualized()
        self.within_sd_analysis_es()

    def all_conditions_visualized(self):
        # group dataframe based on standard deviation and effect size
        grouped_df = self.df.groupby(["es", "sd1", "samp2"])
        results = self.helpers.get_mean_df(grouped_df, False)
        print(results.sample())

        # seperate groups based on typeI or typeII error
        dfs = {"typeI_df": results[:8*7],
               "ef_0_2": results[8*7:8*7*2],
               "ef_0_5": results[8*7*2:8*7*3],
               "ef_0_8": results[8*7*3:]}

        for i in dfs:
            sdI = self.get_sd_list(dfs[i], False)
            dictI = {"xlabel": 'Group sizes', "ylabel": "TypeI error",
                     "title": "Mean typeI error per group size",
                     "xtickslabels": sdI}
            self.multiple_bars(dfs[i], 2, 2, dictI)

    def within_sd_analysis_es(self):
        # group dataframe based on standard deviation and effect size
        grouped_df = self.df.groupby(["es", "sd1"])
        results = self.helpers.get_mean_df(grouped_df, False)
        #print(results)

        # seperate groups based on typeI or typeII error
        typeI_df = results[:8]
        typeII_df = results[8:]

        # make a bar chart for typeI error
        sdI = self.get_sd_list(typeI_df, True)
        dictI = {"xlabel": 'Standard deviation', "ylabel": "TypeI error",
                 "title": "Mean typeI error per standard deviation",
                 "xtickslabels": sdI}
        self.helpers.bar_chart(typeI_df, len(typeI_df.index), dictI)

        # make a bar chart for typeII error
        sdII = self.get_sd_list(typeII_df, True)
        dictI = {"xlabel": 'Standard deviation', "ylabel": "TypeII error",
                 "title": "Mean typeII error per standard deviation",
                 "xtickslabels": sdII}
        self.helpers.bar_chart(typeII_df, len(typeII_df.index), dictI)

    def get_sd_list(self, df, bool):
        """
        get a list of the standard deviations
        """
        indexes = df.index.tolist()
        sd = []
        if bool:
            for (i, j) in indexes:
                sd.append(j)
        else:
            for (i, j, k) in indexes:
                sd.append(k)
        return sd

    def multiple_bars(self, df, nrows, ncols, dict):
        """
        Makes a bar chart with mutliple plots in one figure
        """
        fig, axs = plt.subplots(nrows=8, ncols=1, figsize=(6, 9.3), sharey="row")

        fig.subplots_adjust(left=0.03, right=0.97, hspace=0.3, wspace=0.05)

        indexes = df.index.tolist()
        df["index"] = indexes
        df["effect_size"] = df["index"].apply(lambda x: x[0])
        df["sd"] = df["index"].apply(lambda x: x[1])
        df["group"] = df["index"].apply(lambda x: x[2])
        bar_width = 0.35
        # get an index to set the ticks for the x axis

        df_new = df.groupby("sd")
        # for key, item in df_new:
        #     print(df_new.get_group(key))
        for ax, (sd, dat) in zip(axs, df_new):
            n_groups = len(dat.index)
            index = np.arange(n_groups)

            # make barchart for permutation test
            bar1 = ax.bar(index, dat["perm"], bar_width, color='b',
                      label='Permutation test')
            # make barchart for t-test
            bar2 = ax.bar(index + bar_width, dat["t_test"], bar_width, color='r',
                      label='t-test')
            es = dat["effect_size"].iloc[0]

            ax.set_ylabel("Error")
            ax.set_xticks(index + bar_width / 2)
            ax.set_xticklabels(dict["xtickslabels"])
            ax.set_xlabel(f"Mean error for sd = {sd} per group size")
            print(dat["sig"])
            print("\n\n")
            for rect, i in zip(bar1 + bar2, dat["sig"]):
                height = rect.get_height()
                if i:
                    ax.text(rect.get_x() + rect.get_width(), height, "**", ha='center', va='bottom')

        ax.legend()

        fig.suptitle(f"Effect size = {es}", y=1.0, fontsize = 15)
        fig.tight_layout()
        plt.show()
