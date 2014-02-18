import mpl_toolkits.mplot3d.axes3d as axes3d
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib as cm

cos = np.cos
sin = np.sin
sqrt = np.sqrt
pi = np.pi
a = 2.461
k_start_range = 0.0
k_end_range = 2*pi/a
t = 1

# Returns num evenly spaced samples, calculated over the interval [start, stop ].
u, v = np.linspace(0, 2*pi/a, 5), np.linspace(0, 2*pi/a, 5)

# Return coordinate matrices from two or more coordinate vectors.
ux, vx =  np.meshgrid(u,v)
z = t*(3 + 2*cos(2*pi*a*ux) + 2*cos(2*pi*a*vx) + 2*cos(2*pi*a*(ux-vx)) )**(1/2.0)
        
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.set_xlabel('k1')
ax.set_ylabel('k2')
ax.set_zlabel('Energy +')

print 'k1'
print ux
print 'k2'
print vx
print 'Energy'
print z

plot = ax.plot_surface(ux, vx, z, rstride = 1, cstride = 1, cmap = plt.get_cmap('jet'),
                       linewidth = 0, antialiased = False)

plt.show()
