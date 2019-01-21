import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Scatterplot for both
#histogram seperately

def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
    df = pd.read_csv('./vehiclesNoNulls.csv')
    df2 = pd.read_csv('./vehicles.csv')
    print((df.columns))
    # -------------------------------current fleet-----------------------------------------------
    sns_plot = sns.lmplot(df2.columns[2], df2.columns[0], data=df2, fit_reg=False)

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )

    sns_plot.savefig("scaterplotCurr.png", bbox_inches='tight')
    sns_plot.savefig("scaterplotCurr.pdf", bbox_inches='tight')

#-------------------------------new fleet--------------------------------------------------------
    sns_plot = sns.lmplot(df2.columns[2], df2.columns[1], data=df2, fit_reg=False)

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )

    sns_plot.savefig("scaterplotNew.png", bbox_inches='tight')
    sns_plot.savefig("scaterplotNew.pdf", bbox_inches='tight')

#------------------------------------------------------------------------------------------------

    data = df.values.T[1]

    print((("Mean: %f") % (np.mean(data))))
    print((("Median: %f") % (np.median(data))))
    print((("Var: %f") % (np.var(data))))
    print((("std: %f") % (np.std(data))))
    print((("MAD: %f") % (mad(data))))

    plt.clf()
    sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

    axes = plt.gca()
    axes.set_xlabel('New fleet')
    axes.set_ylabel('Current fleet')

    sns_plot2.savefig("histogram.png", bbox_inches='tight')
    sns_plot2.savefig("histogram.pdf", bbox_inches='tight')