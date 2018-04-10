import numpy as np 
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

CLASS_NVC = -1
CLASS_VC = 1

def extreme_vals(data):
    return data.min(), data.max()

def map_to_class(stat_cc):
    if stat_cc < 5: # Violent
        return CLASS_VC
    elif stat_cc < 8: # Non-violent
        return CLASS_NVC
    else: # Unknown or nan
        return np.NaN

def main():
    # Read in crime data
    data = pd.read_csv("../../data/RPD_crime2011toNow.csv", sep=",")
    label = "Statute_CrimeCategory"
    df_xyl = data[["X", "Y"]]
    df_xyl["class"] = data[label].apply(map_to_class) 

    # Remove rows with NAs
    null_rows = df_xyl.isnull().any(axis=1)
    print("Dropping %d rows with null (X,Y,Label) values" %sum(null_rows))
    df_cleaned_xy = df_xyl[list(map(lambda x: not x, null_rows))]


    # Separate based on class
    nvc_idx = df_cleaned_xy.index[df_cleaned_xy["class"] == CLASS_NVC]
    vc_idx = df_cleaned_xy.index[df_cleaned_xy["class"] == CLASS_VC]
    df_nvc = df_cleaned_xy.loc[nvc_idx]
    df_vc = df_cleaned_xy.loc[vc_idx]

    # Setup city grid
    xmin, xmax = extreme_vals(data["X"])
    ymin, ymax = extreme_vals(data["Y"])
    xgrid, ygrid = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
    xygrid = np.vstack([xgrid.ravel(), ygrid.ravel()])
    
    preds = []
    classes = [df_nvc, df_vc]

    for class_df in classes:
        crime_locs = np.vstack([class_df["X"], class_df["Y"]])

        # Compute KDE (using RBF kernel for now)
        kde = stats.gaussian_kde(crime_locs)

        # "Predict" on the grid
        kde_pred = np.reshape(kde(xygrid).T, xgrid.shape)
        preds.append(kde_pred)
    
    # Plot density estimates
    fig, axn = plt.subplots(1, 2, sharex=True, sharey=True)
    names = ["Non-violent Density", "Violent Density"]
    for i, ax, name in zip([0, 1], axn.flat, names):
        sns.heatmap(preds[i], ax=ax,\
                cbar = i == 1,\
                cmap = "Reds")
        ax.set_title(name)


    plt.show()

if __name__ == "__main__":
    main()
