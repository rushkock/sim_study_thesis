#!/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458
"""
!!!!!!!!!!!!Deprecated -- see individual_sd1_analysis.py!!!!!!!!!!!!!!!!!
This script aims to explore the subquestion:
How does the permutation test compare to Welch t-test under no violation
of the assumption of homogeneity of variances?
Variance is equal if standard deviations are equal
therefore we only look at these cases
In this script we explore the effect of group ratio on the tests when there is
no violation of homogeneity
"""
import matplotlib.pyplot as plt
from helpers import Helpers
import numpy as np


class Group_ratio(object):
    def __init__(self):
        self.helpers = Helpers()

    def group_ratio_analyses(self, df):
        # groupby SD and typeI or typeII error
        grouped_df = df.groupby(["sd1", "typeI"])

        # Get only the group with homogeneity (sd1 = 1 & sd2 = 1)
        homo_typeI = grouped_df.get_group((1.0, True))
        homo_typeII = grouped_df.get_group((1.0, False))

        # groupby sample size
        homo_samp2_typeI = homo_typeI.groupby("samp2")
        print(homo_typeI)
        print(homo_samp2_typeI)
        homo_samp2_typeII = homo_typeII.groupby("samp2")
        #print(homo_samp2_typeI)
        for key, item in homo_samp2_typeII:
            print(homo_samp2_typeII.get_group(key))

        # get a dataframe for each type of error
        results_typeI = self.helpers.get_mean_df(homo_samp2_typeI, True)
        results_typeII = self.helpers.get_mean_df(homo_samp2_typeII, True)

        # print(f"{results_typeI} \n {results_typeII}")

        # get the latex table for each type of error based on sample size
        typeI_tbl = results_typeI.to_latex()
        typeII_tbl = results_typeII.to_latex()
        #print(f"{typeI_tbl} \n {typeII_tbl}")

        # helpers.boxplots(homo_samp2, 7, 2, "samp2")

        # make a dictionary with the relevant labels and names,make a bar chart
        dictI = {"xlabel": 'Group size', "ylabel": "TypeI error",
                 "title": "Mean typeI error per group size",
                 "xtickslabels": results_typeI.index.tolist()}
        self.bar_chart(results_typeI, 7, dictI)
        dictII = {"xlabel": 'Group size', "ylabel": "TypeII error",
                  "title": "Mean typeII error per group size",
                  "xtickslabels": results_typeII.index.tolist()}
        self.bar_chart(results_typeII, 7, dictII)


    def bar_chart(self, df, n_groups, dict):
        """
        This function makes a barchart for each group size based on a given df
        """
        fig, ax = plt.subplots()
        # choose bar width (standard 0.8 chosen)
        bar_width = 0.35
        # get an index to set the ticks for the x axis

        index = np.arange(n_groups)
        indexes = df.index.tolist()
        print(indexes)
        df["index"] = indexes
        #df["effect_size"] = df["index"].apply(lambda x: x[0])
        #color = ["grey", "Black", "Olive"]

        def get_color(x):
            if x == 0.2:
                return color[0]
            elif x == 0.5:
                return color[1]
            else:
                return color[2]

        #df["edge_color"] = df["effect_size"].apply(get_color)
        #print(df)

        # make barchart for permutation test
        ax.bar(index, df["perm"], bar_width, color='b', linewidth=4,
               label='Permutation test')
               #edgecolor=df["edge_color"])
        # make barchart for t-test
        ax.bar(index + bar_width, df["t_test"], bar_width, color='r',
               label='t-test')
               #linewidth=4,
               #edgecolor=df["edge_color"],
               #)

        ax.set_xlabel(dict["xlabel"])
        ax.set_ylabel(dict["ylabel"])
        ax.set_title(dict["title"])
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(dict["xtickslabels"])
        ax.legend()

        fig.tight_layout()
        plt.show()
