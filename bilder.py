import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  
import numpy as np

data_list = []
zz = np.zeros
my_file = open('fahrten.txt', 'r')
zeilen = my_file.readlines()
for zeile in zeilen:
    data_list += [zeile[:-1].split(',')]
my_file.close()
print(data_list)


x_hours = np.linspace(0,23,24)
y_days = np.linspace(1,7,7)
zz = np.zeros((len(y_days), len(x_hours)))
xx, yy = np.meshgrid(x_hours,y_days)
for line in data_list:
    zz[int(line[3])-8][int(line[4])] += 1
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, zz, cmap = cm.coolwarm)

fig2 = plt.figure()
bx = fig2.add_subplot()
cmap = bx.pcolor(xx,yy,zz, cmap = cm.coolwarm)
fig2.colorbar(cmap)

ax.set_xlabel('Hours in the day')
ax.set_ylabel('Day in the week')
plt.yticks(y_days, ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
ax.set_zlabel('Nr of rides')
bx.set_xlabel('Hours in the day')
bx.set_ylabel('Day in the week')
ax.set_zlabel('Nr of rides')

plt.show()