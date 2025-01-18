import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)

m.drawcoastlines()
m.drawmapboundary(fill_color='lightblue')
m.fillcontinents(color='lightgreen', lake_color='lightblue')

# Generate random data
lons = np.random.uniform(-180, 180, 1000)
lats = np.random.uniform(-80, 80, 1000)
x, y = m(lons, lats)
m.scatter(x, y, s=10, marker='o', color='red', zorder=5)

plt.show()