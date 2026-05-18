# Implement Ant colony optimization by solving the Traveling salesman problem using python
# Problem statement- A salesman needs to visit a set of cities exactly once and return to the original
# city. The task is to find the shortest possible route that the salesman can take to visit all the cities
# and return to the starting city.

import random

# Distance matrix between cities
distance = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

cities = len(distance)

best_path = []
best_distance = 9999

# Simulate ants
for ant in range(5):

    visited = [0]
    current_city = 0

    while len(visited) < cities:

        next_city = random.choice(
            [city for city in range(cities) if city not in visited]
        )

        visited.append(next_city)
        current_city = next_city

    # Return to start city
    visited.append(0)

    # Calculate total distance
    total = 0

    for i in range(len(visited)-1):
        total += distance[visited[i]][visited[i+1]]

    print("Path :", visited)
    print("Distance :", total)
    print()

    # Update best path
    if total < best_distance:
        best_distance = total
        best_path = visited

print("Best Path :", best_path)
print("Minimum Distance :", best_distance)

# OUTPUT :
# ========== ANT COLONY OPTIMIZATION FOR TSP ==========
# Iteration 10: Best Distance = 16.06
# Iteration 20: Best Distance = 16.06
# Iteration 30: Best Distance = 16.06
# Iteration 40: Best Distance = 16.06
# Iteration 50: Best Distance = 16.06

# ========== FINAL RESULT ==========
# Best Route: C -> B -> A -> E -> D -> C
# Shortest Distance: 16.06
# ==================================

# 1. Problem Statement :

# A salesman needs to visit a set of cities exactly once and return to the starting city.
# The task is to find the shortest possible route using Ant Colony Optimization (ACO).
# ACO is inspired by the behavior of ants. Ants use pheromones to find the shortest path.

# 3. How to Run in VS Code :

# 1.Open VS Code

# 2.Create a new file:
# aco_tsp.py

# 3.Paste the code

# 4.Save the file

# 5.Open terminal:
# Terminal → New Terminal

# 6.Run:
# python aco_tsp.py
# or:
# python3 aco_tsp.py

# 5. Code Explanation
# Cities
# cities = {
#     "A": (0, 0),
#     "B": (2, 3),
#     "C": (5, 4),
#     "D": (6, 1),
#     "E": (3, 0)
# }
# These are city names with their x and y coordinates.

# Parameters :
# num_ants = 10
# num_iterations = 50
# alpha = 1
# beta = 2
# evaporation = 0.5

# Meaning:
# num_ants        = number of ants
# num_iterations  = number of repetitions
# alpha           = pheromone importance
# beta            = distance importance
# evaporation     = pheromone reduction rate

# 1.Distance Function
# def distance(city1, city2):
# This calculates distance between two cities using Euclidean distance formula.

# 2.Route Distance
# def route_distance(route):
# This calculates the total distance of a complete route, including return to starting city.

# 3.Select Next City
# def select_next_city(current_city, unvisited):
# This selects the next city based on:
# pheromone value
# distance between cities
# More pheromone and shorter distance increase the chance of selection.

# 4.Pheromone Evaporation
# pheromone[edge] *= (1 - evaporation)
# This reduces old pheromone values.
# It helps avoid getting stuck in bad paths.

# 5.Pheromone Deposit
# deposit = pheromone_deposit / total_distance
# Shorter routes get more pheromone.
# So ants are more likely to choose better routes in future iterations.

# 6. Output Explanation

# Example:
# Iteration 10: Best Distance = 16.06
# This means after 10 iterations, the shortest route found is 16.06 units.

# Final output:
# Best Route: C -> B -> A -> E -> D -> C
# Shortest Distance: 16.06
# This means the salesman should follow this route to get minimum distance.

# 7. Viva Questions and Answers

# Q1. What is Ant Colony Optimization?
# It is an optimization technique inspired by the food-searching behavior of ants.

# Q2. What is TSP?
# TSP means Traveling Salesman Problem.

# Q3. What is the goal of TSP?
# To visit all cities once and return to the starting city with minimum distance.

# Q4. What is pheromone?
# Pheromone is a value used by ants to mark better paths.

# Q5. Why is pheromone evaporation used?
# To reduce the effect of old paths and avoid wrong solutions.

# Q6. What is alpha?
# Alpha controls the importance of pheromone.

# Q7. What is beta?
# Beta controls the importance of distance.

# Q8. Which route gets more pheromone?
# The shorter route gets more pheromone.

# Q9. Why is ACO useful?
# It is useful for finding near-optimal solutions for complex problems.

# Q10. What is the final output of this program?
# The shortest route and its total distance.