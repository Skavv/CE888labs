import matplotlib
matplotlib.use('Agg')
import pandas as pd
import seaborn as sns
import random
import numpy as np
import math


def boostrap(sample, sample_size, iterations):
    array = []
    data_mean = []

    #-----------CI value------------
    percent = 0.05  #10% CI
    #-------------------------------

    for i in range(0, sample_size):
        rand = random.randint(0, sample_size-1)
        array.append(sample[rand])
    array.sort()
    #print(array)
    data_mean = np.mean(array)

    #calculate number of elements to remove from list
    res = percent*sample_size
    res = math.floor(res)

    for i in range(0, res):
        array.pop(i)
    #print(array)

    for i in range(sample_size-1, sample_size-res-1, -1):
        array.pop(i-1)
    #print(array)
    #print("")
    lower = min(array)
    upper = max(array)

    return data_mean, lower, upper


if __name__ == "__main__":
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