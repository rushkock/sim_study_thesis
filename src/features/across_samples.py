#!/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458
import pandas as pd
from helpers import Helpers
from individual_sd1_analysis import SD_analysis
from hetero import Hetero
from group_ratio import Group_ratio


class Across_samples(object):
    def __init__(self):
        self.helpers = Helpers()
        self.gr = Group_ratio()

    def across_sample_es(self, small_csv, med_csv, large_csv):
        helpers = Helpers()
        # get the df's for all the files
        df_small = helpers.get_df(small_csv)
        df_med = helpers.get_df(med_csv)
        df_large = helpers.get_df(large_csv)

        # combine the dataframes for the files
        frames = [df_small, df_med, df_large]
        df = pd.concat(frames)

        ######################################################################
        ###########################  SAMP1 - ES ###############################
        #######################################################################

        # groupby samp1 to have a broad overview of the effect of sample size
        # without taking into account deviation between sample sizes
        grouped_by_samp1 = df.groupby(["samp1", "es"])
        df_samp1 = self.helpers.get_mean_df(grouped_by_samp1, False)
        print(df_samp1)

        # To visualize this we can make two types of bar charts. One for each
        # effect size but all 3 samp1 (10,60,1000). Or one where effect sizes
        # are compared but group sizes aren't visible in the plot. The latter
        # plot already exists and in this script we compare across group sizes
        # that is why the first type of plot is chosen.
        grouped_by_samp1 = df.groupby(["es", "samp1"])
        df_samp1 = self.helpers.get_mean_df(grouped_by_samp1, False)
        print(df_samp1)
        dict = {"xlabel": 'Group size', "ylabel": "TypeI error",
                 "title": "Mean typeI error per group size",
                 "xtickslabels": df_samp1.index.tolist()}
        self.gr.bar_chart(df_samp1, 3, dict)


        #######################################################################
        ########################  SAMP1 - SAMP2 - ES ##########################
        #######################################################################

        # Now lets take into account group size deviation
        # First we group based on the two groups then we compare
        # them across effect sizes
        grouped_by_samp1_samp2 = df.groupby(["samp1", "samp2", "es"])
        df_samp1_samp2 = self.helpers.get_mean_df(grouped_by_samp1_samp2, False)
        #print(df_samp1_samp2)

        ######################################################################
        #######################  SAMP1 - SAMP2 SD1 - ES ######################
        #######################################################################
        # Now if we also take sd deviation into account
        # we end up with the same df that we stated with (672 columns)
        # At this point this becomes too complicated to plot or analyze
        grouped_by_samp1_samp2_sd1 = df.groupby(["samp1", "samp2", "sd1", "es"])


        ######################################################################
        ########################  SAMP1 - SD1  - ES ##########################
        #######################################################################

        # Now we forget samp2 and we just look at the effect of sd1
        # This gives information based on how much the homogeneity was violated
        # and its effect across sample size : samp1 (not group ratio)
        grouped_by_samp1_sd1 = df.groupby(["samp1", "sd1", "es"])
        df_samp1_sd1 = self.helpers.get_mean_df(grouped_by_samp1_sd1, False)
        #print(df_samp1_sd1)
