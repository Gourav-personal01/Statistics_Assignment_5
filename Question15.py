# Q15. An electronics company produces a certain type of product with a mean weight of 5 pounds and a
# standard deviation of 0.5 pounds. A random sample of 25 products is taken, and the sample mean weight
# is found to be 4.8 pounds. Test the hypothesis that the true mean weight of the products is less than 5
# pounds with a significance level of 0.01.

# Answer - 
population_mean = 5
standard_devaition = 0.5
sample_size = 25
sample_mean = 4.8
alpha = 0.01

# Null hypothesis = population mean = 5
# alternate hypothesis = population mean =! 5

z_test = (4.8-5)/(0.5*5)

print(z_test)

p_value = 0.46812

if p_value < alpha:
    print("reject the null hypothesis")
else:
    print("accept the null hypothesis")