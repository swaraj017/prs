# Implementation of Clonal selection algorithm using Python.

import random

# Fitness function
# Goal: minimize f(x) = x^2

def fitness(x):
    return x * x

# Step 1: Initialize population
population = [random.uniform(-10, 10) for i in range(5)]

generations = 10

for g in range(generations):

    # Step 2: Evaluate fitness
    population.sort(key=fitness)

    # Best antibodies
    best = population[:2]

    clones = []

    # Step 3: Cloning and Mutation
    for b in best:
        for i in range(3):  # create 3 clones
            mutation = random.uniform(-1, 1)
            clone = b + mutation
            clones.append(clone)

    # Step 4: New population
    population = best + clones

    # Keep only best 5
    population.sort(key=fitness)
    population = population[:5]

    print("Generation", g+1)
    print("Best Solution =", population[0])
    print("Fitness =", fitness(population[0]))
    print()

print("Final Best Solution =", population[0])


# OUTPUT :
#========== CLONAL SELECTION ALGORITHM ==========

# Generation 1
# -------------------------
# Best Antibody : [1, 1, 0, 1, 0, 1, 1, 0]
# Best Fitness  : 5

# Generation 2
# -------------------------
# Best Antibody : [1, 1, 1, 1, 0, 1, 1, 0]
# Best Fitness  : 6

# ...

# ========== FINAL RESULT ==========
# Best Solution : [1, 1, 1, 1, 1, 1, 1, 1]
# Best Fitness  : 8
# ==================================


# Problem Statement :
# Implement Clonal Selection Algorithm in Python to find the best solution from a population.

# The algorithm works like the human immune system:
# 1.Generate random antibodies.
# 2.Calculate fitness.
# 3.Select best antibodies.
# 4.Clone selected antibodies.
# 5.Mutate clones.
# 6.Replace weak antibodies.
# 7.Display best solution.

# Goal: Maximize the number of 1s in a binary string.

# 1. How to Run in VS Code
# Open VS Code

# 2.Create a new file:
# clonal_selection.py

# 3.Paste the code
# Save the file

# 4.Open terminal:
# Terminal → New Terminal
# Run:
# python clonal_selection.py
# or
# python3 clonal_selection.py

# Code Explanation

# 1.Population:
# Group of random antibodies.

# 2.Antibody:
# One possible solution, for example:

# [1, 0, 1, 1, 0, 1, 0, 1]

# 3.Fitness Function:
# Counts number of 1s.
# def fitness(antibody):
#     return sum(antibody)
# Higher fitness means better solution.

# 4.Selection:
# Best antibodies are selected.
# selected = population[:5]

# 5.Cloning:
# Selected antibodies are copied many times.

# 6.Mutation:
# Some bits are randomly changed from 0 to 1 or 1 to 0.

# 7.Replacement:
# Weak antibodies are removed and replaced by new random antibodies.


# Viva Questions

# Q1. What is Clonal Selection Algorithm?
# It is an optimization algorithm inspired by the immune system.

# Q2. What is antibody?
# An antibody is one possible solution.

# Q3. What is fitness?
# Fitness measures the quality of a solution.

# Q4. What is cloning?
# Cloning means creating copies of selected best antibodies.

# Q5. What is mutation?
# Mutation means randomly changing values in an antibody.

# Q6. What is the goal of this program?
# To find a binary string with maximum number of 1s.

# Q7. Why are weak antibodies replaced?
# To maintain diversity in the population.

# Q8. What is the best fitness in this program?
# The best fitness is 8 because string length is 8.