import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def plot_fam(data,output):
    ax=sns.barplot(x=data['samples'],y=data['frequency'],hue=data['family'])
    ax.set(xlabel='Samples', ylabel='Frequency')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title='Families')
    plt.xticks(rotation=90)
    plt.show()
    ax.figure.savefig(f"{output}/families_barplot.png",dpi=1200,bbox_inches="tight")
    return ax