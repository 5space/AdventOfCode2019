class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xv = 0
        self.yv = 0
        self.zv = 0
    
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

moons = [Moon(x=-13, y=14, z=-7),
         Moon(x=-18, y=9, z=0),
         Moon(x=0, y=-3, z=-3),
         Moon(x=-15, y=3, z=-13)]
# moons = [Moon(x=-1, y=0, z=2),
#          Moon(x=2, y=-10, z=-7),
#          Moon(x=4, y=-8, z=8),
#          Moon(x=3, y=5, z=-1)]

for _ in range(1000):
    for m in moons:
        others = moons.copy()
        others.remove(m)
        m.update_velocity(others)
    for m in moons:
        m.update_position()

print(sum(m.energy() for m in moons))
