import itertools
import random

# Available servers
servers = ["Server A", "Server B", "Server C"]

# ROUND ROBIN
rr_cycle = itertools.cycle(servers)

def round_robin():
    return next(rr_cycle)

# RANDOM
def random_selection():
    return random.choice(servers)

# LEAST CONNECTIONS
def least_connections(connections):
    return min(connections, key=connections.get)

# SIMULATION FUNCTION
def simulate(algorithm, total_requests=6):

    # Reset connections for each algorithm
    connections = {
        "Server A": 0,
        "Server B": 0,
        "Server C": 0
    }

    print("\n" + "="*40)
    print(f"Algorithm: {algorithm.upper()}")
    print("="*40)

    for i in range(1, total_requests + 1):

        if algorithm == "round robin":
            server = round_robin()

        elif algorithm == "random":
            server = random_selection()

        elif algorithm == "least connections":
            server = least_connections(connections)

        # Increase load
        connections[server] += 1

        print(f"Request {i} -> {server}")

    print("\nServer Loads:")

    for server in connections:
        print(f"{server}: {connections[server]}")

# MAIN
simulate("round robin")
simulate("random")
simulate("least connections")