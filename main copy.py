import rebound
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

sizes = [109.25, 0.383, 0.950, 1, 0.532, 10.97, 9.14, 3.98, 3.87, 0.187]

for body in bodies:
    sim.add(m=body["m"], a=body["a"], e=body["e"], inc=np.radians(body["inc"]),
            omega=np.radians(body["omega"]), Omega=np.radians(body["Omega"]), f=np.radians(body["f"]))

Noutputs = 300
year = 2.0 * np.pi
times = np.linspace(0., 1.0 * year, Noutputs)

# Set up figure and axes
fig, axs = plt.subplots(2, 2, figsize=(10, 10), subplot_kw={'projection': '3d'})
axs = axs.flatten()
for ax in axs:
    ax.view_init(elev=30., azim=30)

moon_x, moon_y, moon_z = np.zeros(Noutputs), np.zeros(Noutputs), np.zeros(Noutputs)
sun_x_mer, sun_y_mer, sun_z_mer = np.zeros(Noutputs), np.zeros(Noutputs), np.zeros(Noutputs)
sun_x, sun_y, sun_z = np.zeros(Noutputs), np.zeros(Noutputs), np.zeros(Noutputs)
sun_x_mars, sun_y_mars, sun_z_mars = np.zeros(Noutputs), np.zeros(Noutputs), np.zeros(Noutputs)

ax_titles = ['General Simulate', 'Mercury Simulate', 'Earth Simulate', 'Mars Simulate']
colors = ['orange', 'grey', 'yellow', 'blue', 'grey', 'red', 'orange', 'khaki', 'aqua', 'blue', 'purple']

# Create separate animation functions for each subplot
def animate_general(i):
    ax = axs[0]
    ax.clear()
    ax.text2D(0.05, 0.95, 'General Simulate', transform=ax.transAxes, color='white')
    ax.grid(True)
    ax.set_facecolor('black')
    ax.set_xlim([-3.5, 3.5])
    ax.set_ylim([-3.5, 3.5])
    ax.set_zlim([-3.5, 3.5])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    for j in range(10):
        x, y, z = sim.particles[j].x, sim.particles[j].y, sim.particles[j].z
        ax.scatter(x, y, z, color=colors[j], s=sizes[j])

def animate_mercury(i):
    ax = axs[1]
    ax.clear()
    ax.text2D(0.05, 0.95, 'Mercury Simulate', transform=ax.transAxes, color='white')
    ax.grid(True)
    ax.set_facecolor('black')
    ax.set_xlim([-3.5, 3.5])
    ax.set_ylim([-3.5, 3.5])
    ax.set_zlim([-3.5, 3.5])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.scatter(0, 0, 0, color='grey', s=1000 / 109)
    dist_mer_sun = 0.39
    sun_x_mer[i] = -dist_mer_sun * np.cos(i / 88 * 2 * np.pi)
    sun_y_mer[i] = -dist_mer_sun * np.sin(i / 88 * 2 * np.pi)
    ax.scatter([sun_x_mer[i]], [sun_y_mer[i]], [sun_z_mer[i]], color='orange', s=1000)

def animate_earth(i):
    ax = axs[2]
    ax.clear()
    ax.text2D(0.05, 0.95, 'Earth Simulate', transform=ax.transAxes, color='white')
    ax.grid(True)
    ax.set_facecolor('black')
    ax.set_xlim([-3.5, 3.5])
    ax.set_ylim([-3.5, 3.5])
    ax.set_zlim([-3.5, 3.5])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.scatter(0, 0, 0, color='blue', s=1000 / 109)
    ax.scatter(moon_x[i], moon_y[i], moon_z[i], color='grey', s=1000 / 400)
    dist_earth_sun = 1
    sun_x[i] = -dist_earth_sun * np.cos(i / 365.25 * 2 * np.pi)
    sun_y[i] = -dist_earth_sun * np.sin(i / 365.25 * 2 * np.pi)
    ax.scatter([sun_x[i]], [sun_y[i]], [sun_z[i]], color='orange', s=1000)

def animate_mars(i):
    ax = axs[3]
    ax.clear()
    ax.text2D(0.05, 0.95, 'Mars Simulate', transform=ax.transAxes, color='white')
    ax.grid(True)
    ax.set_facecolor('black')
    ax.set_xlim([-3.5, 3.5])
    ax.set_ylim([-3.5, 3.5])
    ax.set_zlim([-3.5, 3.5])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.scatter(0, 0, 0, color='grey', s=1000 / 285)
    dist_mars_sun = 1.5237
    sun_x_mars[i] = -dist_mars_sun * np.cos(i / 687.0 * 2 * np.pi)
    sun_y_mars[i] = -dist_mars_sun * np.sin(i / 687.0 * 2 * np.pi)
    ax.scatter([sun_x_mars[i]], [sun_y_mars[i]], [sun_z_mars[i]], color='orange', s=1000)

# Create separate animations for each subplot
ani_general = animation.FuncAnimation(fig, animate_general, frames=Noutputs, interval=100)
ani_mercury = animation.FuncAnimation(fig, animate_mercury, frames=Noutputs, interval=100)
ani_earth = animation.FuncAnimation(fig, animate_earth, frames=Noutputs, interval=100)
ani_mars = animation.FuncAnimation(fig, animate_mars, frames=Noutputs, interval=100)

# Show the animations
plt.show()
