import numpy as np
import random
import matplotlib.pyplot as plt

# Define the city structure as a tuple of x, y coordinates
cities = [
    (60, 200), (180, 200), (80, 180), (140, 180),
    (20, 160), (100, 160), (200, 160), (140, 140),
    (40, 120), (100, 120), (180, 100), (60, 80),
    (120, 80), (180, 60), (20, 40), (100, 40),
    (200, 40), (20, 20), (60, 20), (160, 20)
]

num_cities = len(cities)
pop_size = 50
max_gen = 10000
crossover_rate = 0.7
mutation_rate = 0.01
def initialize_population():
    population = []
    for _ in range(pop_size):
        individual = list(range(num_cities))
        random.shuffle(individual)
        population.append(individual)
    return population

def calculate_fitness(individual):
    total_distance = 0
    for i in range(num_cities):
        start_city = cities[individual[i]]
        end_city = cities[individual[(i + 1) % num_cities]]
        total_distance += np.hypot(start_city[0] - end_city[0], start_city[1] - end_city[1])
    return 1 / total_distance

def select(population):
    tournament_size = 5
    selected = random.sample(population, tournament_size)
    selected = sorted(selected, key=calculate_fitness, reverse=True)
    return selected[0]

def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        start, end = sorted(random.sample(range(num_cities), 2))
        child = [None] * num_cities
        child[start:end] = parent1[start:end]
        child_pos = end
        for city in parent2:
            if city not in child:
                if child_pos >= num_cities:
                    child_pos = 0
                child[child_pos] = city
                child_pos += 1
        return child
    return parent1

def mutate(individual):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(num_cities), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

def genetic_algorithm():
    population = initialize_population()
    best_solution = None
    best_fitness = float('inf')

    for generation in range(max_gen):
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = select(population)
            parent2 = select(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1)
            mutate(child2)
            new_population.extend([child1, child2])
        population = new_population

        current_best = min(population, key=calculate_fitness)
        current_best_fitness = calculate_fitness(current_best)
        if current_best_fitness < best_fitness:
            best_fitness = current_best_fitness
            best_solution = current_best

    return best_solution, 1 / best_fitness

best_solution, best_distance = genetic_algorithm()
print("Best route:", best_solution)
print("Minimum distance:", best_distance)
