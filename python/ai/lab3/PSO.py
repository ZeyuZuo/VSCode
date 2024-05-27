import random
import numpy as np

# 城市坐标
cities = [
    (60, 200), (180, 200), (80, 180), (140, 180),
    (20, 160), (100, 160), (200, 160), (140, 140),
    (40, 120), (100, 120), (180, 100), (60, 80),
    (120, 80), (180, 60), (20, 40), (100, 40),
    (200, 40), (20, 20), (60, 20), (160, 20)
]
num_cities = len(cities)
num_particles = 30
max_iter = 100
v_max = 4
c1 = c2 = 2.0

# 初始化粒子
class Particle:
    def __init__(self):
        self.position = np.random.permutation(num_cities)
        self.velocity = np.zeros(num_cities)
        self.best_position = self.position.copy()
        self.best_score = float('inf')

    def update_velocity(self, global_best_position):
        for i in range(num_cities):
            rand_c1 = random.random()
            rand_c2 = random.random()
            cognitive = c1 * rand_c1 * (self.best_position[i] - self.position[i])
            social = c2 * rand_c2 * (global_best_position[i] - self.position[i])
            self.velocity[i] = (self.velocity[i] + cognitive + social) / 2
            self.velocity[i] = np.clip(self.velocity[i], -v_max, v_max)

    def update_position(self):
        self.position = np.mod(self.position + self.velocity, num_cities).astype(int)
        np.random.shuffle(self.position)  # Ensuring random permutation

    def calculate_cost(self):
        total_distance = 0
        for i in range(num_cities):
            start_city = cities[self.position[i]]
            next_city = cities[self.position[(i + 1) % num_cities]]
            total_distance += np.hypot(start_city[0] - next_city[0], start_city[1] - next_city[1])
        return total_distance

particles = [Particle() for _ in range(num_particles)]
global_best_position = None
global_best_score = float('inf')

# 主算法循环
for iteration in range(max_iter):
    for particle in particles:
        cost = particle.calculate_cost()
        if cost < particle.best_score:
            particle.best_score = cost
            particle.best_position = particle.position.copy()
        if cost < global_best_score:
            global_best_score = cost
            global_best_position = particle.position.copy()

    for particle in particles:
        particle.update_velocity(global_best_position)
        particle.update_position()

print("Best score:", global_best_score)
print("Best route:", global_best_position)
