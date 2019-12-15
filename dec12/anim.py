import imageio
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import axes3d, Axes3D

class Moon:
    def __init__(self, x, y, z, xv=0, yv=0, zv=0):
        self.x = x
        self.y = y
        self.z = z
        self.xv = xv
        self.yv = yv
        self.zv = zv
    
    def energy(self):
        return (abs(self.x)+abs(self.y)+abs(self.z)) * (abs(self.xv)+abs(self.yv)+abs(self.zv))
    
    def update_velocity(self, other_moons):
        for moon in other_moons:
            if moon.x > self.x: self.xv += 1
            elif moon.x < self.x: self.xv -= 1
            if moon.y > self.y: self.yv += 1
            elif moon.y < self.y: self.yv -= 1
            if moon.z > self.z: self.zv += 1
            elif moon.z < self.z: self.zv -= 1
    
    def update_position(self):
        self.x += self.xv
        self.y += self.yv
        self.z += self.zv

# moons = [Moon(x=-13, y=14, z=-7),
#          Moon(x=-18, y=9, z=0),
#          Moon(x=0, y=-3, z=-3),
#          Moon(x=-15, y=3, z=-13)]
# moons = [Moon(x=-1, y=0, z=2),
#          Moon(x=2, y=-10, z=-7),
#          Moon(x=4, y=-8, z=8),
#          Moon(x=3, y=5, z=-1)]
moons = [Moon(40, 0, 0, 0, 20, 0), Moon(-40, 0, 0, 0, -20, 0)]

fig = plt.figure()
ax = Axes3D(fig)
plt.autoscale(True)

current = 0
delay = 20

xs = [[], [], [], []]
ys = [[], [], [], []]
zs = [[], [], [], []]

ax.set_xlim([-100, 100])
ax.set_ylim([-100, 100])
ax.set_zlim([-100, 100])

lines = []
for i in range(len(moons)):
    lines.append(ax.plot([], [], [])[0])

def init():
    for i in range(len(moons)):
        lines[i].set_data([], [])
        lines[i].set_3d_properties([])
    return lines

def animate(frame):
    print(frame)
    for m in moons:
        others = moons.copy()
        others.remove(m)
        m.update_velocity(others)
    for m in moons:
        m.update_position()
    for i in range(len(moons)):
        xs[i].append(moons[i].x)
        ys[i].append(moons[i].y)
        zs[i].append(moons[i].z)
        lines[i].set_data(xs[i][-delay:], ys[i][-delay:])
        lines[i].set_3d_properties(zs[i][-delay:])
    return lines

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()