/**
 * @author: Zeyu Zuo
 * @date: 2024-05-27 19:21:36
 */
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

struct Item {
    int weight;
    int value;
};

// Global variables
const int NUM_ITEMS = 5;
const int CAPACITY = 50;
const int POP_SIZE = 100;
const int MAX_GEN = 50;
const double CROSSOVER_RATE = 0.7;
const double MUTATION_RATE = 0.01;
vector<Item> items = {{10, 20}, {20, 30}, {30, 40}, {40, 50}, {10, 60}};
vector<vector<int>> population;

// Initialize population with random solutions
void initializePopulation() {
    population.resize(POP_SIZE, vector<int>(NUM_ITEMS));
    for (auto& individual : population) {
        for (int i = 0; i < NUM_ITEMS; ++i) {
            individual[i] = rand() % 2;
        }
    }
}

// Calculate fitness as total value of items in the knapsack
int calculateFitness(const vector<int>& individual) {
    int totalWeight = 0, totalValue = 0;
    for (int i = 0; i < NUM_ITEMS; ++i) {
        if (individual[i] == 1) {
            totalWeight += items[i].weight;
            totalValue += items[i].value;
        }
    }
    if (totalWeight > CAPACITY) return 0; // Penalize overcapacity
    return totalValue;
}

// Tournament selection
vector<int> select() {
    int best = rand() % POP_SIZE;
    for (int i = 0; i < 3; ++i) { // Tournament size of 4
        int next = rand() % POP_SIZE;
        if (calculateFitness(population[next]) > calculateFitness(population[best]))
            best = next;
    }
    return population[best];
}

// Single point crossover
void crossover(vector<int>& parent1, vector<int>& parent2) {
    if (double(rand()) / RAND_MAX < CROSSOVER_RATE) {
        int point = rand() % NUM_ITEMS;
        for (int i = point; i < NUM_ITEMS; ++i) {
            swap(parent1[i], parent2[i]);
        }
    }
}

// Mutation
void mutate(vector<int>& individual) {
    for (int i = 0; i < NUM_ITEMS; ++i) {
        if (double(rand()) / RAND_MAX < MUTATION_RATE) {
            individual[i] = 1 - individual[i]; // Flip bit
        }
    }
}

// Genetic algorithm to solve the knapsack problem
void geneticAlgorithm() {
    initializePopulation();
    for (int gen = 0; gen < MAX_GEN; ++gen) {
        vector<vector<int>> newPopulation;
        for (int i = 0; i < POP_SIZE / 2; ++i) {
            vector<int> parent1 = select(), parent2 = select();
            crossover(parent1, parent2);
            mutate(parent1);
            mutate(parent2);
            newPopulation.push_back(parent1);
            newPopulation.push_back(parent2);
        }
        population = newPopulation;
    }

    // Find the best solution in the final population
    int bestFitness = 0, bestIndex = 0;
    for (int i = 0; i < POP_SIZE; ++i) {
        int fitness = calculateFitness(population[i]);
        if (fitness > bestFitness) {
            bestFitness = fitness;
            bestIndex = i;
        }
    }
    cout << "Best solution fitness: " << bestFitness << endl;
    cout << "Items selected: ";
    for (int i = 0; i < NUM_ITEMS; ++i) {
        if (population[bestIndex][i] == 1)
            cout << i << " ";
    }
    cout << endl;
}

int main() {
    srand((unsigned)time(nullptr));
    geneticAlgorithm();
    return 0;
}
