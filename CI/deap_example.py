# Implement DEAP (Distributed Evolutionary Algorithms) using Python.

from deap import base, creator, tools, algorithms
import random

# Fitness Function
# Minimize f(x) = x^2

def evaluate(individual):
    return (individual[0] ** 2,)

# Create Fitness and Individual
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

# Random number generator
toolbox.register("attr_float", random.uniform, -10, 10)

# Individual and Population
toolbox.register("individual", tools.initRepeat,
                 creator.Individual,
                 toolbox.attr_float, 1)

toolbox.register("population", tools.initRepeat,
                 list, toolbox.individual)

# Genetic Operators
toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian,
                 mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament,
                 tournsize=3)

# Create population
population = toolbox.population(n=10)

# Run Genetic Algorithm
algorithms.eaSimple(population,
                    toolbox,
                    cxpb=0.7,
                    mutpb=0.2,
                    ngen=5,
                    verbose=True)

# Best Solution
best = tools.selBest(population, 1)[0]

print("\nBest Solution =", best[0])
print("Fitness =", evaluate(best)[0])

# OUTPUT : 
# gen nevals
# 0   20
# 1   12
# 2   15
# ...
# Best Individual: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Best Fitness: 10.0


# DEAP means Distributed Evolutionary Algorithms in Python. It is used to implement Genetic Algorithms, Evolution Strategies, etc.

# 1. Install DEAP in VS Code terminal
# Open VS Code → Terminal → New Terminal:
# pip install deap

# 2. Create file
# Create a file named:
# filename.py

# 3. Run in VS Code
# In terminal:
# python deap_example.py
# On some systems:
# python3 deap_example.py

# 1. Problem Statement (What are we solving?)
# We are using DEAP (Distributed Evolutionary Algorithms in Python) to solve a simple optimization problem:

# 👉 Goal:
# Find a binary string (list of 0s and 1s) of length 10 such that the sum of all elements is maximum.

# 👉 Example:
# [0,1,0,1,1,0,0,1,0,1] → sum = 5
# [1,1,1,1,1,1,1,1,1,1] → sum = 10 (BEST)

# ✔ So the algorithm tries to evolve the best solution using:
# Selection
# Crossover
# Mutation

# This is similar to natural evolution (survival of the fittest).

# 🔷 2. Code Explanation (Step-by-step)

# 🔹 Import libraries
# import random
# from deap import base, creator, tools, algorithms
# random → generate random values
# deap → main evolutionary algorithm library

# 🔹 Fitness Function
# def evaluate(individual):
#     return (sum(individual),)

# 👉 This function calculates fitness
# 👉 Higher sum = better individual

# ⚠️ Note: Return must be a tuple → (value,)

# 🔹 Create Fitness and Individual
# creator.create("FitnessMax", base.Fitness, weights=(1.0,))
# creator.create("Individual", list, fitness=creator.FitnessMax)
# FitnessMax → we want to maximize
# Individual → each solution is a list

# 🔹 Toolbox (Main setup)
# toolbox = base.Toolbox()

# Toolbox stores all operations.

# 🔹 Attribute & Individual
# toolbox.register("attr_bool", random.randint, 0, 1)
# toolbox.register("individual", tools.initRepeat,
#                  creator.Individual, toolbox.attr_bool, n=10)
# Each gene = 0 or 1
# Individual = list of 10 values

# 🔹 Population
# toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# 👉 Creates many individuals
# 👉 Example: 20 individuals

# 🔹 Genetic Operators
# toolbox.register("evaluate", evaluate)
# toolbox.register("mate", tools.cxTwoPoint)
# toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
# toolbox.register("select", tools.selTournament, tournsize=3)
# Explanation:
# evaluate → calculates fitness
# mate (crossover) → mix two parents
# mutate → randomly flip bits
# select → choose best individuals

# 🔹 Main Function
# def main():
#     population = toolbox.population(n=20)

# 👉 Start with 20 random solutions

# 🔹 Evolution Process
# algorithms.eaSimple(
#     population,
#     toolbox,
#     cxpb=0.5,
#     mutpb=0.2,
#     ngen=10,
#     verbose=True
# )
# Meaning:
# cxpb=0.5 → 50% crossover
# mutpb=0.2 → 20% mutation
# ngen=10 → run for 10 generations

# 👉 Each generation improves solutions

# 🔹 Best Solution
# best = tools.selBest(population, k=1)[0]

# print("\nBest Individual:", best)
# print("Best Fitness:", best.fitness.values[0])

# 👉 Select best individual after evolution

# 🔷 3. Output Explanation
# Sample Output:
# gen nevals
# 0   20
# 1   12
# 2   15
# ...
# Best Individual: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Best Fitness: 10.0

# 🔹 Meaning:
# gen
# Generation number
# nevals
# Number of individuals evaluated

# 🔹 Final Result:
# Best solution = [1,1,1,1,1,1,1,1,1,1]
# Fitness = 10

# 👉 This is the optimal solution


# 1. Short Handwritten-Style Notes (Exam Content)
# ✍️ DEAP (Distributed Evolutionary Algorithm)

# Problem Statement:
# To find the optimal binary string (0s and 1s) of length 10 such that the sum of elements is maximum using Genetic Algorithm.

# Steps:

# Initialize population randomly
# Evaluate fitness (sum of bits)
# Select best individuals
# Apply crossover and mutation
# Repeat for generations
# Display best solution

# Fitness Function:
# Fitness = Sum of all bits

# Result:
# Best Individual = [1,1,1,1,1,1,1,1,1,1]
# Best Fitness = 10

# 🟢 3. Viva Questions & Answers

# Q1. What is DEAP?
# 👉 DEAP is a Python library used to implement evolutionary algorithms like Genetic Algorithm.

# Q2. What is Fitness Function?
# 👉 It measures how good a solution is.

# Q3. What is an Individual?
# 👉 A single solution (list of 0s and 1s).

# Q4. What is Population?
# 👉 Collection of individuals.

# Q5. What is Crossover?
# 👉 Combining two parents to create new offspring.

# Q6. What is Mutation?
# 👉 Random change in an individual.

# Q7. What is Selection?
# 👉 Choosing best individuals for next generation.

# Q8. What is Goal of this Program?
# 👉 To maximize the number of 1s in the binary string.