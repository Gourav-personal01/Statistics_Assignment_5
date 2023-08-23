# Q2. Write a Python function to estimate the population mean using a sample mean and standard
# deviation.

# Answer - 

def estimate_population_mean(sample_mean,standard_deviation,sample_size):
     population_mean = sample_mean * sample_size ** 0.5/standard_deviation
     print(population_mean)
     return population_mean

sample_mean = 50
sample_size = 100
standard_deviation = 50
estimate_population_mean(sample_mean,standard_deviation,sample_size)