from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(7,7))
m = Basemap(projection='ortho', resolution=None, lat_0=50, lon_0=-100)
m.bluemarble()
plt.show()

m = Basemap(projection='lcc', resolution=None, lat_1=45, lat_2=55, lat_0=50, lon_0=-107, width=12000000, height=9000000)
m.bluemarble()
plt.show()

m = Basemap(projection='mill', resolution='c',
            llcrnrlat=-90, llcrnrlon=-180, urcrnrlat=90, urcrnrlon=180) 
m.drawcoastlines()
m.drawcountries()
m.drawstates(color='b')
m.drawcounties(color='darkred')

plt.title('Basemap Tutorial')
plt.show()
