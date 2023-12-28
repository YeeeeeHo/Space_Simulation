import rebound
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

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
    sim.add(m=body["m"], a=body["a"], e=body["e"], inc=np.radians(body["inc"]),
            omega=np.radians(body["omega"]), Omega=np.radians(body["Omega"]), f=np.radians(body["f"]))

moon = {"name": "Moon", "m": 3.694e-8, "a": 0.2, "e": 0.0549, "inc": 5.145, "omega": 83.3, "Omega": 125.08, "f": 14.73}
earth = sim.particles[3] 
sim.add(m=moon["m"], a=moon["a"], e=moon["e"], inc=np.radians(moon["inc"]),
        omega=np.radians(moon["omega"]), Omega=np.radians(moon["Omega"]), f=np.radians(moon["f"]), primary=earth)

Noutputs = 300
year = 2.0 * np.pi  
times = np.linspace(0.0, 1.0 * year, Noutputs)

# Solar System Axis
x = np.zeros((10, Noutputs))
y = np.zeros((10, Noutputs))
z = np.zeros((10, Noutputs))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(elev=30., azim=30)

# Planet Colors and Sizes
colors = ['orange', 'grey', 'yellow', 'blue', 'grey', 'red', 'orange', 'khaki', 'aqua', 'blue', 'purple']
sizes = [109.25, 0.383, 0.950, 1, 0.532, 10.97, 9.14, 3.98, 3.87, 0.187]

fig, axs = plt.subplots(3, 3, figsize=(15, 15))  # 3x3의 subplots 생성
axs = axs.flatten()  # 1D로 변환
fig.subplots_adjust(wspace=0.3, hspace=0.3)  # subplot 간격 조절

# 애니메이션 함수 변경
def animate(i):
    for ax in axs:  # 모든 subplot을 clear
        ax.clear()
        ax.grid(True)
        ax.set_facecolor('black') 
    for j in range(10):
        sim.integrate(times[i])  # Integrate simulation to the current time step
        x[j][i], y[j][i], z[j][i] = sim.particles[j].x, sim.particles[j].y, sim.particles[j].z
        for k in range(10):
            axs[k].scatter(x[j][i], y[j][i], z[j][i], color=colors[j], s=sizes[j])
            axs[k].set_xlim([-3.5, 3.5])
            axs[k].set_ylim([-3.5, 3.5])
            axs[k].set_xlabel("X")
            axs[k].set_ylabel("Y")
    for k in range(len(bodies)):  # 각 subplot에 대한 타이틀 설정
        axs[k].set_title(bodies[k]['name'])

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=Noutputs, interval=100)
plt.show()

