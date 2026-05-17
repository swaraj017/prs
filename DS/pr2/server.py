from xmlrpc.server import SimpleXMLRPCServer

# Function to concatenate two strings
def concatenate(a, b):
    return a + b

# Create server at localhost and port 8000
server = SimpleXMLRPCServer(("localhost", 8000))

print("Server running on port 8000...")

# Register function
server.register_function(concatenate, "concatenate")

# Keep server running
server.serve_forever()