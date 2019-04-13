#!/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458
import pandas as pd
import matplotlib.pyplot as plt


class Helpers(object):
    """
    General functions such as get the mean or max
    note improve the info
    """
    def __init__(self):
        size = "small_csv"
        if size == "small_csv":
            self.sample_order = [10, 8, 13, 5, 15, 3, 18]
        elif size == "med_csv":
            self.sample_order = [60, 45, 75, 30, 90, 15, 105]
        else:
            self.sample_order = [1000, 750, 1250, 500, 1500, 250, 1750]

    def get_df(self, file):
        # read csv into dataframe
        df = pd.read_csv(file)
        # rename columns
        names = ["samp1", "samp2", "es", "sd1", "sd2", "perm", "t_test",
                 "pval", "typeI", "sig" ]
        df.columns = names

        # make a new column with the difference between the two tests
        df["dif"] = df["t_test"] - df["perm"]
        return df

    def get_min_max(self, groups, key):
        """
        This function gets the min and the max for the permutation test and the
        t-test. It does this for a group with a given effect size(es)
        """
        group = groups.get_group(key)
        min = group.loc[group["dif"].idxmin()]
        max = group.loc[group["dif"].idxmax()]
        minmax = {"min": min, "max": max}
        return minmax

    def get_mean(self, groups, key):
        """
        This function calculates the means for the permutation test and the
        t-test.
        """
        group = groups.get_group(key)
        perm = group["perm"].mean()
        t_test = group["t_test"].mean()
        means = {"perm": perm, "t_test": t_test}
        return means

    def get_descriptive(self, groups, key):
        group = groups.get_group(key)
        perm = group["perm"].describe()
        t_test = group["t_test"].describe()
        means = {"perm": perm, "t_test": t_test}
        return means

    def boxplots(self, groups, nrows, ncols, type):
        fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(6, 9.3), sharey="row")

        fig.subplots_adjust(left=0.03, right=0.97, hspace=0.3, wspace=0.05)

        for ax, (effs, dat) in zip(axs, groups):
            ax[0].boxplot(dat["perm"])
            ax[1].boxplot(dat["t_test"])
            ax[0].set_ylabel("Errors")
            if type == "es":
                ax[0].set_title(f"Effect size = {effs}, Test = Perm")
                ax[1].set_title(f"Effect size = {effs}, Test = t-test")
            elif type == "samp2":
                ax[0].set_title(f"Sample size = {effs}, Test = Perm")
                ax[1].set_title(f"Sample size = {effs}, Test = t-test")


        plt.tight_layout()
        #plt.show()

    def get_mean_df(self, groups, bool):
        """
        This function returns a dataframe with the mean for both tests on
        each sample size and the difference between these means
        """
        # get the means errors for each sample size
        means = {}
        descriptive = {}
        for key, item in groups:
            # get the mean for both tests for each group
            # (thus each sample size in this case)
            mean = self.get_mean(groups, key)
            # calculate the difference between means
            mean.update({"Difference": abs(mean["perm"] - mean["t_test"])})
            # get the descriptive statistics for each test for each sample size
            describe = self.get_descriptive(groups, key)

            # add mean and descriptive statistics to a dictionary
            means.update({key: mean})
            descriptive.update({key: describe})
        results_df = pd.DataFrame.from_dict(means, orient="index")

        # change order based on deviations if true then change sample order
        # else change order of sd
        if bool:
            results_df = results_df.reindex(self.sample_order)
        # else:
        #     results_df = results_df.reindex([1, 0.75, 1.25, 0.50,
        #                                      1.50, 0.25, 1.75, 3])
        return results_df
