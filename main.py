import rebound
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import mplcursors
from matplotlib.widgets import Slider

sim = rebound.Simulation()

sim.add(m=1)

bodies = [
    {"name": "Mercury", "m": 1.66012e-7, "a": 0.241, "e": 0.2056, "inc": 7.0, "omega": 28.58, "Omega": 47.94, "f": 90.0},
    {"name": "Venus", "m": 2.4478383e-6, "a": 0.615, "e": 0.0068, "inc": 3.39, "omega": 55.19, "Omega": 76.68, "f": 50.0},
    {"name": "Earth", "m": 3e-6, "a": 1, "e": 0.0167, "inc": 0.0, "omega": 288.1, "Omega": 174.9, "f": 357.3},
    {"name": "Moon", "m": 3.694e-8, "a": 0.2, "e": 0.0549, "inc": 5.145, "omega": 83.3, "Omega": 125.08, "f": 14.73},
    {"name": "Mars", "m": 3.227151445e-7, "a": 1.5237, "e": 0.0934, "inc": 1.85, "omega": 286.5, "Omega": 49.58, "f": 19.36},
    {"name": "Jupiter", "m": 0.0009543, "a": 5.2026, "e": 0.0484, "inc": 1.304, "omega": 273.9, "Omega": 100.46, "f": 20.2},
    {"name": "Saturn", "m": 0.0002857, "a": 9.5549, "e": 0.0555, "inc": 2.485, "omega": 339.4, "Omega": 113.64, "f": 317.0},
    {"name": "Uranus", "m": 4.365e-5, "a": 19.2184, "e": 0.0463, "inc": 0.772, "omega": 97.9, "Omega": 73.98, "f": 142.2},
    {"name": "Neptune", "m": 5.149e-5, "a": 30.1104, "e": 0.0096, "inc": 1.769, "omega": 276.8, "Omega": 131.78, "f": 256.3}
]
for body in bodies:
    sim.add(m=body["m"], a=body["a"], e=body["e"], inc=np.radians(body["inc"]), omega=np.radians(body["omega"]), Omega=np.radians(body["Omega"]), f=np.radians(body["f"]))


moon = {"name": "Moon", "m": 3.694e-8, "a": 0.2, "e": 0.0549, "inc": 5.145, "omega": 83.3, "Omega": 125.08, "f": 14.73}
earth = sim.particles[3] 
sim.add(m=moon["m"], a=moon["a"], e=moon["e"], inc=np.radians(moon["inc"]), omega=np.radians(moon["omega"]), Omega=np.radians(moon["Omega"]), f=np.radians(moon["f"]), primary=earth)



Noutputs = 300 #300
year = 2.*np.pi  
times = np.linspace(0.,1.*year, Noutputs)

###########################################################################################################################################################
#Solor System Axis

x = np.zeros((10,Noutputs))
y = np.zeros((10,Noutputs))
z = np.zeros((10,Noutputs))

fig = plt.figure(figsize=(5,5))

ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=30., azim=30)


###########################################################################################################################################################
#Mercury Axis

Mer_x = np.zeros(Noutputs)
Mer_y = np.zeros(Noutputs)
Mer_z = np.zeros(Noutputs)

for i, t in enumerate(times):
    sim.integrate(t)
    for j in range(10):
        x[j][i], y[j][i], z[j][i] = sim.particles[j].x, sim.particles[j].y, sim.particles[j].z
    Mer_x[i], Mer_y[i], Mer_z[i] = sim.particles[1].x, sim.particles[1].y, sim.particles[1].z

fig_mer = plt.figure(figsize=(5,5))
ax_mer = fig_mer.add_subplot(111, projection='3d')
ax_mer.view_init(elev=30., azim=30) 

##########################################################################################################################################################



#Earth, Moon Axis

earth_x = np.zeros(Noutputs)
earth_y = np.zeros(Noutputs)
earth_z = np.zeros(Noutputs)

for i, t in enumerate(times):
    sim.integrate(t)
    for j in range(10):
        x[j][i], y[j][i], z[j][i] = sim.particles[j].x, sim.particles[j].y, sim.particles[j].z
    earth_x[i], earth_y[i], earth_z[i] = sim.particles[3].x, sim.particles[3].y, sim.particles[3].z

#Primary
moon_x = np.zeros(Noutputs)
moon_y = np.zeros(Noutputs)
moon_z = np.zeros(Noutputs)

for i, t in enumerate(times):
    sim.integrate(t)
    for j in range(10):
        x[j][i], y[j][i], z[j][i] = sim.particles[j].x, sim.particles[j].y, sim.particles[j].z
    #earth_x[i], earth_y[i], earth_z[i] = sim.particles[3].x, sim.particles[3].y, sim.particles[3].z
    moon_x[i], moon_y[i], moon_z[i] = sim.particles[4].x, sim.particles[4].y, sim.particles[4].z

fig_earth = plt.figure(figsize=(5,5))
ax_earth = fig_earth.add_subplot(111, projection='3d')
ax_earth.view_init(elev=30., azim=30) 

##########################################################################################################################################################
# Mars

mars_x = np.zeros(Noutputs)
mars_y = np.zeros(Noutputs)
mars_z = np.zeros(Noutputs)

