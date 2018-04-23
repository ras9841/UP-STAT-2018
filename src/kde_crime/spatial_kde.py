# Imports
import numpy as np 
import pandas as pd
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

from plot_utils import roc_plot

# Response Encodings
CLASS_NVC = -1
CLASS_VC = 1

def map_to_class(stat_cc):
    if stat_cc < 5: # Violent
        return CLASS_VC
    elif stat_cc < 8: # Non-violent
        return CLASS_NVC
    else: # Unknown or nan
        return np.NaN

def process_RPD_data(data_loc):
    # Read in data
    data = pd.read_csv(data_loc, sep=",")
    label = "Statute_CrimeCategory"
    df_xyl = data[["X", "Y"]]
    df_xyl["class"] = data[label].apply(map_to_class) 

    # Remove rows with NAs
    null_rows = df_xyl.isnull().any(axis=1)
    print("Dropping %d rows with null (X,Y,Label) values" %sum(null_rows))
    df_cleaned_xy = df_xyl[list(map(lambda x: not x, null_rows))]

    return df_cleaned_xy

def generate_KDE(data, plotCity=False, plotDensities=False):
    # Separate based on class
    nvc_idx = data.index[data["class"] == CLASS_NVC]
    vc_idx = data.index[data["class"] == CLASS_VC]
    df_nvc = data.loc[nvc_idx]
    df_vc = data.loc[vc_idx]

    # Setup city grid
    extreme_vals = lambda X: (X.min(), X.max())
    xmin, xmax = extreme_vals(data["X"])
    ymin, ymax = extreme_vals(data["Y"])
    xgrid, ygrid = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    xygrid = np.vstack([xgrid.ravel(), ygrid.ravel()])


    # Run KDE on each class
    preds = []
    classes = [df_nvc, df_vc]

    for class_df in classes:
        crime_locs = np.vstack([class_df["X"], class_df["Y"]])

        # Compute KDE (using RBF kernel for now)
        kde = stats.gaussian_kde(crime_locs)

        # "Predict" on the grid
        kde_pred = np.reshape(kde(xygrid).T, xgrid.shape)
        preds.append(kde_pred)


    # Convert to probabilities
    num_NVC = sum(nvc_idx)
    num_VC = sum(vc_idx)
    pi_NVC = num_NVC/(num_VC+num_NVC)
    pi_VC = num_VC/(num_VC+num_NVC)

    p_of_x = np.array(preds[0]*pi_NVC + preds[1]*pi_VC)
    probs = [preds[0]*pi_NVC/p_of_x, preds[1]*pi_VC/p_of_x]

    if plotDensities:
        # Plot density estimates
        xvals = np.round(np.linspace(xmin, xmax, 100), 3)
        yvals = np.round(np.linspace(ymin, ymax, 100), 3)
        scale = lambda x: (x - np.min(preds))/(np.max(preds)-np.min(preds))
        scaled_preds = list(map(scale, preds))
        fig, axn = plt.subplots(1, 2, sharex=True, sharey=True)
        names = ["Non-violent Density", "Violent Density"]
        for i, ax, name in zip([0, 1], axn.flat, names):
            sns.heatmap(scaled_preds[i], ax=ax, cbar = i == 1, vmin = 0,\
                    vmax = 1, cmap = "Reds")
            ax.set_title(name)
            ax.set_xticklabels(xvals)
            ax.set_yticklabels(yvals)
            ax.get_xaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
            ax.get_yaxis().set_minor_locator(mpl.ticker.AutoMinorLocator())
            ax.grid(b=True, which='major', color='k', alpha=1, linewidth=1.0)
            ax.grid(b=True, which='minor', color='k', alpha=1, linewidth=0.5)
        fig.tight_layout()
        plt.savefig('output.png', dpi=300)
        plt.show()

    if plotCity:
        # Plot city boundary
        # x=>long, y=>lat
        roc_plot(xgrid, ygrid, probs[0])

    return probs

if __name__ == "__main__":
    data_loc = "../../data/RPD_crime2011toNow.csv"
    data = process_RPD_data(data_loc)
    print("Completed Processing.")
    probs = generate_KDE(data, plotCity=True)

