# Q14. A researcher hypothesizes that a new drug will decrease blood pressure by 10 mmHg. They conduct a
# clinical trial with 100 patients and find that the sample mean decrease in blood pressure is 8 mmHg with a
# standard deviation of 3 mmHg. Test the hypothesis with a significance level of 0.05.

# Answer - 
population_mean = 10
sample_mean = 8
standard_deviation = 3
sample_size = 100
alpha = 0.05
z_critical = 1.96  # for 0.05 significance 

# Null Hypothesis (H0) - population mean = 10
# Alternate Hypothesis - population mean =! 10

# Experiment - 
z_test = (10-8)/(3/10)
print(z_test)

if z_test >= z_critical:
    print("Reject the Null Hypothesis")
else:
    print("Failed to reject the Null hypothesis, the drug has impact")