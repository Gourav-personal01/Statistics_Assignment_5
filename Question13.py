# Q13. A coffee shop owner wants to estimate the average daily revenue for their shop. They take a random
# sample of 50 days and find the sample mean revenue to be $500 with a standard deviation of $50.
# Estimate the population mean revenue with a 95% confidence interval.

sample_mean = 500
population_std_dev = 50
sample_size = 50
confidence_level = 0.95
z_critical = 1.96  # For a 95% confidence level

margin_of_error = z_critical * (population_std_dev / (sample_size ** 0.5))
confidence_interval_lower = sample_mean - margin_of_error
confidence_interval_upper = sample_mean + margin_of_error

print("Sample Mean:", sample_mean)
print("Confidence Interval (95%):", (confidence_interval_lower, confidence_interval_upper))
