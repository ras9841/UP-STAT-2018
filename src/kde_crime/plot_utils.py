from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def roc_plot(long, lat, data):
    # Setup inputs
    m = long.shape[0]*long.shape[1]
    long = long.reshape(m)
    lat = lat.reshape(m)
    data = data.reshape(m)

    # Load in locations
    places = pd.read_csv("../../data/ROC_places.csv",\
            names=["Name", "Lat", "Long"])


    m = Basemap(projection='lcc', resolution='h',\
            lat_0=np.mean(lat), lon_0=np.mean(long),\
            width=3e4, height=3e4)
    
    m.drawcoastlines(color="black")
    m.drawrivers(color="black")
    m.drawparallels(np.linspace(lat[0], lat[-1], 5), labels=[1,0,0,0])
    meridians = m.drawmeridians(np.linspace(long[-1], long[0], 5), labels=[0,0,0,1])
    for merid in meridians:
        meridians[merid][1][0].set_rotation(45)

    m.scatter(long, lat, latlon=True,\
            c=data, cmap='Blues')
    plt.colorbar(label="Probability")
    plt.clim(0,1)

    # Plot known places
    m.scatter(places["Long"].values, places["Lat"].values,\
            latlon=True, color="black")
    for name, n_lat, n_long in places.values:
        plt.annotate(name, xy=m(n_long, n_lat), xytext=m(n_long, n_lat+0.003))
    plt.show()
