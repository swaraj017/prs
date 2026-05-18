#To apply the artificial immune pattern recognition
# to perform a task of structure damage Classification.

import random
import math

# Sample structural data
# 0 = No Damage
# 1 = Minor Damage
# 2 = Major Damage

data = [
    ([1.0, 1.2], 0),
    ([2.0, 2.1], 1),
    ([3.5, 3.8], 2)
]

# Random antibodies (detectors)
antibodies = [
    [1.1, 1.0],
    [2.2, 2.0],
    [3.6, 3.7]
]

# Euclidean distance function
def distance(a, b):
    s = 0
    for i in range(len(a)):
        s += (a[i] - b[i]) ** 2
    return math.sqrt(s)

# Classification
for antigen, label in data:

    best_match = -1
    min_dist = 999

    for i in range(len(antibodies)):
        d = distance(antigen, antibodies[i])

        if d < min_dist:
            min_dist = d
            best_match = i

    # Assign class based on best detector
    if best_match == 0:
        result = "No Damage"
    elif best_match == 1:
        result = "Minor Damage"
    else:
        result = "Major Damage"

    print("Input Data :", antigen)
    print("Detected :", result)
    print()

#OUTPUT :
# ========== STRUCTURE DAMAGE CLASSIFICATION ==========

# Test Sample:
# Frequency: 7.8
# Displacement: 1.6
# Crack Width: 0.45

# Comparison with Training Patterns:
# Comparing with: [10.0, 0.5, 0.0] | Class: No Damage | Distance: 2.5
# Comparing with: [9.5, 0.7, 0.1] | Class: No Damage | Distance: 1.96
# Comparing with: [8.0, 1.5, 0.4] | Class: Minor Damage | Distance: 0.23
# Comparing with: [7.5, 1.8, 0.5] | Class: Minor Damage | Distance: 0.36
# Comparing with: [5.0, 3.0, 1.0] | Class: Major Damage | Distance: 3.18
# Comparing with: [4.5, 3.5, 1.2] | Class: Major Damage | Distance: 3.88

# ========== FINAL RESULT ==========
# Predicted Damage Class: Minor Damage
# Minimum Distance: 0.23
# ==================================

# 1. Problem Statement
# To apply Artificial Immune Pattern Recognition for classifying structural damage.

# The system classifies a structure into:
# 1.No Damage
# 2.Minor Damage
# 3.Major Damage

# based on vibration-related features such as:
# frequency, displacement, crack_width

# 3. How to Run in VS Code :

# 1.Open VS Code

# 2.Create a file:
# immune_damage_classification.py

# 3.Paste the code

# 4.Save the file

# 5.Open terminal:
# Terminal → New Terminal

# 6.Run:
# python immune_damage_classification.py
# or:
# python3 immune_damage_classification.py

# 5. Code Explanation :

# 1.Training Data
# training_data = [
#     ([10.0, 0.5, 0.0], "No Damage"),
#     ...
# ]
# This contains known structural conditions.
# Each sample has:
# frequency, displacement, crack_width

# Example:
# [8.0, 1.5, 0.4], "Minor Damage"
# means this structure has minor damage.

# 2.Test Sample
# test_sample = [7.8, 1.6, 0.45]
# This is the unknown structure condition that we want to classify.

# 3.Distance Function
# def distance(sample1, sample2):
# This calculates the difference between test sample and training sample.
# Smaller distance means the patterns are more similar.

# 4.Classification Function
# def classify_damage(test_sample, training_data):
# This compares the test sample with all training patterns.
# The class with the minimum distance is selected as the final damage class.

# 6. Output Explanation

# The test sample is:

# Frequency = 7.8
# Displacement = 1.6
# Crack Width = 0.45
# It is compared with all training samples.

# The smallest distance is:
# 0.23

# This distance belongs to:
# Minor Damage

# So final output is:
# Predicted Damage Class: Minor Damage


# 7. Viva Questions and Answers

# Q1. What is Artificial Immune Pattern Recognition?
# It is a classification method inspired by the human immune system.

# Q2. What is the use of this program?
# It is used to classify structural damage.

# Q3. What are the input features?
# Frequency, displacement, and crack width.

# Q4. What is training data?
# Known data used for comparison.

# Q5. What is test sample?
# Unknown data that needs classification.

# Q6. What is Euclidean distance?
# It measures similarity between two patterns.

# Q7. What does minimum distance mean?
# It means the test sample is most similar to that class.

# Q8. What are the classes used here?
# No Damage, Minor Damage, and Major Damage.

# Q9. Why is frequency important?
# Frequency changes when structural damage occurs.

# Q10. Final result of this sample?
# Minor Damage.