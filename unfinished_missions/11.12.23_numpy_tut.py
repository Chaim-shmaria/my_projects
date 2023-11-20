# # Task
# The goal of the exercise is to analyze the test scores of 20 students over 5 dates and 7 courses. The scores are stored in a 3D array of shape (20, 5, 7).
#
# Here is the description of the steps to perform the exercise:
#
# 1. Find the average of each course: Calculate the mean of all the scores for each of the 7 courses across all 20 students and 5 dates. This will give you the average score for each course. (shape - (7,))
#
#
#
# 2. Find the spread of each student
#     Compute the average across time of the minimum score in each date for each student (20,):
#     For each student, find the minimum score across all 7 courses (20,5).
#     Then, calculate the mean of these minimum scores across all dates for each student.
#
#     do it again with the maximum score in each date
#
#     Return the difference: Subtract the average of the minimum scores from the average of the maximum scores to get the difference.
#
# Overall, this exercise requires using the numpy library to manipulate the 3D array of scores, perform element-wise operations, and calculate means and extrema.


import matplotlib.pyplot as plt
import numpy as np

# Generate random scores using a skewed distribution
np.random.seed(42)
scores = 100 - (np.random.gamma(2, 1, (20, 5, 7)) * 10)
scores = scores.astype(int)

# Plot the histogram of the scores

plt.hist(scores.reshape(-1), bins=30, edgecolor='black')
plt.show()

scores.shape
