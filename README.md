# Distributed Computing Practicals – Viva & Execution Notes

## Practical 1 – RPC Factorial Program

### Title
Design a distributed application using RPC where client sends a number to server and server returns factorial.

### Aim
To implement client-server communication using RPC.

### Files
- `pr_1_server.py`
- `pr_1_client.py`

### Workflow
```text
Client → Sends number → Server calculates factorial → Result returned
```

### Commands

#### Windows
```powershell
python pr_1_server.py
python pr_1_client.py
```

#### Linux
```bash
python3 pr_1_server.py
python3 pr_1_client.py
```

### Important Viva Questions

#### What is RPC?
RPC (Remote Procedure Call) allows a client to call functions on a remote server as if they were local functions.

#### What is the role of client?
Client sends request to server.

#### What is the role of server?
Server processes request and returns response.

#### What operation is performed?
Factorial calculation.

### One-Line Viva Answer
```text
Client sends integer → Server computes factorial → Result returned.
```

---

# Practical 2 – RMI String Concatenation (Python XML-RPC Version)

## Title
Design a distributed application where client sends two strings and server returns concatenated string.

## Why XML-RPC instead of Pyro5?
XML-RPC is easier because:
- built into Python
- no installation required
- simple client-server communication

Pyro5 is more advanced and requires extra setup.

## Files
- `server.py`
- `client.py`

## Workflow
```text
Client → Sends two strings → Server concatenates → Result returned
```

## Commands

### Windows
```powershell
python server.py
python client.py
```

### Linux
```bash
python3 server.py
python3 client.py
```

## Important Viva Questions

### What is RMI?
RMI allows methods to be invoked remotely over a network.

### What is XML-RPC?
XML-RPC is a protocol used for remote function calls using XML over HTTP.

### What is the remote method?
```python
concatenate(a, b)
```

### Sample Output
```text
Enter first string: Hello
Enter second string: World
Concatenated String: HelloWorld
```

### One-Line Viva Answer
```text
Client sends strings → Server concatenates → Result returned.
```

---

# Practical 3 – Hadoop MapReduce Simulation (Word Count)

## Title
Character Count and Word Count using MapReduce.

## Aim
To simulate MapReduce processing using Python.

## Files
- `mapper.py`
- `reducer.py`
- `input.txt`

## Workflow
```text
Input File → Mapper → Sorting → Reducer → Final Output
```

## Windows Commands

```powershell
Get-Content input.txt | python mapper.py > mapped.txt
Get-Content mapped.txt | Sort-Object > sorted.txt
Get-Content sorted.txt | python reducer.py
```

## Linux Commands

```bash
cat input.txt | python3 mapper.py > mapped.txt
sort mapped.txt > sorted.txt
cat sorted.txt | python3 reducer.py
```

## Mapper Function
Breaks input into words and emits:
```text
(word, 1)
```

## Reducer Function
Adds counts of repeated words.

## Important Viva Questions

### What is Hadoop?
Hadoop is a distributed framework for processing big data.

### What is MapReduce?
A programming model for distributed data processing.

### What is Mapper?
Processes input and generates key-value pairs.

### What is Reducer?
Combines values of same keys.

### One-Line Viva Answer
```text
Mapper generates word counts and Reducer sums them.
```

---

# Practical 4 / 5 – Load Balancing Algorithms

## Title
Simulate client requests and distribute them using load balancing algorithms.

## Algorithms Used
- Round Robin
- Random
- Least Connections

## File
- `load_balancer.py`

## Workflow
```text
Clients → Load Balancer → Servers
```

## Commands

### Windows
```powershell
python load_balancer.py
```

### Linux
```bash
python3 load_balancer.py
```

## Algorithm Differences

| Algorithm | Working |
|---|---|
| Round Robin | Requests assigned one-by-one cyclically |
| Random | Requests assigned randomly |
| Least Connections | Request goes to least loaded server |

## Simple Explanation

### Round Robin
```text
S1 → S2 → S3 → S1
```

### Random
Any server selected randomly.

### Least Connections
Request goes to server with minimum active connections.

## Important Viva Questions

### What is Load Balancing?
Distributing requests among multiple servers efficiently.

### Why is load balancing needed?
- avoids overload
- improves performance
- increases scalability

### Which algorithm is best?
Least Connections is generally better because it checks current server load.

### One-Line Viva Answer
```text
Load balancing distributes requests across multiple servers efficiently.
```

---

# Quick Viva Memory Tricks

## RPC
```text
Remote function call
```

## RMI
```text
Remote method invocation
```

## MapReduce
```text
Mapper splits → Reducer combines
```

## Round Robin
```text
One by One
```

## Least Connections
```text
Minimum Load
```