for i, t in enumerate(times):
    sim.integrate(t)
    for j in range(10):
        x[j][i], y[j][i], z[j][i] = sim.particles[j].x, sim.particles[j].y, sim.particles[j].z
    mars_x[i], mars_y[i], mars_z[i] = sim.particles[5].x, sim.particles[5].y, sim.particles[5].z

fig_mars = plt.figure(figsize=(5,5))
ax_mars = fig_mars.add_subplot(111, projection='3d')
ax_mars.view_init(elev=30., azim=30) 

##########################################################################################################################################################
# Update function for animation
def animate(i):
    
    ax.clear()
    ax.text2D(0.05, 0.95, 'General Simulate', transform=ax.transAxes, color='white') # Add text in each frame
    ax_earth.clear()
    ax_earth.text2D(0.05, 0.95, 'Earth Simulate', transform=ax_earth.transAxes, color='Black') # Add text in each frame
    ax_mars.clear()
    ax_mars.text2D(0.05, 0.95, 'Mars Simulate', transform=ax_mars.transAxes, color='Black') # Add text in each frame
    ax_mer.clear()
    ax_mer.text2D(0.05, 0.95, 'Mercury Simulate', transform=ax_mer.transAxes, color='Black') # Add text in each frame
    

    ax.grid(True)
    ax_earth.grid(True)
    ax_mars.grid(True)
    ax_mer.grid(True)
    

    ax.set_facecolor('black') 
    ax_earth.set_facecolor('white') 
    ax_mars.set_facecolor('white')
    ax_mer.set_facecolor('white')

    colors = ['orange', 'grey', 'yellow', 'blue', 'grey', 'red', 'orange', 'khaki', 'aqua', 'blue', 'purple']
    sizes = [109.25, 0.383, 0.950, 1, 0.532, 10.97, 9.14, 3.98, 3.87, 0.187] 
    for j in range(10):
        ax.scatter(x[j][i], y[j][i], z[j][i], color=colors[j], s=sizes[j]) 
    fig.suptitle('General Simulate', color='white') # Set subtitle once and change color to white

 ###########################################################################################################################################################
    ax_mer.scatter(0, 0, 0, color='grey', s=1000 / 109)
    
    dist_mer_sun = 0.39

    sun_x_mer = -dist_mer_sun * np.cos(i/88 * 2 * np.pi)
    sun_y_mer = -dist_mer_sun * np.sin(i/88 * 2 * np.pi)
    sun_z_mer = 0

    ax_mer.scatter([sun_x_mer], [sun_y_mer], [sun_z_mer], color='orange', s=1000)
 ###########################################################################################################################################################
    ax_earth.scatter(0, 0, 0, color='blue', s=1000 / 109)
    ax_earth.scatter(moon_x[i], moon_y[i], moon_z[i], color='grey', s=1000 / 400)

    dist_earth_sun = 1

    sun_x = -dist_earth_sun * np.cos(i/365.25 * 2 * np.pi)
    sun_y = -dist_earth_sun * np.sin(i/365.25 * 2 * np.pi)
    sun_z = 0

    ax_earth.scatter([sun_x], [sun_y], [sun_z], color='orange', s=1000)

 ###########################################################################################################################################################
    ax_mars.scatter(0, 0, 0, color='grey', s=1000 / 285)

    dist_mars_sun = 1.5237

    sun_x_mars = -dist_mars_sun * np.cos(i/687.0 * 2 * np.pi)
    sun_y_mars = -dist_mars_sun * np.sin(i/687.0 * 2 * np.pi)
    sun_z_mars = 0

    ax_mars.scatter([sun_x_mars], [sun_y_mars], [sun_z_mars], color='orange', s=1000)

 ###########################################################################################################################################################
    
    ax_earth.set_xlim([-2, 2])
    ax_earth.set_ylim([-2, 2])
    ax_earth.set_zlim([-2, 2])
    ax_earth.set_xlabel("X")
    ax_earth.set_ylabel("Y")
    ax_earth.set_zlabel("Z")

    ax_mer.set_xlim([-2, 2])
    ax_mer.set_ylim([-2, 2])
    ax_mer.set_zlim([-2, 2])
    ax_mer.set_xlabel("X")
    ax_mer.set_ylabel("Y")
    ax_mer.set_zlabel("Z")

    ax_mars.set_xlim([-2, 2])
    ax_mars.set_ylim([-2, 2])
    ax_mars.set_zlim([-2, 2])
    ax_mars.set_xlabel("X")
    ax_mars.set_ylabel("Y")
    ax_mars.set_zlabel("Z")

    ax.set_xlim([-3.5, 3.5])
    ax.set_ylim([-3.5, 3.5])
    ax.set_zlim([-3.5, 3.5])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=Noutputs, interval=100)
ani_earth = animation.FuncAnimation(fig_earth, animate, frames=Noutputs, interval=100)
ani_mars = animation.FuncAnimation(fig_mars, animate, frames=Noutputs, interval=100)
ani_mer = animation.FuncAnimation(fig_mer, animate, frames=Noutputs, interval=100)

plt.show()

