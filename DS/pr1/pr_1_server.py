from xmlrpc.server import SimpleXMLRPCServer

# Function to calculate factorial
def factorial(n):
    fact = 1

    if n < 0:
        return "Factorial not possible for negative numbers"

    for i in range(1, n + 1):
        fact = fact * i

    return fact

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))

print("Server is running on port 8000...")

# Register function
server.register_function(factorial, "factorial")

# Run server forever
server.serve_forever()