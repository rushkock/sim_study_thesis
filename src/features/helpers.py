#!/usr/bin/env python
# Name: Ruchella Kock
# Student number: 1815458
import pandas as pd
import numpy as np
import researchpy as rp
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
                 "pval", "typeI", "sig"]
        df.columns = names

        # make a new column with the difference between the two tests
        df["dif"] = df["perm"] - df["t_test"]
        return df

    def get_df_all_results(self, file):
        # read csv into dataframe
        df = pd.read_csv(file)
        # rename columns
        names = ["index", "samp1", "samp2", "es", "sd1", "sd2", "k", "perm",
                 "t_test"]
        df.columns = names
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
        sig = group["sig"].iloc[0]
        means = {"perm": perm, "t_test": t_test, "sig": sig}
        return means

    def get_descriptive(self, groups, key):
        """
        Get the descriptive statistics of a group
        """
        group = groups.get_group(key)
        perm = group["perm"].describe()
        t_test = group["t_test"].describe()
        means = {"perm": perm, "t_test": t_test}
        return means

    def boxplots(self, groups, nrows, ncols, type):
        """
        make a boxplot with n number of rows and n number of columns
        """
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
            mean.update({"Difference": mean["perm"] - mean["t_test"]})
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

    def mcnemar(self, df):
        """
        This function performs the mcnemar test and returns a df with the results
        """
        table, res = rp.crosstab(df['perm'], df['t_test'], test='mcnemar')
        return res

    def means_and_pval(self, means, df):
        """
        This function combines the dataframe with means from get_mean_df with
        its pvalues from the mcnemar test
        """
        list = np.arange(len(df))
        for i, (key, item) in zip(list, df):
            res = self.mcnemar(item)
            means.loc[means.index[i], "p_value"] = res["results"][1]
        return means

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

        # make barchart for permutation test
        ax.bar(index, df["perm"], bar_width, color='b', linewidth=4,
               label='Permutation test')
        # make barchart for t-test
        ax.bar(index + bar_width, df["t_test"], bar_width, color='r',
               label='t-test')

        ax.set_xlabel(dict["xlabel"])
        ax.set_ylabel(dict["ylabel"])
        ax.set_title(dict["title"])
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(dict["xtickslabels"])
        ax.legend()

        fig.tight_layout()
        plt.show()

    def multiple_bars(self, df, nrows, ncols, dict):
        """
        Makes a bar chart with mutliple plots in one figure
        """
        fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=(6, 9.3))

        fig.subplots_adjust(left=0.03, right=0.97, hspace=0.50, wspace=0.05)

        bar_width = 0.35
        for ax, (key, dat) in zip(axs.flatten(), df):
            n_groups = len(dat.index)
            index = np.arange(n_groups)

            # make barchart for permutation test
            bar1 = ax.bar(index, dat["perm"], bar_width, color='b',
                      label='Permutation test')
            # make barchart for t-test
            bar2 = ax.bar(index + bar_width, dat["t_test"], bar_width, color='r',
                      label='t-test')

            ax.set_ylabel("Error")
            ax.set_xticks(index + bar_width / 2)
            ax.set_xticklabels(dict["xtickslabels"])
            ax.set_title(f"Effect size = {key}")
            ax.set_xlabel(f"Group Size")
            ax.legend()

            for rect, i in zip(bar1 + bar2, dat["sig"]):
                height = rect.get_height()
                if i:
                    ax.text(rect.get_x() + rect.get_width(), height, "**", ha='center', va='bottom')


        fig.suptitle(dict["title"], y=1.0, fontsize = 15)
        fig.tight_layout()
        plt.show()
