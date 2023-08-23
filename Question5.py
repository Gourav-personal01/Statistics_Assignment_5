# Q5. Write a Python script to conduct a hypothesis test on the difference between two population means,
# given a sample from each population.

import numpy as np
from scipy import stats

sample1 = np.array([65, 70, 68, 72, 75, 78, 68, 71, 73, 70])
sample2 = np.array([60, 62, 65, 63, 67, 64, 61, 63, 62, 60])


significance_value = 0.05
degrees_of_freedom = 18

t_statistics,p_value = stats.ttest_ind(sample1,sample2,alternative='two-sided')
print(t_statistics)
print(p_value)
print(degrees_of_freedom)


if p_value < significance_value:
    print("Reject the Null hypothesis, There is a significant change in population mean ")
else:
    print("Failed to reject the Null hyposthes. there is no significant change in population mean")