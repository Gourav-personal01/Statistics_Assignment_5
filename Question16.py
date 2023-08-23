# Q16. Two groups of students are given different study materials to prepare for a test. The first group (n1 =
# 30) has a mean score of 80 with a standard deviation of 10, and the second group (n2 = 40) has a mean
# score of 75 with a standard deviation of 8. Test the hypothesis that the population means for the two
# groups are equal with a significance level of 0.01.

import numpy as np
from scipy import stats

# Group 1 data
n1 = 30
mean1 = 80
std_dev1 = 10

# Group 2 data
n2 = 40
mean2 = 75
std_dev2 = 8

# Significance level
alpha = 0.01

# Calculate the pooled standard deviation
pooled_std_dev = np.sqrt(((std_dev1 ** 2) * (n1 - 1) + (std_dev2 ** 2) * (n2 - 1)) / (n1 + n2 - 2))

# Calculate the t-statistic
t_statistic = (mean1 - mean2) / (pooled_std_dev * np.sqrt((1 / n1) + (1 / n2)))

# Calculate the degrees of freedom
degrees_of_freedom = n1 + n2 - 2

# Calculate the p-value
p_value = 2 * (1 - stats.t.cdf(np.abs(t_statistic), df=degrees_of_freedom))

# Compare the p-value with the significance level to make a decision
if p_value < alpha:
    print("Reject the null hypothesis: The population means are not equal.")
else:
    print("Fail to reject the null hypothesis: The population means are equal.")

print("t-statistic:", t_statistic)
print("p-value:", p_value)
