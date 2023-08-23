# Q17. A marketing company wants to estimate the average number of ads watched by viewers during a TV
# program. They take a random sample of 50 viewers and find that the sample mean is 4 with a standard
# deviation of 1.5. Estimate the population mean with a 99% confidence interval.



sample_mean = 4
population_std_dev = 1.5
sample_size = 50
confidence_level = 0.98
z_critical = 0.16109 # For a 95% confidence level

margin_of_error = z_critical * (population_std_dev / (sample_size ** 0.5))
confidence_interval_lower = sample_mean - margin_of_error
confidence_interval_upper = sample_mean + margin_of_error

print("Sample Mean:", sample_mean)
print("Confidence Interval (98%):", (confidence_interval_lower, confidence_interval_upper))