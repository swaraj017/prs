import xmlrpc.client

# Connect to server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Take input from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remote method call
result = proxy.concatenate(str1, str2)

# Print result
print("Concatenated String:", result)