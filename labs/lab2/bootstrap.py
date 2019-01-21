import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import random
import numpy as np
import math


def boostrap(sample, sample_size, iterations):
    array = []
    meansArray = []

    #-----------CI value------------
    percent = 90  #10% CI
    #-------------------------------

    for i in range(0, iterations):
        for i in range(0, sample_size):
            rand = random.randint(0, sample_size - 1)
            array.append(sample[rand])
        meansArray.append(np.mean(array))
        array.clear()


    #print(meansArray)

    data_mean = np.mean(meansArray)
    lower = np.percentile(meansArray, (100 - percent)/2)
    upper = np.percentile(meansArray, percent + (100 - percent)/2)
    #print(upper)
    #print(lower)
    #print("")

    return data_mean, lower, upper


if __name__ == "__main__":
    mode = 2
    if mode == 1:
        df = pd.read_csv('./salaries.csv')

        data = df.values.T[1]
        boots = []
        for i in range(100, 100000, 1000):
            boot = boostrap(data, data.shape[0], i)
            boots.append([i, boot[0], "mean"])
            boots.append([i, boot[1], "lower"])
            boots.append([i, boot[2], "upper"])

        df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
        sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

        sns_plot.axes[0, 0].set_ylim(0,)
        sns_plot.axes[0, 0].set_xlim(0, 100000)

        sns_plot.savefig("bootstrap_confidence.png", bbox_inches='tight')
        sns_plot.savefig("bootstrap_confidence.pdf", bbox_inches='tight')

        var_a = "Mean: %f" % np.mean(data)
        var_b = "Var: %f" % np.var(data)

        print(var_a)
        print(var_b)
    else:
        #-----------------Bootstrap(2)--------------------------

        df = pd.read_csv('./vehicles.csv')

        data = df.values.T[0]
        data2 = df.values.T[1]

        boots = []
        for i in range(100, 100000, 1000):
            boot = boostrap(data, data.shape[0], i)
            boots.append([i, boot[0], "mean"])
            boots.append([i, boot[1], "lower"])
            boots.append([i, boot[2], "upper"])

        df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
        sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

        sns_plot.axes[0, 0].set_ylim(0, )
        sns_plot.axes[0, 0].set_xlim(0, 100000)

        sns_plot.savefig("bootstrap_confidenceCurr.png", bbox_inches='tight')
        sns_plot.savefig("bootstrap_confidenceCurr.pdf", bbox_inches='tight')

        var_a = "Mean of current fleet: %f" % np.mean(data)
        var_b = "Var of current fleet: %f" % np.var(data)

        print(var_a)
        print(var_b)

        """boots.clear()
        for i in range(100, 100000, 1000):
            boot = boostrap(data2, data2.shape[0], i)
            boots.append([i, boot[0], "mean"])
            boots.append([i, boot[1], "lower"])
            boots.append([i, boot[2], "upper"])
        var_a = "Mean of new fleet: %f" % np.mean(data)
        var_b = "Var of new fleet: %f" % np.var(data)

        df_boot = pd.DataFrame(boots, columns=['Boostrap Iterations', 'Mean', "Value"])
        sns_plot = sns.lmplot(df_boot.columns[0], df_boot.columns[1], data=df_boot, fit_reg=False, hue="Value")

        sns_plot.axes[0, 0].set_ylim(0, )
        sns_plot.axes[0, 0].set_xlim(0, 100000)

        sns_plot.savefig("bootstrap_confidenceNew.png", bbox_inches='tight')
        sns_plot.savefig("bootstrap_confidenceNew.pdf", bbox_inches='tight')

        print(var_a)
        print(var_b)"""
        #-------------------------------------------------------