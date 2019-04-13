#!/usr/bin/env python
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
import matplotlib.pyplot as plt
from helpers import Helpers


class ES(object):
    def analyze_based_es(self, df):
        # make an instance of the class
        helpers = Helpers()

        # get only the group with homogeneity (sd1 = 1 & sd2 = 1)
        grouped_df = df.groupby("sd1")
        homo = grouped_df.get_group(1.0)

        # groupby typeI and typeII error
        homo_es = homo.groupby("es")

        # uncomment if you want to print the groups
        # for key, item in homo_es:
        #      print(homo_es.get_group(key), "\n\n")

        # get min and max difference between the perm and t-test based
        # on effect size
        dif_TypeI = helpers.get_min_max(homo_es, 0.0)
        dif_0_2 = helpers.get_min_max(homo_es, 0.2)
        dif_0_5 = helpers.get_min_max(homo_es, 0.5)
        dif_0_8 = helpers.get_min_max(homo_es, 0.8)

        # get mean for the perm and t-test based on effect size
        mean_typeI = helpers.get_mean(homo_es, 0.0)
        mean_0_2 = helpers.get_mean(homo_es, 0.2)
        mean_0_5 = helpers.get_mean(homo_es, 0.5)
        mean_0_8 = helpers.get_mean(homo_es, 0.8)

        # Dictionary with min and max conditions and mean for perm and t-test
        # based on effect size
        results_each_es = {0.0: [dif_TypeI["min"], dif_TypeI["max"],
                           mean_typeI["perm"], mean_typeI["t_test"]],
                           0.2: [dif_0_2["min"], dif_0_2["max"],
                           mean_0_2["perm"], mean_0_2["t_test"]],
                           0.5: [dif_0_5["min"], dif_0_5["max"],
                           mean_0_5["perm"], mean_0_5["t_test"]],
                           0.8: [dif_0_8["min"], dif_0_8["max"],
                           mean_0_8["perm"], mean_0_8["t_test"]]
        }
        #print(results_each_es)
        helpers.boxplots(homo_es, 4, 2, "es")
