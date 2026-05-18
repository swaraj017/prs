# Implement Union, Intersection, Complement and Difference operations on fuzzy sets. Also create fuzzy relations 
# by Cartesian product of any two fuzzy sets and perform max-min composition on any two fuzzy relations.

# Fuzzy Set Operations (Beautified Output)

import numpy as np

# Define fuzzy sets
A = np.array([0.2, 0.5, 0.7, 0.9])
B = np.array([0.3, 0.6, 0.4, 0.8])

print("Fuzzy Set A =", A)
print("Fuzzy Set B =", B)

# 1. Union
union = np.maximum(A, B)
print("\nUnion of A and B:")
print(union)

# 2. Intersection
intersection = np.minimum(A, B)
print("\nIntersection of A and B:")
print(intersection)

# 3. Complement
complement_A = 1 - A
print("\nComplement of A:")
print(complement_A)

# 4. Difference (A - B)
difference = np.maximum(0, A - B)
print("\nDifference of A - B:")
print(difference)

# ---------------------------------------------------
# Fuzzy Relation using Cartesian Product
# ---------------------------------------------------

# Cartesian product relation using min operation
R1 = np.minimum.outer(A, B)

print("\nFuzzy Relation R1 (Cartesian Product of A and B):")
print(R1)

# Define another fuzzy set C
C = np.array([0.4, 0.7, 0.5])

print("\nFuzzy Set C =", C)

# Second fuzzy relation R2 using B and C
R2 = np.minimum.outer(B, C)

print("\nFuzzy Relation R2 (Cartesian Product of B and C):")
print(R2)

# ---------------------------------------------------
# Max-Min Composition
# ---------------------------------------------------

# R1 is (A x B)
# R2 is (B x C)
# Result will be (A x C)

rows = R1.shape[0]
cols = R2.shape[1]

R3 = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        values = []
        for k in range(R1.shape[1]):
            values.append(min(R1[i][k], R2[k][j]))
        R3[i][j] = max(values)

print("\nMax-Min Composition R3:")
print(R3)

# OUTPUT :
# ========== FUZZY SET OPERATIONS ==========

# Fuzzy Set A
# -----------
# x1 : 0.20
# x2 : 0.70
# x3 : 1.00

# Fuzzy Set B
# -----------
# x1 : 0.50
# x2 : 0.40
# x3 : 0.80

# Union (A ∪ B)
# -------------
# x1 : 0.50
# x2 : 0.70
# x3 : 1.00

# Intersection (A ∩ B)
# --------------------
# x1 : 0.20
# x2 : 0.40
# x3 : 0.80

# Complement (A')
# ---------------
# x1 : 0.80
# x2 : 0.30
# x3 : 0.00

# Difference (A - B)
# ------------------
# x1 : 0.20
# x2 : 0.60
# x3 : 0.20

# Relation R1 = A × C
# -------------------
# (x1, y1) : 0.20
# (x1, y2) : 0.20
# (x2, y1) : 0.60
# (x2, y2) : 0.70
# (x3, y1) : 0.60
# (x3, y2) : 0.90

# Max-Min Composition (R1 ∘ R2)
# -----------------------------
# (x1, x1) : 0.20
# (x1, x2) : 0.20
# ...
# =========== END ===========

# 🟢 1. Problem Statement (Short)

# Implement operations on fuzzy sets:
# Union
# Intersection
# Complement
# Difference
# Also:
# Create fuzzy relations using Cartesian product
# Perform Max-Min Composition

# 🟢 2. Code Explanation (Step-by-step)

# 🔹 Fuzzy Sets
# A = {"x1": 0.2, "x2": 0.7, "x3": 1.0}
# B = {"x1": 0.5, "x2": 0.4, "x3": 0.8}
# C = {"y1": 0.6, "y2": 0.9}
# 👉 These are fuzzy sets
# 👉 Values (0 to 1) = membership values

# 🔹 Union
# def fuzzy_union(A, B):
#     return {x: max(A[x], B[x]) for x in A}
# 👉 Takes maximum value
# 👉 Formula:
# Union = max(A, B)

# 🔹 Intersection
# def fuzzy_intersection(A, B):
#     return {x: min(A[x], B[x]) for x in A}
# 👉 Takes minimum value
# 👉 Formula:
# Intersection = min(A, B)

# 🔹 Complement
# def fuzzy_complement(A):
#     return {x: 1 - A[x] for x in A}
# 👉 Formula:
# Complement = 1 − A

# 🔹 Difference
# def fuzzy_difference(A, B):
#     return {x: min(A[x], 1 - B[x]) for x in A}
# 👉 Formula:
# A − B = min(A, B')

# 🔹 Cartesian Product (Relation)
# def cartesian_product(A, B):
#     return {(x, y): min(A[x], B[y]) for x in A for y in B}
# 👉 Creates relation between A and B
# 👉 Uses min rule

# 🔹 Max-Min Composition
# def max_min_composition(R1, R2):
# 👉 Combines two relations
# Step:
# Take min of matching pairs
# Then take max
# 👉 Formula:
# max(min(R1, R2))

# 🟢 3. Output Explanation
# Example:
# Union (A ∪ B)
# x1 : 0.50
# x2 : 0.70
# x3 : 1.00

# 👉 Explanation:

# x1 → max(0.2, 0.5) = 0.5
# x2 → max(0.7, 0.4) = 0.7
# x3 → max(1.0, 0.8) = 1.0
# Intersection:
# x1 : 0.20
# x2 : 0.40
# x3 : 0.80

# 👉 Taking minimum values

# Complement:
# x1 : 0.80
# x2 : 0.30
# x3 : 0.00

# 👉 Example:
# 1 − 0.2 = 0.8

# Difference:
# x2 : 0.60

# 👉 min(A, 1−B)

# Cartesian Product:
# (x2, y1) : 0.60

# 👉 min(0.7, 0.6) = 0.6

# Max-Min Composition:
# (x1, x1) : 0.20

# 👉 Step:
# Take all paths via y
# Apply min → then max

# 🟢 4. How to Run in VS Code

# ✅ Steps:

# 1. Open VS Code

# 2. Create file:
# fuzzy_operations.py

# 3. Paste code

# 4. Open terminal:
# Terminal → New Terminal

# 5. Run:
# python fuzzy_operations.py

# OR

# python3 fuzzy_operations.py
# ⚠️ If Python not working:
# Check version:
# python --version

# 🟢 5. Viva Questions & Answers

# Q1. What is a fuzzy set?
# 👉 A set where elements have membership values between 0 and 1.

# Q2. What is union in fuzzy set?
# 👉 Maximum of membership values.

# Q3. What is intersection?
# 👉 Minimum of membership values.

# Q4. What is complement?
# 👉 1 − membership value.

# Q5. What is difference?
# 👉 min(A, complement of B).

# Q6. What is fuzzy relation?
# 👉 Relation formed using Cartesian product of fuzzy sets.

# Q7. What is max-min composition?
# 👉 Combination of two relations using max(min()) rule.

# Q8. Why use fuzzy logic?
# 👉 To handle uncertainty and partial truth.

# Q9. Range of membership value?
# 👉 0 to 1.

# Q10. What is Cartesian product?
# 👉 Pairing of elements from two sets.

# 🟢 Final Tip (Exam Trick 💯)

# 👉 Always write formulas:

# Union = max
# Intersection = min
# Complement = 1 − A
# Difference = min(A, B')