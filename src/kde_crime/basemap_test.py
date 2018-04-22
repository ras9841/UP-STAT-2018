from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Rochester locations
lower_left_long = -77.701
lower_left_lat = 43.145
upper_right_long = -77.682
upper_right_lat = 43.106

"""
map = Basemap(resolution="h", epsg=5520,  
        llcrnrlat=lower_left_lat,
        llcrnrlon=lower_left_long,
        urcrnrlat=upper_right_lat,
        urcrnrlon=upper_right_long)
"""

m = Basemap(projection='lcc', resolution='h',\
        lat_0=43.161, lon_0=-77.611,\
        width=8e4, height=5e4)
m.drawcounties(color='gray')
m.drawparallels(np.linspace(43.106, 43.145, 10))
m.drawmeridians(np.linspace(-77.70, -77.682, 10))
plt.show()
